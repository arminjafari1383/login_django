from rest_framework.routers import DefaultRouter
# from login import Person_router
from django.urls import path, include
router = DefaultRouter()
# router.registry.extend(Person_router.registry)
urlpatterns = [
    path('',include(router.urls)),
    
]