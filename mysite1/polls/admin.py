from django.contrib import admin

from .models import Choice, Question


class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ['question']


admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None, {'fields': ['question_text', 'question_text_long']}),
        ('Int information', {'fields': ['views']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('id', 'question_text', 'pub_date')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
