from django.contrib import admin
from django.urls import path, include
from App.models import Support
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ========== FRONTEND SECTION ==========
    # Path to render homepage
    path('', views.home, name="home"),
    # Path to render opportunities page
    path('opportunities/', views.opportunities, name="opportunities"),
    # Path to Login/logout
    path('login/', include('django.contrib.auth.urls')),
    # Path to Support
    path('support/', views.support, name="support"),

    # ========== SEND EMAIL ==========
    # Path to send frontend form
    path('email_frontend', views.email_frontend, name="email_frontend"),
    # Path to send backend form
    path('email_backend', views.email_backend, name="email_backend"),
    # Path to send fullstack form
    path('email_fullstack', views.email_fullstack, name="email_fullstack"),

    # ========== BACKEND SECTION ==========
    path('backend/', views.backend, name="backend"),
]
