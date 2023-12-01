from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta: #わあああああああああああああああああああああああああああああああああああああああああ（怒）
        model =CustomUser
    
        fields = ('username', 'email', 'password1', 'password2')
