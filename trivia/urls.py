from django.urls import path

from .views import (
	HomeListView, 
	QuestionDetailView, 
	check_answer,
	ResultPageView,
)


app_name = 'trivia'

urlpatterns = [
	path('', HomeListView.as_view(), name='home'),
	path('<str:category_name>/<int:pk>/', QuestionDetailView.as_view(), name='question_page'),
	path('<str:category_name>/<int:pk>/check/', check_answer, name='check_answer'),
	path('result/', ResultPageView.as_view(), name='result'),
]