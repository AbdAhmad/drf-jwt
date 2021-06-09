from django.urls import include, path
from rest_framework import routers
from . views import UserViewSet,NotificationListView,NotificationDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('notifications/',NotificationListView.as_view(),name="notification-list"),
    path('notifications/<int:pk>/',NotificationDetailView.as_view(),name="notification-detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]