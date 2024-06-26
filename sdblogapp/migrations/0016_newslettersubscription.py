# Generated by Django 5.0.1 on 2024-02-29 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdblogapp', '0015_contactentry_delete_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
