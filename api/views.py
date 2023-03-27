from django.core.validators import ip_address_validator_map
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.shortcuts import get_object_or_404
import json
from rest_framework import status
from typing import Dict
# Create your views here.

class QuestionModelViewSet(viewsets.ModelViewSet):
  queryset=Question.objects.all()
  serializer_class=QuestionSerializer
  # authentication=[JWTAuthentication]
  # permission_classes=[IsAuthenticated]
  http_method_names = ['get']

class ResponseModelViewSet(viewsets.ModelViewSet):
  queryset=UserAnswer.objects.all()
  serializer_class=ResponseSerializer
  # authentication=[JWTAuthentication]
  # permission_classes=[IsAuthenticated]

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

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

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
    total_q = 30

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
                qa_dict = {ans.question.id:ans.answer for ans in completed}
                # return Response({'data': qa_dict,'status':status.HTTP_200_OK})
                leadership_type = self.calculate_leadership_type(qa_dict)
                return Response({'leadership_type':leadership_type, 'msg':'Record fetched successfully ','status':status.HTTP_200_OK})
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
            if question_number in [1, 6, 10, 15, ]:
                scores['Determined Driver'] += int(answer)
            elif question_number in [2, 3, 7, 16]:
                scores['Methodical Specialist'] += int(answer)
            elif question_number in [4, 8, 14, 27]:
                scores['Careful Collaborator'] += int(answer)
            elif question_number in [5, 9, 12, 21, 23, 25]:
                scores['Collective Adventurer'] += int(answer)
            elif question_number in [11, 17, 19, 22, 26]:
                scores['Intuitive Decider'] += int(answer)
            elif question_number in [13, 18, 20, 24]:
                scores['Culture Creator'] += int(answer)
        return max(scores, key=scores.get)


