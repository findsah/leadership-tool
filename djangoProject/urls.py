
from django.contrib import admin
from django.urls import path
from qandA import views
from qandA.views import SegmentationView, SegmentationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('', views.home, name='home'),
    # path('grid', views.grid_questions, name='grid'),
    path('', SegmentationView.as_view(), name='segmentation'),
    path('api/', SegmentationAPIView.as_view(), name='segmentation_api'),

]
