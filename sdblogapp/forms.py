from django import forms
from .models import Post, Category
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User
from django import forms
from django.core.validators import EmailValidator
from .models import NewsletterSubscription
from sdmember.forms import UserChangeForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        



class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'body', 'thumbnail']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PrimeUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_prime_user']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
    
class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        
class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']