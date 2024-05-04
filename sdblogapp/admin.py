from django.contrib import admin
from .models import Post, Category, Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_prime_user', 'subscription_start_date', 'subscription_expiry_date')
    list_filter = ('is_prime_user',)
    search_fields = ('user__username', 'user__email')
    actions = ['make_prime', 'end_membership']

    def make_prime(self, request, queryset):
        queryset.update(is_prime_user=True)
    make_prime.short_description = "Make selected users prime members"

    def end_membership(self, request, queryset):
        queryset.update(is_prime_user=False, subscription_start_date=None, subscription_expiry_date=None)
    end_membership.short_description = "End membership for selected users"

admin.site.register(Profile, ProfileAdmin)

