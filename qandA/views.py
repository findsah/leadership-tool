from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.views import View
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Segment, Question, Response


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'base.html')


class SegmentationView(View):
    def get(self, request):
        questions = Question.objects.all()
        return render(request, 'segmentation.html', {'questions': questions})


class SegmentationAPIView(APIView):
    def post(self, request):
        response_data = {}
        responses = request.data
        total_score = 0
        for q_id, answer in responses.items():
            response = Response(question_id=q_id, answer=answer)
            response.save()
            question_score = 0
            for segment in Segment.objects.all():
                intercept = segment.intercept
                coefficients = [getattr(segment, f'question_{i}_score') for i in range(1, 6)]
                answer_value = 0
                if answer == 'SD':
                    answer_value = -2
                elif answer == 'D':
                    answer_value = -1
                elif answer == 'A':
                    answer_value = 1
                elif answer == 'SA':
                    answer_value = 2
                question_score += coefficients.pop(0) + (answer_value * sum(coefficients))
            segment_score = round(intercept + question_score, 2)
            response_data[segment.name] = segment_score
            total_score += segment_score
        response_data['total_score'] = round(total_score, 2)
        return Response(response_data)
