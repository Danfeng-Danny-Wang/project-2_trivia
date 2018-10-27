from django.test import TestCase
from django.urls import resolve, reverse

from trivia.views import home_page


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'trivia/home.html')

