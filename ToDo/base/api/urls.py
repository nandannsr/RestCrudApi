from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MyTokenObtainPairView
from .views import TodoViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]