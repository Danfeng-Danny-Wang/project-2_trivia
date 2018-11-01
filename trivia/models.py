from django.db import models
from django.urls import reverse, reverse_lazy


class Category(models.Model):
	name = models.CharField(max_length=200)

	# def get_absolute_url(self):
	# 	return reverse('home')

	def __str__(self):
		return self.name


class Question(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	question_text = models.TextField(max_length=200)

	def __str__(self):
		return self.question_text

	def get_absulute_url(self):
		return reverse_lazy('question_page', args=[str(category.name), str(self.id)])


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	is_correct_answer = models.BooleanField()

	def __str__(self):
		return self.choice_text
