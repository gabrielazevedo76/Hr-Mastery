from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Path to render homepage
    path('', views.home, name="home"),
    #Path to render opportunities page
    path('opportunities/', views.opportunities, name="opportunities"),

    # ========== SEND EMAIL ==========
    #Path to send frontend form
    path('email_frontend', views.email_frontend, name="email_frontend"),
    #Path to send backend form
    path('email_backend', views.email_backend, name="email_backend"),
    #Path to send fullstack form
    path('email_fullstack', views.email_fullstack, name="email_fullstack"),
]
