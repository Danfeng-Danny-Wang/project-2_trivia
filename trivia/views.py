from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from trivia.models import Category, Question, Choice


class HomeListView(ListView):

	template_name = 'home.html'
	
	def get_queryset(self):
		self.request.session['score'] = 0
		return Category.objects.all()

class QuestionDetailView(DetailView):

	template_name = 'question.html'

	def get_queryset(self):
		self.category = get_object_or_404(Category, name=self.kwargs['category_name'])
		return Question.objects.filter(category=self.category)


def check_answer(request, category_name, pk):
	question = get_object_or_404(Question, pk=pk)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		if selected_choice.is_correct_answer == True:
			request.session['score'] += 10
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'question.html', {
			'question': question,
			'error_message': "You did not select a choice...",
		})
	else:
		category = get_object_or_404(Category, name=category_name)
		if Question.objects.filter(category=category, pk=pk+1).exists():
			return HttpResponseRedirect(reverse('trivia:question_page', args=(category_name, pk+1,)))
		else:
			return HttpResponseRedirect(reverse('trivia:result'))


class ResultPageView(TemplateView):
	template_name = 'result.html'