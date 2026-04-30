from django.shortcuts import render
from .models import TeamMember

def active_team(request):
    members = TeamMember.objects.filter(is_active=True)
    return render(request, 'team_app/team.html', {'members': members})

def former_presidents(request):
    members = TeamMember.objects.filter(is_former_president=True)
    return render(request, 'team_app/team_former.html', {'members': members})
