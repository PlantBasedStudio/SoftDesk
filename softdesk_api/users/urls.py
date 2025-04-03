from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import UserViewSet, register_user, login_user, UserRetrieveUpdateAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('me/', UserRetrieveUpdateAPIView.as_view(), name='user-details'),
]
