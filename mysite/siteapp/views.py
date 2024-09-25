from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import UserSubmission

def home(request):
    current_time = datetime.now()
    return render(request, 'index.html',{'time' : current_time})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        UserSubmission.objects.create(name=name, email=email)
        return HttpResponse(f'Thank you, {name}. We have received your email: {email}')

def view_submissions(request):
    submissions = UserSubmission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions}) 
    