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

		# She notices that there are many categories she can choose.
		categories = self.browser.find_elements_by_tag_name('button')
		self.assertTrue(len(categories) >= 1)
		history_button = self.browser.find_element_by_id('history').value
		self.assertEqual('history', history_button.value)

		# She clicks history, and a question shows up. On the side shows: "score: 0".
		sub_header = self.browser.find_element_by_tag_name('h3')
		self.browser.find_element_by_id('History').click()
		question_text = self.browser.find_element_by_tag_name('h3')
		self.assertNotEqual(sub_header, question_text)

		score = self.browser.find_element_by_class_name('score').text
		self.assertEqual(score, '0')
		choices = self.browser.find_elements_by_tag_name('button')
		num_choices = len(choices)
		self.assertEqual(num_choices, 4)

		# She has no idea what that question could possibly mean. So, she chooses a 
		# random answer. Another question pops up, and the score shows 0.
		self.borwser.find_element_by_id('a').click()
		new_question = self.borwser.find_element_by_tag_name('h3')
		self.assertNotEqual(new_question, question_text)

		score = self.browser.find_element_by_class_name('score').text
		self.assertEqual(score, '0')

		# She has no idea again. She chooses a random answer and another question 
		# pops up, but the score becomes 10 now.
		self.borwser.find_element_by_id('b').click()
		new_question2 = self.borwser.find_element_by_tag_name('h3')
		self.assertNotEqual(new_question2, new_question)
		
		score = self.browser.find_element_by_class_name('score').text
		self.assertEqual(score, '10')
