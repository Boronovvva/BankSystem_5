from django.urls import path 
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPI

router = DefaultRouter()
router.register('users', UserAPI, basename='api_user')

urlpatterns = router.urls
