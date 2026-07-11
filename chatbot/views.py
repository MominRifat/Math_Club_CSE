from django.shortcuts import render
from chatbot.gemini import ask_gemini
# Create your views here.
from django.http import HttpResponse
from .context import get_mathclub_context
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from chatbot.gemini import ask_gemini

from .context import get_mathclub_context
mathclub_context = get_mathclub_context()
system_instruction = f"""
I am a official AI Assistant of UAP CSE Math Club.
Made by Momin Ali Rifat
My job is to answer visitors using ONLY the information provided below.

Rules:

1. Never make up information.

2. If the answer is not available in the database, politely say:
"Sorry, I couldn't find that information."

3. Be friendly.

4. Keep answers short unless the user asks for details.

5. If someone asks about recruitment, explain the current recruitment status.

6. If someone asks about events, quizzes, gallery, or team members, answer from the database.

Database:

{mathclub_context}
"""


import json
import urllib.request
import os
import logging
import traceback

logger = logging.getLogger(__name__)

@require_POST
def chatbot(request):

    try:
        data = json.loads(request.body)

        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse(
                {
                    "error": "Empty message"
                },
                status=400
            )

        context = get_mathclub_context()

        prompt = f"""
You are the Official AI Assistant of UAP CSE Math Club.

Answer ONLY from the information below.

Rules:

- Never make up information.
- Never guess.
- If the answer is unavailable say:
Sorry, I couldn't find that information.
- Be friendly.
- Keep answers short.

Database:

{context}

User Question:

{user_message}
"""

        reply = ask_gemini(prompt)

        return JsonResponse({
            "reply": reply
        })

    except Exception as e:

        print(e)

        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )