# Generated by Django 4.2.5 on 2024-02-22 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_membershipplan_img_membershipplan_plandetals_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membershipplan',
            old_name='plandetals',
            new_name='plandetails',
        ),
    ]
