# Generated by Django 4.2.5 on 2024-01-16 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_enrollment_duedate_enrollment_prise_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='Prise',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='membershipplan',
            old_name='prise',
            new_name='price',
        ),
    ]
