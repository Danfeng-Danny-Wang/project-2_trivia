from django.test import TestCase
from django.urls import resolve, reverse

from trivia.views import home_page
from trivia.models import Category, Question


class HomePageTest(TestCase):

	def test_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'trivia/home.html')

	def test_can_create_and_displays_categories(self):
		category1 = Category.objects.create(name='history')
		category2 = Category.objects.create(name='movies')
		category1.save()
		category2.save()
		categories = Category.objects.all()
		self.assertEqual(categories[0].name, 'history')
		self.assertEqual(categories[1].name, 'movies')

		response = self.client.get('/')
		self.assertContains(response, 'history')
		self.assertContains(response, 'movies')


class QuestionModelTest(TestCase):

	def test_question_is_related_to_list(self):
		category = Category.objects.create(name='history')
		question1 = Question(category=category, question_text="What's your name?")
		question2 = Question(category=category, question_text="How are you?")
		question1.save()
		question2.save()
		self.assertIn(question1, category.question_set.all())
		self.assertIn(question2, category.question_set.all())


class CategoryModelTest(TestCase):

	def test_default_category_model(self):
		category = Category()
		self.assertEqual(category.name, '')

	# def test_get_absolute_url(self):
	# 	category = Category.objects.create()
	# 	self.assertEqual(category.get_absolute_url(), f'/{category.name}/')