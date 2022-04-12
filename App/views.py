from django.shortcuts import render
# New imports
from django.http import HttpResponseRedirect  # Redirect the page after submit
from django.contrib import messages  # Return messages
from django.core.mail import EmailMultiAlternatives  # Requered to send emails
from django.template import loader  # Render templates on email body
from App.models import Registered_email, Support, Message  # Informations in models.py
# Login required to access private pages
from django.contrib.auth.decorators import login_required
# Destry section after logout
from django.views.decorators.cache import cache_control

# ========== FRONTEND SECTION ==========
# Function to render home page
def home(request):
    return render(request, "home.html")

# Function to render opportunities page
def opportunities(request):
    return render(request, "opportunities.html")

# Function to render FAQ page
def faq(request):
    return render(request, "faq.html")

# Support
def support(request):
    if request.method == "POST":

        #Check if email exists
        email = request.POST['email']

        if Support.objects.filter(email = email).exists():
            messages.info(request, "You already have a request in progress !")
            return HttpResponseRedirect('/support')
        else:
            support = Support()

            message = request.POST.get('message')
            terms = request.POST.get('terms')
            person = request.POST.get('person')
            option = request.POST.get('option')
            email = request.POST.get('email')
            
            support.message = message
            support.terms = terms
            support.person = person
            support.option = option
            support.email = email

            support.save()
            messages.success(request, 'We will review your request !')
            return HttpResponseRedirect('/')
    else:
        return render(request, "support.html")
    
# MESSAGE
def add_message(request):
    if request.method == "POST":
        if request.POST.get("message"):
            message = Message()
            message.text = request.POST.get("message")
            message.save()
            messages.success(request, 'Message sent successfully!')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'home.html')
            

# ========== RESUMES ==========

# Function to send frontend form

def email_frontend(request):
    if request.method == "POST":

        # Check if email exist in DB
        email = request.POST['email']

        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume in our DB!")
            return HttpResponseRedirect("/opportunities")
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template('resume_form.txt')
            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'skills': skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Frontend - Candidate", message,
                "Frontend Opportunity",
                ['bestofdjango@gmail.com', ]
            )
            email.content_subtype = 'html'
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'Frontend resume sent successfully!')
            return HttpResponseRedirect('/')

# Function to send backend form


def email_backend(request):

    # Check if email exist in DB
    email = request.POST['email']

    if Registered_email.objects.filter(email=email).exists():
        messages.error(request, "We already have your resume in our DB!")
        return HttpResponseRedirect("/opportunities")
    else:
        if request.method == "POST":
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template('resume_form.txt')
            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'skills': skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Backend - Candidate", message,
                "Backend Opportunity",
                ['bestofdjango@gmail.com', ]
            )
            email.content_subtype = 'html'
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'Backend resume sent successfully!')
            return HttpResponseRedirect('/')

# Function to send fullstack form


def email_fullstack(request):

    # Check if email exist in DB
    email = request.POST['email']

    if Registered_email.objects.filter(email=email).exists():
        messages.error(request, "We already have your resume in our DB!")
        return HttpResponseRedirect("/opportunities")
    else:
        if request.method == "POST":
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template('resume_form.txt')
            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'skills': skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Fullstack - Candidate", message,
                "Fullstack Opportunity",
                ['bestofdjango@gmail.com', ]
            )
            email.content_subtype = 'html'
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'Fullstack resume sent successfully!')
            return HttpResponseRedirect('/')

# =================== BACKEND SECTION ===================

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")
