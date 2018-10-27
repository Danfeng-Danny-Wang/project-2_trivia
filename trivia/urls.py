from django.urls import path

from trivia import views


app_name = 'trivia'

urlpatterns = [
	path('', views.home_page, name='home'),
]