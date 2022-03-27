from django.shortcuts import render
# New imports
from django.http import HttpResponseRedirect # Redirect the page after submit
from django.contrib import messages # Return messages
from django.core.mail import EmailMultiAlternatives # Requered to send emails
from django.template import loader # Render templates on email body

# Function to render home page
def home(request):
    return render(request, "home.html")

# Function to render opportunities page
def opportunities(request):
    return render(request, "opportunities.html")

# ========== RESUMES ==========

# Function to send frontend form
def email_frontend(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
    
        template = loader.get_template('resume_form.txt')
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Frontend - Candidate", message,
            "Frontend Opportunity",
            ['bestofdjango@gmail.com',]
        )
        email.content_subtype = 'html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Frontend resume sent successfully!')
        return HttpResponseRedirect('/')

# Function to send backend form
def email_backend(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
    
        template = loader.get_template('resume_form.txt')
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Backend - Candidate", message,
            "Backend Opportunity",
            ['bestofdjango@gmail.com',]
        )
        email.content_subtype = 'html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Backend resume sent successfully!')
        return HttpResponseRedirect('/')

# Function to send fullstack form
def email_fullstack(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
    
        template = loader.get_template('resume_form.txt')
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : address,
            'experience' : experience,
            'skills' : skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Fullstack - Candidate", message,
            "Fullstack Opportunity",
            ['bestofdjango@gmail.com',]
        )
        email.content_subtype = 'html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Fullstack resume sent successfully!')
        return HttpResponseRedirect('/')