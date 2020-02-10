from django import forms
from .models import Sales
from django.db import models
from django.forms import RadioSelect

class JobForm(forms.ModelForm):

    class Meta:
        model = Sales
        exclude = ('job_date',)
