from django.contrib import admin
from .models import Question
from .models import Choice
from .models import Poll

# Register your models here.
class PollsAdmin(admin.ModelAdmin):
    readonly_fields = [('created')]

class SurveyAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Poll, SurveyAdmin)
admin.site.register(Question, PollsAdmin)
admin.site.register(Choice)

