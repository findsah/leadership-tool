from django.urls import include, path  
from secondtoll import views

urlpatterns = [ 
    path('questions/', views.QuestionAPI.as_view()),  
    path('questions/<int:pk>', views.QuestionAPI.as_view()),  
] 
