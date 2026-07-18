from events_app.models import Event
from gallery_app.models import GalleryItem
from team_app.models import TeamMember
from quiz_app.models import Quiz
from join_app.models import RecruitmentControl
from home_app.models import Convenor

def get_mathclub_context():

    context = []

    # =========================
    # Developer Info (static)
    # =========================

    context.append("""
================ DEVELOPER INFO ================

Developed by:
Momin Ali Rifat

Education:
B.Sc. in Computer Science & Engineering (CSE), University of Asia Pacific (UAP), Bangladesh

Portfolio:
https://mominrifat8.onrender.com

GitHub:
https://github.com/MominRifat

Facebook:
https://facebook.com/mominrifat8

Codeforces:
https://codeforces.com/profile/Momin_Rifat

""")
    
    # =========================
    # Convenor
    # =========================

    convenor = Convenor.objects.first()

    if convenor:

        context.append(f"""

================ CONVENOR ================

Name:
{convenor.name}

Designation:
{convenor.designation}

Organization:
{convenor.organization}

""")

    # =========================
    # Recruitment
    # =========================

    recruitment = RecruitmentControl.objects.last()

    if recruitment:

        status = "OPEN" if recruitment.is_active else "CLOSED"

        context.append(f"""
================ RECRUITMENT ================

Current Semester:
{recruitment.semester_name}

Recruitment Status:
{status}

Application Deadline:
{recruitment.deadline}

If Closed:
{recruitment.message_if_closed}

""")

    # =========================
    # Events
    # =========================

    events = Event.objects.filter(
        is_published=True
    ).order_by("-start_registration")[:5]

    if events.exists():

        event_list = []

        for event in events:

            event_list.append(f"""

Title:
{event.title}

Type:
{event.get_event_type_display()}

Description:
{event.description}

Registration Starts:
{event.start_registration}

Registration Ends:
{event.end_registration}

Registration Link:
{event.form_url}

Current Status:
{event.get_status()}

""")

        context.append(
            "================ EVENTS ================\n"
            + "\n".join(event_list)
        )

    # =========================
    # Quiz
    # =========================

    quizzes = Quiz.objects.filter(
        is_published=True
    ).order_by("-start_time")[:5]

    if quizzes.exists():

        quiz_list = []

        for quiz in quizzes:

            participant = quiz.participant_set.count()

            context.append(f"""
================ QUIZ ================

Title:
{quiz.title}

Description:
{quiz.description}

Start Time:
{quiz.start_time}

End Time:
{quiz.end_time}

Status:
{quiz.status}

Participants:
{participant}

""")

    # =========================
    # Team
    # =========================

    members = TeamMember.objects.filter(
        is_active=True
    )

    if members.exists():

        member_list = []

        for member in members:

            member_list.append(f"""

Name:
{member.name}

Designation:
{member.designation}

Facebook:
{member.facebook or "N/A"}

GitHub:
{member.github or "N/A"}

Email:
{member.email or "N/A"}

""")

        context.append(
            "================ TEAM MEMBERS ================\n"
            + "\n".join(member_list)
        )

    # =========================
    # Former Presidents
    # =========================

    presidents = TeamMember.objects.filter(
        is_former_president=True
    )

    if presidents.exists():

        president_list = []

        for president in presidents:

            president_list.append(
                f"{president.name} ({president.tenure_year})"
            )

        context.append(
            "FORMER PRESIDENTS:\n"
            + "\n".join(president_list)
        )

    # =========================
    # Gallery
    # =========================

    total_images = GalleryItem.objects.count()

    categories = GalleryItem.objects.values_list(
        "category",
        flat=True
    ).distinct()

    context.append(f"""
================ GALLERY ================

Total Images:
{total_images}

Categories:
{", ".join(categories)}

""")

    return "\n\n".join(context)