from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MemberApplication, RecruitmentControl
from utils.google_sheet import save_application

def join(request):
    config = RecruitmentControl.objects.last()
    if not config or not config.is_active:
        return render(request, 'join_app/closed.html', {'config': config})
    if request.method == 'POST':
        skills = request.POST.getlist('design_skills')
        other_skill = request.POST.get('other_design')
        if other_skill:
            skills.append(other_skill)
        application = MemberApplication.objects.create(
            full_name=request.POST.get('name'),
            registration_number=request.POST.get('reg_no'),
            email=request.POST.get('email'),
            contact_number=request.POST.get('phone'),
            current_semester=request.POST.get('semester'),
            section=request.POST.get('section'),
            gender=request.POST.get('gender'),
            motivation=request.POST.get('motivation'),
            experience=request.POST.get('experience'),
            designing_skills=", ".join(skills),
            video_editing=request.POST.get('video_edit'),
            extracurricular=request.POST.get('extracurricular'),
        )
        save_application(
            application,
            config.semester_name
        )
        messages.success(request, 'Application submitted successfully!')
        return redirect('join')
    return render(request, 'join_app/join.html', {'config': config})