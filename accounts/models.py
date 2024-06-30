

from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   # Basic Information
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)

    # Contact Information
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Academic Performance
    unweighted_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    weighted_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sat_score = models.IntegerField(blank=True, null=True)
    act_score = models.IntegerField(blank=True, null=True)

    # Address
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    # School and Educational Background
    current_school = models.CharField(max_length=100, blank=True, null=True)
    grade_level = models.CharField(max_length=10, blank=True, null=True)
    courses_taken = models.TextField(blank=True, null=True)

    # Extracurricular Activities
    activities = models.TextField(blank=True, null=True)

    # Achievements and Awards
    awards = models.TextField(blank=True, null=True)

    # Family Information
    household_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    parent_occupations = models.CharField(max_length=255, blank=True, null=True)
    siblings_information = models.TextField(blank=True, null=True)

    # Career Interests
    interest_major = models.CharField(max_length=100, blank=True, null=True)
    trade_school_preference = models.CharField(max_length=100, blank=True, null=True)
    career_aspirations = models.TextField(blank=True, null=True)

    # Availability and Schedule
    weekly_availability = models.TextField(blank=True, null=True)
    time_commitments = models.TextField(blank=True, null=True)

    # Additional Information
    special_circumstances = models.TextField(blank=True, null=True)
    languages_spoken = models.CharField(max_length=100, blank=True, null=True)
    cultural_background = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
