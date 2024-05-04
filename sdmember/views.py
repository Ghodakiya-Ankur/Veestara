# sdmember/views.py
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, EditProfileForm
from sdblogapp.models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from sdblog.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse
from django.utils import timezone
from .models import OTP
from django.urls import reverse
from twilio.rest import Client
import os
import random
from django.db import transaction
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.views.decorators.csrf import csrf_exempt



#-----------------------------------------
# For Registering
class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been created successfully. You can now log in."

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        email = self.request.POST.get('email')
        phone = self.request.POST.get('phone_number')

        # Generate random OTP
        otp = str(random.randint(100000, 999999))

        # Store OTP in the database along with user's email and phone number
        expiry_time = timezone.now() + timezone.timedelta(minutes=1)
        OTP.objects.create(user=user, otp=otp, expiry_time=expiry_time)

        # Send OTP via email
        send_mail("User Data:", f"Verify Your Mail by the OTP: {otp}", settings.EMAIL_HOST_USER, [email], fail_silently=True)

        # Send OTP via SMS using Twilio
        send_otp_sms(phone, otp)  # Pass the same OTP for SMS

        messages.success(self.request, 'User saved Successfully')

        # Pass OTP to the verification template for displaying to the user
        return render(self.request, 'registration/verify_otp.html', {'otp': otp})

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check for and delete expired OTPs
        expired_otps = OTP.objects.filter(expiry_time__lt=timezone.now())
        expired_otps.delete()
        return context




# ------------------------------------------------------
# for sending SMS

def send_otp_sms(phone_number, otp):
    # Twilio account credentials
    account_sid = "AC9213a47561dd259923b4e87795145fc7"
    auth_token = "13ab287e94f4647042f995267b3382e3"
    twilio_phone_number = "+12108710951"

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Customizing SMS with OTP message
        message_body = f"Your custom OTP message: {otp}"
        
        # Sending SMS with OTP
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"SMS sent successfully to {phone_number}. SID: {message.sid}")
        return True  # Return True indicating successful SMS delivery
    except Exception as e:
        print(f"Error occurred while sending SMS: {e}")
        return False  # Return False indicating failure to send SMS"
    
# ------------------------------------------------------
# for verifing otp

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_entered = request.POST.get('otp')

        try:
            # Retrieve the OTP entry from the database based on OTP value
            otp_obj = OTP.objects.get(otp=otp_entered)

            # Compare entered OTP with stored OTP
            if otp_obj.otp == otp_entered:
                # Check if 'phone_number' key exists in the session before deleting it
                if 'phone_number' in request.session:
                    del request.session['phone_number']
                otp_obj.delete()

                messages.success(request, 'OTP verified. You are now logged in.')
                return render(request, 'registration/verification_success.html')

            else:
                # Invalid OTP, display error message
                messages.error(request, 'Invalid OTP. Please try again.')
                # return render(request, 'registration/error.html')
                return render(request, 'registration/error.html')

        except OTP.DoesNotExist:
            # OTP entry does not exist or OTP is incorrect, display error message
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'registration/error2.html')

    return render(request, 'registration/verify_otp.html')




#-----------------------------------------
# For Changing Password

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

    

#-----------------------------------------
# For Profile Editing

class UserEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user  # Assuming the user has a profile associated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_prime_user'] = self.request.user.profile.is_prime_user
        return context
    
#-----------------------------------------
# for Logout
    
def logout_view(request):
    logout(request)
    # Redirect to a success page or any other page after logout
    return redirect('landingpage/')


    
    




#-----------------------------------------------
# For Resting Password

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')