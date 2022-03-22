from django.shortcuts import render

# Function to render home page
def home(request):
    return render(request, "home.html")

# Function to render opportunities page
def opportunities(request):
    return render(request, "opportunities.html")
