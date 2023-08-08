from django import forms
from sql_integration.settings import AUTHENTICATION_OPTIONS

class DatabaseConnectionForm(forms.Form):
    db_engine = forms.ChoiceField(choices=AUTHENTICATION_OPTIONS)
    if db_engine == 'SQLite':
        db_name = forms.CharField(max_length=100)
        db_user = forms.CharField(max_length=100)
        db_password = forms.CharField(widget=forms.PasswordInput)
        db_host = forms.CharField(max_length=100)
        db_port = forms.CharField(max_length=100)
    elif db_engine == "SQL server":
        db_name = forms.CharField(max_length=100)
        db_user = forms.CharField(max_length=100)
        db_password = forms.CharField(widget=forms.PasswordInput)
        db_host = forms.CharField(max_length=100)
        db_port = forms.CharField(max_length=100)
    elif db_engine == "PostgresSQL":
        db_name = forms.CharField(max_length=100)
        db_user = forms.CharField(max_length=100)
        db_password = forms.CharField(widget=forms.PasswordInput)
        db_host = forms.CharField(max_length=100)
        db_port = forms.CharField(max_length=100)
    else:
        print("Error")
