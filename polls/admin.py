from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']    # 빌드 순서 변경

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

admin.site.register(Question, )