from django.urls import path
from authapp import views   

 
urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.handlelogin,name="handlelogin"),
    path('logout/',views.handlelogout,name="handlelogout"),
    path('contact/',views.contact,name="contact"),
    path('join/',views.enroll,name="enroll"),    
    path('profile/',views.profile,name="profile"),
    path('gallery/',views.gallery,name="gallery"),
    path('attendance/',views.attendance,name="attendance"),
    path('services/',views.services,name="services"),
    #otp verificatio
    path('otpverification/', views.otp, name="otp_verificat"),
    path('sendemail/', views.send_email, name="send_email"),       
   
   #payment
    path('plans/', views.plans_view, name="membership plans"),
    path('plandetails/', views.plans_details_view, name="membership plans details"),
    path('payment/', views.payment, name="payments"),   
]
 
 
