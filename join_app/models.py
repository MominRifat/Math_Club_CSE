from django.db import models

class RecruitmentControl(models.Model):
    semester_name = models.CharField(max_length=100, default="Fall 2025")
    is_active = models.BooleanField(default=False)
    deadline = models.CharField(max_length=100, default="26 January, 2026")
    message_if_closed = models.TextField(default="Please wait for Spring 2026 recruitment.")

    def __str__(self):
        return f"Settings for {self.semester_name}"

class MemberApplication(models.Model):
    SEMESTER_CHOICES = [('1-2', '1-2'), ('2-1', '2-1')]
    SECTION_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    current_semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    section = models.CharField(max_length=5, choices=SECTION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    motivation = models.TextField() 
    experience = models.TextField(blank=True, null=True) 
    designing_skills = models.CharField(max_length=255) 
    video_editing = models.CharField(max_length=5) 
    extracurricular = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.registration_number}"