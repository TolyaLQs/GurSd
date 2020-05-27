from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
import django.forms as forms
from user.models import User


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class MyUserChangeAvatarForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''