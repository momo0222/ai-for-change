# profiles/forms.py

from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email',
                  'unweighted_gpa', 'weighted_gpa', 'sat_score', 'act_score',
                  'address', 'city', 'state', 'zipcode', 'current_school', 'grade_level', 'courses_taken',
                  'activities', 'awards', 'household_income', 'parent_occupations', 'siblings_information',
                  'interest_major', 'trade_school_preference', 'career_aspirations', 'weekly_availability',
                  'time_commitments', 'special_circumstances', 'languages_spoken', 'cultural_background']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set all fields as optional
        for field_name, field in self.fields.items():
            field.required = False
