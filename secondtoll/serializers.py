from rest_framework import serializers
from .models import Question, QuestionOption, UserAnswer


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionOption
        fields=['id','answer_test']

class QuestionSerializer(serializers.ModelSerializer):
    question_answers=QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        fields=['id','question_text','can_skip','can_multiple_choice','question_answers']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAnswer
        fields=['id','user','question','answer']