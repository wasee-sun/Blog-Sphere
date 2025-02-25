"""URL mappings for the Blog API."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views


# basename will be singluar eg user
# basename-list (Get /users/ and Post /users/)
# basename-detail (Get /users/id, Put/patch /users/id, Delete /users/id)
# basename-action-name (Post /users/id/upload-image/)
router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"blogs", views.BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('get-csrf-token/', views.CSRFTokenView.as_view(), name='get_csrf_token'),
    # path('retrieve-token/', views.RetrieveTokenView.as_view(), name='retrieve_session_id'),
    path('email-verification/', views.EmailVerificationView.as_view(), name='email_verification'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]