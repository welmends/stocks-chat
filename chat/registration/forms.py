from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1"]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields["password2"]
        for fieldname in ["username", "password1"]:
            self.fields[fieldname].help_text = None
