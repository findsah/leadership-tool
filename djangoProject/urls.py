from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

from api.views import CalculateLeadershipTypeViewSet, RegisterAPI, LoginAPI, LoggedInUser, ProgressViewSet
from knox import views as knox_views 

router=DefaultRouter()

router.register('question_api', views.QuestionModelViewSet, basename='question')

router.register('response_api', views.ResponseModelViewSet, basename='response')
router.register('user_progress_api', ProgressViewSet, basename='user_progress')
router.register('user_result_api', CalculateLeadershipTypeViewSet, basename='user_result')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include(router.urls)),
    path('get_token/',TokenObtainPairView.as_view(),name='get_token'),
    path('refresh_token/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verify_token/',TokenVerifyView.as_view(),name='verify_token'),
    path('api/register/', RegisterAPI.as_view(), name='register'),

    path('api/auth/user', LoggedInUser.as_view()),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
