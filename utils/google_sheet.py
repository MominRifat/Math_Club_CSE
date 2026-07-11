import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = Credentials.from_service_account_file(
    settings.GOOGLE_CREDENTIAL,
    scopes=SCOPES
)

client = gspread.authorize(credentials)

def get_sheet(sheet_name):
    spreadsheet = client.open("Math Club Recruitment")

    try:
        worksheet = spreadsheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title=sheet_name,
            rows=1000,
            cols=20,
        )

    return worksheet

def save_application(application, semester_name):

    sheet = get_sheet(semester_name)

    if sheet.row_count == 1000 and sheet.cell(1, 1).value is None:
        sheet.append_row([
            "Applied At",
            "Full Name",
            "Registration",
            "Email",
            "Phone",
            "Semester",
            "Section",
            "Gender",
            "Motivation",
            "Experience",
            "Design Skill",
            "Video Editing",
            "Extra Curricular",
        ])

    sheet.append_row([
        application.applied_at.strftime("%d-%m-%Y %I:%M %p"),
        application.full_name,
        application.registration_number,
        application.email,
        application.contact_number,
        application.current_semester,
        application.section,
        application.gender,
        application.motivation,
        application.experience,
        application.designing_skills,
        application.video_editing,
        application.extracurricular,
    ])