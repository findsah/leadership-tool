from django.contrib import admin
from django.urls import include, path 
from django.conf.urls.static import static
from django.conf import settings 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

from api.views import  RegisterAPI, LoginAPI, LoggedInUser
from knox import views as knox_views 
 
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('get_token/',TokenObtainPairView.as_view(),name='get_token'),
    path('refresh_token/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verify_token/',TokenVerifyView.as_view(),name='verify_token'),
    path('api/register/', RegisterAPI.as_view(), name='register'),

    path('api/auth/user', LoggedInUser.as_view()),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/v1/',include('api.urls'), name='api'), 
    path('api/v2/', include('secondtoll.urls'), name='secondtoll'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Leadership Toll Admin"
admin.site.site_title = "Leadership Toll Admin Portal"
admin.site.index_title = "Welcome to the Leadership Toll Portal"