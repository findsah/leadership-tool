from rest_framework.views import APIView
from rest_framework import status
from .serializers import QuestionSerializer, UserAnswerSerializer
from .models import Question, UserAnswer, QuestionOption
from rest_framework.response import Response
from django.db.models import Count
# Create your views here.

class QuestionAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                que = Question.objects.get(id=pk)
                serializer = QuestionSerializer(que)
                return Response({'data':serializer.data, 'status':status.HTTP_200_OK})
            except Question.DoesNotExist:
                return Response({'data':{}, 'status':status.HTTP_200_OK})
        que = Question.objects.all()
        serializer = QuestionSerializer(que, many=True)
        return Response({'data':serializer.data, 'status':status.HTTP_200_OK})

class SubmitAnswerAPI(APIView):

    def get(self, request, pk=None, format=None):
        user_id = request.GET.get('user_id')
        if pk is not None:
            try:
                if user_id is not None:
                    que = UserAnswer.objects.get(id=pk, user_id=user_id)
                else:
                    que = UserAnswer.objects.get(id=pk)
                serializer = UserAnswerSerializer(que)
                return Response({'data':serializer.data, 'status':status.HTTP_200_OK})
            except UserAnswer.DoesNotExist:
                return Response({'data':{}, 'status':status.HTTP_200_OK})
        if pk is None and user_id is not None:
            que = UserAnswer.objects.filter(user_id=user_id)
            serializer = UserAnswerSerializer(que, many=True)
            return Response({'data':serializer.data, 'status':status.HTTP_200_OK})
        que = UserAnswer.objects.all()
        serializer = UserAnswerSerializer(que, many=True)
        return Response({'data':serializer.data, 'status':status.HTTP_200_OK})
    
    def post(self, request, format=None): 
        serializer = UserAnswerSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            try:
                ins = UserAnswer.objects.get(
                    user_id = serializer.validated_data.get('user'),
                    question_id = serializer.validated_data.get('question')
                    )
            except UserAnswer.DoesNotExist:
                ins = None
            if ins:
                if ins.answer != serializer.validated_data.get('answer'):
                    ins.answer = serializer.validated_data.get('answer')
                    ins.save()
                return Response({'msg':'Record save Successfully', 'data':serializer.data,'status':status.HTTP_200_OK})
            serializer.save()
            return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})
        return Response({'data':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})

class ProgressAPIView(APIView):
  # permission_classes = [permissions.IsAuthenticated] 

  def get(self, request, pk=None, format=None):
    user_id = request.GET.get('user_id', pk)
    if user_id:
        quesryset = Question.objects.all()
        total_q = quesryset.count()  
        completed = UserAnswer.objects.filter(user_id=user_id)
        completed_count =completed.count()
        if completed_count > 0:
            last_q = completed.last().question_id 
            per=int((completed_count*100)/total_q)
            return Response({
                'total_question':total_q,
                'completed_percentage':per,
                'completed_question':completed_count,
                'question_left':total_q-completed_count,
                "last_completed_question":last_q,
                'status':status.HTTP_200_OK
            })
        return Response({'msg':'No Data found for this user','status':status.HTTP_200_OK})    
    return Response({'msg':'User id is required','status':status.HTTP_200_OK})

