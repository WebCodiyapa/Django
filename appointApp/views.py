
from django.http import HttpResponseRedirect
from django.views import View

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
#from django.core.urlresolvers import reverse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from appointApp.forms import SignUpForm#, PatientForm, AppoimentForm, TreatmentForm, PrescriptionForm


#@login_required
def home(request):
    return render(request, 'home.html')


# doctor
''''
def dotodaypatient(request):

def dotodaypatientdetails(request):

def dochangepassword(request):

def readdtreatment(request):
'''

# receptionist or Admin
'''
def add_doctor(request):

def retodaybooking(request):

def doctorlist(request):

def patientlist(request):

def rebill(request):

def readdPrescription(request):

def rechangepassword(request):
'''

# patient
'''
def patienthome(request):

def padetails(request):

def readdappoinment(request):

def pachangepassword(request):

def retodaybooking(request):

def writeFeedback(request):
'''


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal UserProfile
            user.userprofile.birth_date = form.cleaned_data.get('birth_date')
            #user.userprofile.user_type = form.cleaned_data.get('user_type')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup_form.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = 	authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            userprofile = UserProfile.objects.get(user=user)
            if userprofile.user_type == 'RECEPTIONIST':
                return HttpResponseRedirect('/home_test/retodaybooking/')
            elif user.UserProfile.user_type == 'DOCTOR':
                return HttpResponseRedirect('/home_test/dotodaypatient/')
            else:
                return HttpResponseRedirect('/home_test/patienthome')
    return render(request, 'login.html')
