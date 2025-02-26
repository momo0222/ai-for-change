# Generated by Django 4.2.13 on 2024-06-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='activities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='awards',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='career_aspirations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='courses_taken',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='cultural_background',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='current_school',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='grade_level',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='household_income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='interest_major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='languages_spoken',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='parent_occupations',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='siblings_information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='special_circumstances',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='time_commitments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='trade_school_preference',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unweighted_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='weekly_availability',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='weighted_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
