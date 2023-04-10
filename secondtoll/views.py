from rest_framework.views import APIView
from rest_framework import status
from .serializers import QuestionSerializer
from .models import QuestionOption, Question
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

