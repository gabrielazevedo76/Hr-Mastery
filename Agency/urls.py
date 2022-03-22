from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Path to render homepage
    path('', views.home, name="home"),
    #Path to render opportunities page
    path('opportunities/', views.opportunities, name="opportunities")
]
