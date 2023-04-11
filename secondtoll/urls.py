from django.urls import include, path  
from secondtoll import views

urlpatterns = [ 
    path('submit_answer/', views.SubmitAnswerAPI.as_view()),  
    path('submit_answer/<int:pk>', views.SubmitAnswerAPI.as_view()),  
    path('questions/', views.QuestionAPI.as_view()),  
    path('questions/<int:pk>', views.QuestionAPI.as_view()),  
    path('progress_api/', views.ProgressAPIView.as_view()),  
    path('progress_api/<int:pk>', views.ProgressAPIView.as_view()),  
] 
