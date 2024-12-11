from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import get_users, create_users, user_detail

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.yourwebsite.com/terms/",
        contact=openapi.Contact(email="contact@yourwebsite.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('users/', get_users, name='get_users'),
    path('users/create/', create_users, name='create_users'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
]
