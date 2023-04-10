from rest_framework import serializers
from .models import Question, QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionOption
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    question_answers=QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        fields=['id','question_text','question_answers']