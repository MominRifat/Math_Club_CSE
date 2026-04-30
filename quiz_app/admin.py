from django.contrib import admin
from .models import Quiz, Question, Participant

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    # Admin layout-e options ebong tader image gulo pashapashi sajano
    fieldsets = (
        (None, {
            'fields': ('text', 'image')
        }),
        ('Option 1', {'fields': (('opt1', 'opt1_img'),)}),
        ('Option 2', {'fields': (('opt2', 'opt2_img'),)}),
        ('Option 3', {'fields': (('opt3', 'opt3_img'),)}),
        ('Option 4', {'fields': (('opt4', 'opt4_img'),)}),
        ('Correct Answer', {
            'fields': ('correct_option', 'marks'),
        }),
    )

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'start_time', 'end_time', 'is_published')
    inlines = [QuestionInline]
    list_filter = ('is_published',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'dept', 'roll', 'quiz', 'score', 'submitted_at')
    list_filter = ('quiz', 'dept')
    ordering = ('quiz', '-score')
    search_fields = ('student_id', 'name')