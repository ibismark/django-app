from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 表示の順序を指定
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
