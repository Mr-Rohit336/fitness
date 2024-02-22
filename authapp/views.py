from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authapp.models import Contact, MembershipPlan, Trainer, Enrollment, Gellery, Attendance, Otp
from .utils import send_mail_to_client

import random

# Create your views here.-
def Home(request):
    trainer_count=Trainer.objects.count()
    user_count=Enrollment.objects.count()
    return render(request,"index.html", {'user_count':user_count , 'trainer_count':trainer_count}) 
    
def gallery(request):
    posts=Gellery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html", context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try  Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request, "Attendace Applied Success")
        return redirect('/attendance')
    
    return render(request,"attendance.html", context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try  Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html", context,)

 
def signup(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1') 
        pass2 = request.POST.get('pass2') 

        if len(username) != 10:
            messages.info(request, "Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1 != pass2:
            messages.info(request, "Passwords do not match")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Phone Number is Taken")
                return redirect('/signup')
        except User.DoesNotExist:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')
        except User.DoesNotExist:
            pass
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = pass1  
        
        # Generate OTP and store it in the database
        otp_code = str(random.randint(1000, 9999))
        otp_object = Otp.objects.create(otp=otp_code)

        # Redirect to OTP verification page
        return redirect("/sendemail")

    return render(request, "signup.html")


def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
        
    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')

def contact(request):  
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

def enroll(request, plan_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try Again")
        return redirect('/login')

    # Retrieve the plan based on the plan_id
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    SelectTrainer = Trainer.objects.all()

    if request.method == "POST":
        FullName = request.POST.get('FullName')
        email = request.POST.get('email')
        PhoneNumber = request.POST.get('PhoneNumber')
        gender = request.POST.get('gender')
        DOB = request.POST.get('DOB')
        trainer = request.POST.get('trainer')
        address = request.POST.get('address')
        
        # Create Enrollment instance
        query = Enrollment(FullName=FullName, Email=email, PhoneNumber=PhoneNumber, Gender=gender, DOB=DOB,
                           SelectTrainer=trainer, Address=address)
        query.save()
        messages.info(request, "Thanks For Enrollment")
        return redirect('/payment/' + str(plan_id))  # Redirect to payment page with plan_id
    else:
        context = {"SelectTrainer": SelectTrainer, "plan_id": plan_id}
        return render(request, "enroll.html", context)


# def enroll(request):
#     if not request.user.is_authenticated:
#         messages.warning(request, "Please Login And Try  Again")
#         return redirect('/login')    
#     SelectTrainer=Trainer.objects.all()
#     context={"SelectTrainer":SelectTrainer}
#     if request.method=="POST":
#         FullName=request.POST.get('FullName')
#         email=request.POST.get('email')
#         PhoneNumber=request.POST.get('PhoneNumber')
#         gender=request.POST.get('gender')        
#         DOB=request.POST.get('DOB')        
#         trainer=request.POST.get('trainer')        
#         address=request.POST.get('address')
#         query=Enrollment(FullName=FullName, Email=email, PhoneNumber=PhoneNumber, Gender=gender, DOB=DOB, SelectTrainer=trainer,  Address=address)
#         query.save()
#         messages.info(request, "Thanks For Enrollment")
#         return redirect('/payment')        
#     return render(request, "enroll.html",context)

def enrollcounter(request):
    if request.method == 'POST':
        form = enroll(request.POST)
        if form.is_valid():
            enroll=form.save()
            login(request, Enrollment)
            return redirect('/join')
    else:
        form= enroll()   
        return render(request, "enroll.html", {'form':form}) 
    
def otp(request):
    if request.method == 'POST':
        user_input_otp = request.POST.get('otp')        
        otp_data = Otp.objects.latest('id')         
        if otp_data:
            stored_otp = otp_data.otp
            if int(user_input_otp) == stored_otp:  
                username = request.session.get('username') 
                email = request.session.get('email')
                password = request.session.get('password')
  
                myuser = User.objects.create_user(username, email, password)
                myuser.save()
                          
                otp_data.delete()
                
                messages.success(request, "User created successfully. Please login.")
                return redirect('/login')
            else:
                messages.error(request, "Please enter a valid OTP")
        else:
            messages.error(request, "No OTP data found")
        
    return render(request, "otp.html")


def send_email(request):
    send_mail_to_client(request)
    return redirect("/otpverification")


def services(request):
    return render(request, "services.html")

def payment(request, plan_id):
    # Retrieve the plan based on the plan_id
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    # You can pass the plan object to the payment template
    context = {'plan': plan}

    return render(request, "payment.html", context)  

def plans_view(request):
    membership_plans = MembershipPlan.objects.all()
    return render(request, "plans.html", {"membership_plans": membership_plans})

def plans_details_view(request, plan_id): 
    plan = get_object_or_404(MembershipPlan, id=plan_id)
    price = get_object_or_404(MembershipPlan, id=plan_id)
    return render(request, 'plandetails.html', {'plan': plan, 'price':price})