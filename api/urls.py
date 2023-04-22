from django.urls import include, path  
from api import views
from rest_framework.routers import DefaultRouter 

from api.views import CalculateLeadershipTypeViewSet, ProgressViewSet

router=DefaultRouter()

router.register('question_api', views.QuestionModelViewSet, basename='question')
router.register('response_api', views.ResponseModelViewSet, basename='response')
router.register('user_progress_api', ProgressViewSet, basename='user_progress')
router.register('user_result_api', CalculateLeadershipTypeViewSet, basename='user_result')

urlpatterns = [ 
    path('',include(router.urls)), 
]