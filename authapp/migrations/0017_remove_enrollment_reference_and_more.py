# Generated by Django 4.2.5 on 2024-02-22 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_rename_plandetals_membershipplan_plandetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='Reference',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='SelectMembershipplan',
        ),
    ]