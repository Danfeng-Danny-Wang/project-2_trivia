from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import time
import os


class NewPlayerTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		# staging_server = os.environ.get('STAGING_SERVER')
		# if staging_server:
		# 	self.live_server_url = 'http://' + staging_server

	def tearDown(self):
		self.browser.quit()

	def test_can_play_the_game_and_count_the_score(self):
		# Stephany has heard about a COOL trivia show website. She goes to check out its homepage.
		self.browser.get('http://localhost:8000')

		# The website's title is TheGreatestTrivia, and Stephany sees the header of the website
		# is The Greatest Trivia Show on Earth!
		self.assertIn('TheGreatestTrivia', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('The Greatest Trivia Show on Earth!', header_text)

		# She notices that there are 4 categories she can choose: history, x2, x3, and x4.
		categories = self.browser.find_elements_by_tag_name('button')
		self.assertEqual(len(categories), 4)
		categories_text = []
		for button in categories:
			categories_text.append(button.value)
		self.assertIn('history', categories_text)
		self.assertIn('x2', categories_text)
		self.assertIn('x3', categories_text)
		self.assertIn('x4', categories_text)

		# On the side shows: "score: 0".
		score = self.browser.find_element_by_class_name('score').text
		self.assertEqual(score, '0')

		# She then choose history. A question pops up, along with 4 choices. The question asks "Which U.S. president 
		# appears on the front of the $2 bill?" 

		# She then chooses "Thomas Jefferson". The question disappears and another question
		# shows up. She notices that the score becomes 10.

		# The new question is "Which Kentucky-born U.S. president is honored in the Wrestling Hall of Fame?"
		# She chooses "Andrew Jackson". The website goes to the next page but the socre does not change.
