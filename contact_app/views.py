from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage # Model import korun

def contact(request):
    if request.method == 'POST':
        # Form theke data gulo niche
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
            messages.success(request, 'Thank you! Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, 'Something went wrong. Please try again.')
            
        return redirect('contact')
        
    return render(request, 'contact_app/contact.html')