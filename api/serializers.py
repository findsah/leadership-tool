from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model=Question
    fields=['id','question_text']
    

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAnswer
        fields='__all__'
    def validate(self, data):
        if data['user_id'] < 1:
            raise serializers.ValidationError('Value should be grater than 0')
        if not User.objects.filter(pk=data['user_id']).exists():
            raise serializers.ValidationError('User Id does not exist. Please provide a valid user ID')
        return data

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# LeadershipType Serializer
class LeadershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipType
        fields = ['name','description','get_image'] 


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
    
 