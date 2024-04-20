from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import(
    Login
)
Person_router = DefaultRouter()
Person_router.register(r'posts',Login)
urlpatterns = [
    path('login', Login.as_view(),name = 'Login'),
]