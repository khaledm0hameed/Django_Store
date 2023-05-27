from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

    def clean_username(self):
        username = self.cleaned_data['username']
        # Add any additional validation or uniqueness checks for the username field
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        # Add any additional validation or uniqueness checks for the email field
        return email
