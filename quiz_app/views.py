from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Participant
from django.db import IntegrityError

def quiz_list(request):
    quizzes = Quiz.objects.filter(is_published=True).order_by('-start_time')
    return render(request, 'quiz_app/quiz.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if quiz.status != "RUNNING":
        return HttpResponse("<h2 style='text-align:center; margin-top:100px;'>This quiz is not active.</h2>")

    if request.method == "POST":
        sid = request.POST.get('student_id')
        score = 0
        for q in quiz.questions.all():
            ans = request.POST.get(f'q_{q.id}')
            if ans and int(ans) == q.correct_option:
                score += q.marks
        
        try:
            Participant.objects.create(
                quiz=quiz,
                name=request.POST.get('name'),
                student_id=sid,
                uap_mail=request.POST.get('uap_mail'),
                dept=request.POST.get('dept'),
                semester=request.POST.get('semester'),
                section=request.POST.get('section'),
                roll=request.POST.get('roll'),
                score=score
            )
            return render(request, 'quiz_app/quiz_success.html', {'quiz': quiz})
            
        except IntegrityError:
            return HttpResponse(f"""
                <div style="text-align:center; padding-top:100px; font-family:sans-serif;">
                    <h1 style="color:#e11d48;">Submission Denied!</h1>
                    <p>You have already submitted this quiz.</p>
                    <a href='/quiz/'>Back to Portal</a>
                </div>
            """)

    return render(request, 'quiz_app/take_quiz.html', {'quiz': quiz})