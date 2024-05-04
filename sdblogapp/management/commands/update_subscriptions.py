# In your management/commands directory, create a new Python file, e.g., update_subscriptions.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from sdblogapp.models import Profile

class Command(BaseCommand):
    help = 'Check for expired subscriptions and update user status'

    def handle(self, *args, **kwargs):
        # Get current date
        current_date = timezone.now().date()
        
        # Query profiles with expired subscriptions
        expired_profiles = Profile.objects.filter(
            subscription_expiry_date__lt=current_date,
            is_prime_user=True
        )
        
        # Update user status for expired profiles
        for profile in expired_profiles:
            profile.is_prime_user = False
            profile.save()
            
        self.stdout.write(self.style.SUCCESS('User statuses updated successfully'))
