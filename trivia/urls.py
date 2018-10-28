from django.urls import path

from trivia import views


app_name = 'trivia'

urlpatterns = [
	path('', views.home_page, name='home'),
	path('<str:name>/<int:question_id>/', views.question_page, name='question'),
	path('<str:name>/<int:question_id>/answer/', views.answer, name='answer'),
]