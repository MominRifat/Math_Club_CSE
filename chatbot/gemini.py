from google import genai
from google.genai import errors as genai_errors

from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

MODEL_NAME = "gemini-flash-latest"  # auto-updating alias to the latest stable Flash model
# Alternatives: "gemini-2.5-flash-lite" (cheapest/fastest), "gemini-3-flash"


def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text

    except genai_errors.ClientError as e:
        # 429 = quota exceeded / rate limited
        if getattr(e, "code", None) == 429 or "RESOURCE_EXHAUSTED" in str(e) or "quota" in str(e).lower():
            return (
                "Sorry, I'm currently experiencing high demand and have hit my "
                "usage limit. Please try again in a minute."
            )
        raise

    except Exception:
        return "Sorry, I'm having trouble responding right now. Please try again shortly."