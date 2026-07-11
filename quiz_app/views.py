from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Participant
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Quiz, Participant

def quiz_list(request):
    quizzes = Quiz.objects.filter(is_published=True).order_by('-start_time')

    paginator = Paginator(quizzes, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'quiz_app/quiz.html', {
        'quizzes': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if quiz.status != "RUNNING":
        return HttpResponse("<h2 style='text-align:center; margin-top:100px;'>This quiz is not active.</h2>")

    if request.method == "POST":
        # return HttpResponse(
        #     f"""
        #     POST DATA: {request.POST}<br>
        #     Dept: {request.POST.get('dept')}<br>
        #     Semester: {request.POST.get('semester')}
        #     """
        # )
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
            return HttpResponse("""
                <html>
                <head>
                    <style>
                        body {
                            margin: 0;
                            min-height: 100vh;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            background: #0f172a;
                            font-family: 'Inter', -apple-system, sans-serif;
                        }

                        .denied-card {
                            background: transparent;
                            padding: 45px 40px;
                            border-radius: 24px;

                            border: 1px solid rgba(239, 68, 68, 0.25);

                            backdrop-filter: blur(16px);
                            -webkit-backdrop-filter: blur(16px);

                            box-shadow:
                                inset 0 1px 0 rgba(255, 255, 255, 0.04),
                                0 20px 50px rgba(2, 6, 23, 0.4),
                                0 0 30px rgba(239, 68, 68, 0.12);

                            max-width: 460px;
                            width: 90%;
                            text-align: center;

                            position: relative;
                            overflow: hidden;
                        }

                        .denied-card::before {
                            content: "";
                            position: absolute;
                            inset: 0;
                            background: radial-gradient(circle at top,
                                rgba(239, 68, 68, 0.12) 0%,
                                rgba(37, 99, 235, 0.05) 40%,
                                transparent 70%);
                            pointer-events: none;
                        }

                        .denied-card > * {
                            position: relative;
                            z-index: 1;
                        }

                        .denied-icon {
                            width: 64px;
                            height: 64px;

                            background: rgba(239, 68, 68, 0.12);
                            color: #f87171;
                            border: 1px solid rgba(239, 68, 68, 0.35);

                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0 auto 22px;
                            font-size: 28px;
                            font-weight: 800;

                            backdrop-filter: blur(10px);
                            box-shadow: 0 0 22px rgba(239, 68, 68, 0.25);
                        }

                        .denied-title {
                            font-size: 1.6rem;
                            margin-bottom: 10px;
                            font-weight: 800;

                            background: linear-gradient(to right, #f87171, #f472b6);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;
                            background-clip: text;
                        }

                        .denied-text {
                            color: #94a3b8;
                            font-size: 14px;
                            line-height: 1.6;
                            margin-bottom: 0;
                        }

                        .back-btn {
                            display: inline-block;
                            margin-top: 26px;
                            padding: 12px 32px;

                            background: rgba(37, 99, 235, 0.14);
                            color: #dbeafe;

                            border: 1px solid rgba(59, 130, 246, 0.25);
                            border-radius: 12px;

                            text-decoration: none;
                            font-weight: 700;
                            font-size: 14px;

                            backdrop-filter: blur(10px);
                            transition: all 0.3s ease;
                        }

                        .back-btn:hover {
                            background: rgba(37, 99, 235, 0.22);
                            border-color: rgba(96, 165, 250, 0.5);
                            color: #fff;
                            transform: translateY(-2px);
                            box-shadow: 0 0 18px rgba(59, 130, 246, 0.18);
                        }
                    </style>
                </head>
                <body>
                    <div class="denied-card">
                        <div class="denied-icon">&#10005;</div>
                        <h1 class="denied-title">Submission Denied!</h1>
                        <p class="denied-text">You have already submitted this quiz.</p>
                        <a href="/quiz/" class="back-btn">Back to Portal</a>
                    </div>
                </body>
                </html>
            """)

    return render(request, 'quiz_app/take_quiz.html', {'quiz': quiz})


def leaderboard_home(request):
    quizzes = Quiz.objects.annotate(
        participant_count=Count('participant')
    ).order_by('-start_time')

    return render(request, 'quiz_app/leaderboard_list.html', {
        'quizzes': quizzes,
    })


def quiz_leaderboard(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    participants = Participant.objects.filter(quiz=quiz).order_by('-score', 'submitted_at')

    ranked_participants = []
    for idx, p in enumerate(participants, start=1):
        ranked_participants.append({
            'rank': idx,
            'participant': p,
        })

    return render(request, 'quiz_app/leaderboard_detail.html', {
        'quiz': quiz,
        'ranked_participants': ranked_participants,
        'total_participants': participants.count(),
    })


