# Generated by Django 5.0.1 on 2024-03-05 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdmember', '0006_alter_otp_email_expiry_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='email_expiry_time',
            new_name='expiry_time',
        ),
        migrations.RenameField(
            model_name='otp',
            old_name='email_otp',
            new_name='otp',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='phone_expiry_time',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='phone_otp',
        ),
    ]
