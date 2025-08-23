# views.py
from django.shortcuts import render, redirect, HttpResponse
from CodingIndiaErp.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# For email
from django.core.mail import send_mail
import random
from CodingIndiaErp.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import CreateUserForm
import random


def SignUpView(request):
    form = CreateUserForm()
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')  

        form = CreateUserForm(request.POST)

        if form.is_valid():
            otp = random.randint(100000, 999999)
            send_mail(
                subject="Verify your account",
                message=f"Your OTP is {otp}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )
            
            # Store user data and OTP in session
            request.session['otp'] = str(otp)
            request.session['pending_user'] = {
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'password1': password1,
                'password2': password2
            }

            return render(request, 'verify.html', {'otp': otp})
        else:
            messages.error(request, form.errors)

    return render(request, 'signup.html', {"form": form})


@csrf_exempt
def verifyOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if userotp == session_otp:
            user_data = request.session.get('pending_user')
            if user_data:
                if user_data['password1'] == user_data['password2']:
                    User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name'],
                        password=user_data['password1']
                    )
                    return JsonResponse({'message': 'User created successfully!'}, status=200)
                else:
                    return JsonResponse({'error': 'Passwords do not match'}, status=400)
            else:
                return JsonResponse({'error': 'User session expired'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid OTP'}, status=400)



# For login
@csrf_exempt
def verifyLoginOTP(request):
    if request.method == "POST":
        # print("Incoming POST data:", request.POST)
        userotp = request.POST.get('otp')
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("LOGIN DONE!!")

        print("OTP: ", userotp)
    return JsonResponse({'data':'Hello'}, status=200)
def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = User.objects.get(username=username).email
        
        print("username:", username)
        print("password:",password)
        print("email:", email)

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
            
        #     login(request, user)
        #     print("Login saved")
        #     messages.success(request, "Login Successfully !!")

        #     return redirect("/")
        # else:
        #     print("Some Error")
        otp = random.randint(100000,999999)
        send_mail(subject="User Data",message=f"Verify your LoginMail by opt : {otp}",from_email=EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
        messages.success(request, "User Saved Successfully !!")
        return render(request,'verifyloginotp.html',{'otp':otp, 'username':username, 'password':password})
        #     messages.error(request, "Invalid Details !!")

        


        
    context = {}
    return render(request, 'login.html', context)


def LogOut(request):
    logout(request)
    print("LogOut Successfully")
    messages.success(request, "Logout Successfully !!")


    return redirect("loginview")




#For Forget the password

def ForgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        print("Email : ", email)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("User Exit")
            send_mail(subject="Reset Your Password ",message=f"Hey user  : {user} if You want to reset your password then click on this link \n http://127.0.0.1:8000/newpasswordpage/{user}/",from_email=EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
            return HttpResponse("Reset Password Link send to Your Email")
        return render(request, 'forget_password.html')
    return render(request, 'forget_password.html')



def NewPassword(request, user):
    userId = User.objects.get(username=user)
    print("UserId : ", userId)
    if request.method == "POST":
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        print("Pass1 and Pass2 : ", pass1, pass2)
        if pass1 == pass2:
            userId.set_password(pass1)
            userId.save()
            return HttpResponse("Password Reset")
    return render(request, 'new_password.html')

