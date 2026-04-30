from django.contrib import admin
from .models import MemberApplication, RecruitmentControl

@admin.register(RecruitmentControl)
class RecruitmentControlAdmin(admin.ModelAdmin):
    list_display = ('semester_name', 'is_active', 'deadline')
    list_editable = ('is_active',) 

@admin.register(MemberApplication)
class MemberApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'registration_number', 'current_semester', 'section', 'applied_at')
    
    list_filter = ('current_semester', 'section', 'gender', 'video_editing', 'applied_at')

    search_fields = ('full_name', 'registration_number', 'email', 'contact_number')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'registration_number', 'gender', 'email', 'contact_number')
        }),
        ('Academic Details', {
            'fields': ('current_semester', 'section')
        }),
        ('Technical Skills', {
            'fields': ('designing_skills', 'video_editing')
        }),
        ('Application Content', {
            'fields': ('motivation', 'experience', 'extracurricular')
        }),
    )
    readonly_fields = ('applied_at',)