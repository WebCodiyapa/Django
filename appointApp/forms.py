from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import UserProfile

from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile
#Patient, Appoiment, Treatment, Prescription,

#USER_TYPE = (('DOCTOR', 'DOCTOR'),  ('PATIENT', 'PATIENT'), ('RECEPTIONIST', 'RECEPTIONIST'))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


'''class SignUpForm(UserCreationForm):
    USER_TYPE = (('DOCTOR', 'DOCTOR'),
                ('PATIENT', 'PATIENT'))
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    user_type = forms.MultipleChoiceField(choices=USER_TYPE,  widget=forms.RadioSelect())


'''



'''def get_my_choices():
        USER_TYPE = (('DOCTOR', 'DOCTOR'),  ('PATIENT', 'PATIENT'), ('RECEPTIONIST', 'RECEPTIONIST'))
        return USER_TYPE

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['user_type'] = forms.ChoiceField(choices=get_my_choices())



class DoctorForm(ModelForm):
	class Meta:
		model = User
		fields = ('user_name', 'user_sex', 'user_address', 'user_specialised', 'user_phone', 'user_qualification')

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = ('name', 'email', 'phone', 'address', 'bloodgroup', 'sex', 'age')

class AppoimentForm(ModelForm):
	class Meta:
		model = Appoiment
		fields = ('patient', 'doctor', 'token', 'date', 'time')

class TreatmentForm(ModelForm):
	class Meta:
		model = Treatment
		fields = ('patient', 'doctor', 'title', 'token', 'description')

class PrescriptionForm(ModelForm):
	class Meta:
		model = Prescription
		fields = ( 'patient', 'doctor', 'treatment')
'''
