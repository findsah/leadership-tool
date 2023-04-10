from rest_framework.views import APIView
from rest_framework import status
from .serializers import QuestionSerializer, UserAnswerSerializer
from .models import Question, UserAnswer
from rest_framework.response import Response
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
            print('USERID ', request.data['user'])
            print('QUESTIONID ', request.data['question'])
            try:
                ins = UserAnswer.objects.get(
                    user_id = serializer.validated_data.get('user'),
                    question_id = serializer.validated_data.get('question')
                    )
            except UserAnswer.DoesNotExist:
                ins = None
            if ins:
                ins.answer = serializer.validated_data.get('answer')
                ins.save()
                return Response({'msg':'Record save Successfully', 'data':serializer.data,'status':status.HTTP_200_OK})
            serializer.save()
            return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})
        return Response({'data':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})

