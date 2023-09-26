from django import forms

class NewTask(forms.Form):
    task = forms.CharField(label="NewTask",max_length=20)
