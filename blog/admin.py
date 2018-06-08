from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Choice
from .models import Question



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes':
    ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
'''
admin.site.register(Choice)
admin.site.register(Question)
'''