from django.core.mail import send_mail
from django.conf import settings
from socket import gaierror
from .models import Otp
from django.contrib.auth.models import User

def send_mail_to_client(request): 
    subject = " One-Time Password for Account Verification"
    # Retrieve the latest OTP from the database
    latest_otp = Otp.objects.latest('id').otp
    message = f"Dear user,\n\nYour one-time password (OTP) for account verification is: {latest_otp}\n\nPlease use this OTP to complete the verification process.\n\nBest regards,\nThe Sigma Gym Team"  
    from_email = settings.EMAIL_HOST_USER
    # Retrieve the email from the session where it was stored during signup
    recipient_email = request.session.get('email')

    if recipient_email:
        recipient_list = [recipient_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            print("Email sent successfully")
        except gaierror as e:
            pass
            # print("hii Error: No address associated with hostname.", e)
    else:
        print("Recipient email not found in session. Email not sent.")
        
def send_mail_for_login(request): 
    subject = " One-Time Password for Account Verification"
    
    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Retrieve the latest OTP from the database
        latest_otp = Otp.objects.latest('id').otp
        
        # Get the username entered during login
        entered_username = request.POST.get('username') 
        print("user name :", entered_username)
        # Retrieve the user object based on the entered username
        try:
            user = User.objects.get(username=entered_username)
            user_email = user.email
            
            message = f"Dear user,\n\nYour one-time password (OTP) for account verification is: {latest_otp}\n\nPlease use this OTP to complete the verification process.\n\nBest regards,\nThe Sigma Gym Team"  
            from_email = settings.EMAIL_HOST_USER
            
            if user_email:
                recipient_list = [user_email]
                print("email  ", user_email)
                try:
                    send_mail(subject, message, from_email, recipient_list)
                    print("Email sent successfully")
                    print("email sent ", user_email)
                except gaierror as e:
                    pass
                    # print("hii Error: No address associated with hostname.", e)
            else:
                print("User email not found. Email not sent.")
        
        except User.DoesNotExist:
            print("User not found. Email not sent.")
    
    else:
        print("Invalid request method. Email not sent.")
      