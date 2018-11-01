from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from trivia.models import Category, Question, Choice


class HomeListView(ListView):
	model = Category
	template_name = 'home.html'

class QuestionDetailView(DetailView):
	model = Question
	template_name = 'question.html'


def check_answer(request, category_name, pk):
	question = get_object_or_404(Question, pk=pk)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'question.html', {
			'question': question,
			'error_message': "You did not select a choice...",
		})
	else:
		return HttpResponseRedirect(reverse('trivia:question_page', args=(category_name, pk+1,)))