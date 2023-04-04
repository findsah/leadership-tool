from django.core.validators import ip_address_validator_map
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView 
import json
from rest_framework import status
from typing import Dict 
from knox.models import AuthToken
# Create your views here.

class QuestionModelViewSet(viewsets.ModelViewSet):
  queryset=Question.objects.all()
  serializer_class=QuestionSerializer
  # authentication=[JWTAuthentication]
  # permission_classes=[IsAuthenticated]
  http_method_names = ['get']

class ResponseModelViewSet(viewsets.ModelViewSet):
    serializer_class=ResponseSerializer
    # authentication=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    def get_queryset(self):
        queryset=UserAnswer.objects.all()
        r_user_id = self.request.GET.get('user_id')
        if r_user_id is not None:
            queryset=UserAnswer.objects.filter(user_id=r_user_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            try:
                queryset=UserAnswer.objects.get(user_id=request.data.get('user_id'), question_id=request.data.get('question'))
            except UserAnswer.DoesNotExist:
                queryset = None
            if queryset:
                queryset.answer = request.data.get('answer')
                queryset.save()
                return Response({'msg':'Record save Successfully','status':status.HTTP_200_OK})
            serializer.save()
            return Response({'msg':'Record save Successfully','data':serializer.data,'status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginUserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoggedInUser(generics.RetrieveAPIView):
  # permission_classes = [
  #     permissions.IsAuthenticated
  # ]
  serializer_class = UserSerializer
  def get_object(self):
    return self.request.user

class ProgressViewSet(viewsets.ViewSet):
  # permission_classes = [permissions.IsAuthenticated]
  def list(self, request):
      return Response(request.data)

  def retrieve(self, request, pk=None):
    total_q = 25

    if pk is not None:
      completed = UserAnswer.objects.filter(user_id=pk).count()
      last_q = UserAnswer.objects.filter(user_id=pk).last().question_id

      per=int((completed*100)/total_q)
      return Response({'completed_percentage':per,'completed_question':completed,'question_left':total_q-completed, "last_completed_question":last_q})

class CalculateLeadershipTypeViewSet(viewsets.ViewSet):
  # permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        return Response(request.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            completed = UserAnswer.objects.filter(user_id=pk)
            if completed.count() > 0:
                qa_dict = {ans.question.question_id:ans.answer for ans in completed} 
                print('qa_dict ',qa_dict)
                leadership_type = self.calculate_leadership_type(qa_dict)
                try:
                    get_leadership=LeadershipType.objects.get(name=leadership_type) 
                    leadership_data = LeadershipTypeSerializer(instance=get_leadership).data  
                except LeadershipType.DoesNotExist:
                    leadership_data={}
                return Response({'leadership_type':leadership_data, 'msg':'Record fetched successfully ','status':status.HTTP_200_OK})
            return Response({'msg':'Data not available for user','status':status.HTTP_200_OK})

    def calculate_leadership_type(self, answers:Dict[int, int]) -> str:
        scores = {
            'Careful Collaborator': 0,
            'Methodical Specialist': 0,
            'Culture Creator': 0,
            'Intuitive Decider': 0,
            'Determined Driver': 0,
            'Collective Adventurer': 0,
        }

        for question_number, answer in answers.items():
            if question_number in ["question_1", "question_6" "question_10", "question_15"]:
                scores['Determined Driver'] += int(answer)
            elif question_number in ["question_2", "question_3", "question_7", "question_16"]:
                scores['Methodical Specialist'] += int(answer)
            elif question_number in ["question_4", "question_8", "question_14", "question_27"]:
                scores['Careful Collaborator'] += int(answer)
            elif question_number in ["question_5", "question_9", "question_12", "question_21", "question_23", "question_25"]:
                scores['Collective Adventurer'] += int(answer)
            elif question_number in ["question_11", "question_17", "question_19", "question_22", "question_26"]:
                scores['Intuitive Decider'] += int(answer)
            elif question_number in ["question_13", "question_18", "question_20", "question_24"]:
                scores['Culture Creator'] += int(answer)
        return max(scores, key=scores.get)


