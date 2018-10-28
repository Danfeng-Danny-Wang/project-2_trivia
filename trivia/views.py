from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from trivia.models import Category


def home_page(request):
	categories = Category.objects.all()
	return render(request, 'trivia/home.html', {'categories': categories})

def question_page(request):
	return render(request, 'trivia/question.html')

def answer(request):
	return render(request, 'trivia/question.html')