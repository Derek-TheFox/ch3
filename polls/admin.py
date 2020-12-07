from django.contrib import admin
from polls.models import Question, Choice
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']    # 필드순서 변경

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement',  {'fields': ['question_text']}),
        ('Date Information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields':['question_text']}),
        ('Date information',    {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]   # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)