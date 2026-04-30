from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

    @property
    def status(self):
        now = timezone.now()
        if now < self.start_time:
            return "UPCOMING"
        elif self.start_time <= now <= self.end_time:
            return "RUNNING"
        else:
            return "FINISHED"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='quiz_questions/', blank=True, null=True)
    
    opt1 = models.CharField(max_length=255)
    opt2 = models.CharField(max_length=255)
    opt3 = models.CharField(max_length=255)
    opt4 = models.CharField(max_length=255)
    
    opt1_img = models.ImageField(upload_to='option_images/', blank=True, null=True)
    opt2_img = models.ImageField(upload_to='option_images/', blank=True, null=True)
    opt3_img = models.ImageField(upload_to='option_images/', blank=True, null=True)
    opt4_img = models.ImageField(upload_to='option_images/', blank=True, null=True)
    
    # 🔥 CHANGE HERE (important)
    correct_option = models.IntegerField(
        choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')],
        null=True,
        blank=True
    )

    marks = models.IntegerField(default=1)

    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]


class Participant(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=20)
    uap_mail = models.EmailField()
    dept = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    roll = models.CharField(max_length=20, null=True, blank=True)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('quiz', 'student_id')
        ordering = ['quiz', '-score']

    def __str__(self):
        return f"{self.student_id} - {self.name}"
