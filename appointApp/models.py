
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(user.username)


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()

#https://www.jmu.edu/esol/specialist_list.htm
#Cardiologist - treats heart disease
#Allergist or Immunologist - conducts the diagnosis and treatment of allergic conditions.
#Psychiatrist - treats patients with mental and emotional disorders.
#Pediatrician - treats infants, toddlers, children and teenagers.

USER_TYPE = (('DOCTOR', 'DOCTOR'),  ('PATIENT', 'PATIENT'),
                         ('RECEPTIONIST', 'RECEPTIONIST'))

USER_SPECIALISED = (('PSYCHIATRIST', 'PSYCHIATRIST'), ('ALLERGIST', 'ALLERGIST'),
                    ('CARDIOLOGIST', 'CARDIOLOGIST'),('PEDIATRICIAN','PEDIATRICIAN'))

USER_GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))

'''


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_fullname = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPE, null=True, blank=True)
    #user_address = models.CharField(max_length=155, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #user_specialised = models.CharField(max_length=15, choices=USER_SPECIALISED, blank=True, null=True)
    #user_sex = models.CharField(max_length=10, choices=USER_GENDER)
    #user_qualification = models.CharField(max_length=100, blank=True, null=True)
    #user_phone = models.CharField(max_length=20, blank=True, null=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return str(user.username)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class Patient(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)
	bloodgroup = models.CharField(max_length=10, blank=True, null=True)
	sex = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
	age = models.IntegerField(blank=True, null=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)
	def __str__(self):
		return str(self.name)

class Treatment(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treat_doctor')
	title = models.CharField(max_length=50)
	token = models.IntegerField()
	description = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)
	def __str__(self):
		return str(self.patient)

class Appoiment(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='app_doctor')
	token = models.IntegerField()
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(null=True, blank=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)

	def __str__(self):
		return str(self.patient.username)

	class Meta:
		ordering = ['date']

class Prescription(models.Model):
	date = models.DateField(auto_now=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bill_doctor')
	treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    #prescribed_item = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return str(self.patient)
'''
