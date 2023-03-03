from rest_framework import serializers
from .models import Response


class ResponseSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Response
        fields = ['question', 'answer']
