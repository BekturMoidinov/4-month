from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50,widget=forms.PasswordInput)
    email = forms.EmailField()
    age= forms.IntegerField()
    avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_confirm = cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

class SMScodeForm(forms.Form):
    code = forms.CharField(max_length=4)