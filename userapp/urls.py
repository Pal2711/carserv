from django.contrib import admin
from django.urls import path, include
from userapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('team/',views.team,name="team"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path("logout/", views.userlogout, name="logout"),
    path('signup/',views.signup,name="signup"),
    path('error/',views.error,name="error"), 
    path('booking/<int:id>/', views.booking, name="booking"),
    path('success/', views.success, name="success"),
    path('services/', views.service_list, name="services"),

]
