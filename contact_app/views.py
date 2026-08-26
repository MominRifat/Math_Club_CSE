from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage 
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_body
            )
            send_mail(
                subject=f"New Contact Message: {subject}",

                message=f"""
            New Contact Message

            Name: {name}

            Email: {email}

            Subject:
            {subject}

            Message:

            {message_body}
            """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[settings.EMAIL_HOST_USER],

                fail_silently=False,
            )
            send_mail(

                subject="Thank you for contacting UAP CSE Math Club",

                message=f"""
            Hello {name},

            Thank you for contacting UAP CSE Math Club.

            We have received your message successfully.

            Our team will review your message and get back to you as soon as possible.

            Regards,
            UAP CSE Math Club
            """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[email],

                fail_silently=False,
                

            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, 'Something went wrong. Please try again.')
            
        return redirect('contact')
        
    return render(request, 'contact_app/contact.html')