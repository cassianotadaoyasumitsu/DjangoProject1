from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User
from .serializer import UserSerializer

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_summary="Get all users",
    operation_description="Retrieve a list of all users in the database.",
    responses={200: UserSerializer(many=True)}
)
@api_view(['GET'])
def get_users(request):
    """
    Retrieve all users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    operation_summary="Create a new user",
    operation_description="Create a new user with the provided details.",
    request_body=UserSerializer,
    responses={
        201: UserSerializer,
        400: "Bad Request: Invalid data"
    }
)
@api_view(['POST'])
def create_users(request):
    """
    Create a new user.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_summary="Get user details",
    operation_description="Retrieve details of a specific user by ID.",
    responses={
        200: UserSerializer,
        404: "Not Found: User does not exist"
    }
)
@swagger_auto_schema(
    method='put',
    operation_summary="Update a user",
    operation_description="Update details of a specific user by ID.",
    request_body=UserSerializer,
    responses={
        200: UserSerializer,
        400: "Bad Request: Invalid data",
        404: "Not Found: User does not exist"
    }
)
@swagger_auto_schema(
    method='delete',
    operation_summary="Delete a user",
    operation_description="Delete a specific user by ID.",
    responses={
        204: "No Content: User deleted",
        404: "Not Found: User does not exist"
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update, or delete a user by ID.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
