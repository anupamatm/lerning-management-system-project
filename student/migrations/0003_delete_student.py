# Generated by Django 5.0.6 on 2024-05-22 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_course_completed_student_date_of_joining_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]