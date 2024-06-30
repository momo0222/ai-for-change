# Generated by Django 4.2.13 on 2024-06-30 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('unweighted_gpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weighted_gpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sat_score', models.IntegerField(blank=True, null=True)),
                ('act_score', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('current_school', models.CharField(max_length=100)),
                ('grade_level', models.CharField(max_length=10)),
                ('courses_taken', models.TextField()),
                ('activities', models.TextField()),
                ('awards', models.TextField()),
                ('household_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parent_occupations', models.CharField(max_length=255)),
                ('siblings_information', models.TextField()),
                ('interest_major', models.CharField(max_length=100)),
                ('trade_school_preference', models.CharField(max_length=100)),
                ('career_aspirations', models.TextField()),
                ('weekly_availability', models.TextField()),
                ('time_commitments', models.TextField()),
                ('special_circumstances', models.TextField()),
                ('languages_spoken', models.CharField(max_length=100)),
                ('cultural_background', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
