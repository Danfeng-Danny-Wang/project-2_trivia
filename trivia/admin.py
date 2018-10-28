from django.contrib import admin

from trivia.models import Category, Question, Choice


class QuestionInline(admin.TabularInline):
	model = Question
	extra = 7


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4


class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']
	inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
	fields = ['question_text']
	inlines = [ChoiceInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)