from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None, editable=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Assuming 'category' is the name of the URL pattern for the category page
        return reverse('category', kwargs={'cat': self.slug})

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     is_prime_user = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.user)

#     @staticmethod
#     def create_profile(sender, **kwargs):
#         if kwargs['created']:
#             Profile.objects.create(user=kwargs['instance'])

# # Automatically create a Profile object for every new User object
# models.signals.post_save.connect(Profile.create_profile, sender=User)

from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     is_prime_user = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.user)

#     @staticmethod
#     def create_profile(sender, **kwargs):
#         if kwargs['created']:
#             Profile.objects.create(user=kwargs['instance'])

#     @staticmethod
#     def delete_user(sender, **kwargs):
#         kwargs['instance'].user.delete()

# # Automatically create a Profile object for every new User object
# models.signals.post_save.connect(Profile.create_profile, sender=User)

# # Automatically delete the associated User object when Profile object is deleted
# models.signals.post_delete.connect(Profile.delete_user, sender=Profile)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     is_prime_user = models.BooleanField(default=False)
#     subscription_start_date = models.DateField(null=True, blank=True)
#     subscription_expiry_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return str(self.user)

#     @staticmethod
#     def create_profile(sender, **kwargs):
#         if kwargs['created']:
#             Profile.objects.create(user=kwargs['instance'])

#     @staticmethod
#     def delete_user(sender, **kwargs):
#         kwargs['instance'].user.delete()

#     def set_subscription_dates(self):
#         if self.is_prime_user:
#             # Set subscription start date to current date
#             self.subscription_start_date = timezone.now().date()
#             # Calculate subscription expiry date as 28 days from start date
#             self.subscription_expiry_date = self.subscription_start_date + timezone.timedelta(days=28)
#         else:
#             # Reset subscription dates if user is not a prime user
#             self.subscription_start_date = None
#             self.subscription_expiry_date = None

#     def is_subscription_active(self):
#         if self.subscription_expiry_date:
#             return self.subscription_expiry_date >= timezone.now().date()
#         return False

# # Automatically create a Profile object for every new User object
# models.signals.post_save.connect(Profile.create_profile, sender=User)

# # Automatically delete the associated User object when Profile object is deleted
# models.signals.post_delete.connect(Profile.delete_user, sender=Profile)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    is_prime_user = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @staticmethod
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            Profile.objects.create(user=kwargs['instance'])

    @staticmethod
    def delete_user(sender, **kwargs):
        instance = kwargs['instance']
        if instance.user:
            instance.user.delete()

    def set_subscription_dates(self):
        if self.is_prime_user:
            # Set subscription start date to current date
            self.subscription_start_date = timezone.now().date()
            # Calculate subscription expiry date as 28 days from start date
            self.subscription_expiry_date = self.subscription_start_date + timezone.timedelta(days=28)
        else:
            # Reset subscription dates if user is not a prime user
            self.subscription_start_date = None
            self.subscription_expiry_date = None

    def is_subscription_active(self):
        if self.subscription_expiry_date:
            return self.subscription_expiry_date >= timezone.now().date()
        return False

# Automatically create a Profile object for every new User object
models.signals.post_save.connect(Profile.create_profile, sender=User)

# Automatically delete the associated User object when Profile object is deleted
models.signals.post_delete.connect(Profile.delete_user, sender=Profile)

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    post_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    body = RichTextField(blank = True, null = True)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("detail-article", kwargs={"cat": self.category.slug, "slug": self.slug})

class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class Notification(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)