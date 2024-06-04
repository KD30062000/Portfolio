from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.conf import settings
from django.core.mail import send_mail
from .models import Emails

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html')
def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Koushik_Das_Resume.pdf')  # Replace with your file path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("File not found.")
def subscribe(request):
    if request.method=='POST':
        email=request.POST.get('email')
        try:
            g=Emails(email1=email,email2=email)
            g.save()
            print(f"{email} Subscribed Successfully")
        except Exception as e:
            print(f"Failed to save email: {e}")
        subject = 'Test Subject'
        message = 'This is the body of the email'
        from_email = 'kdchrist30@gmail.com'
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
        return redirect('index')
    return redirect('index')
