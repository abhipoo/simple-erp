from django import forms
from .models import Sales
from django.db import models
from django.forms import RadioSelect

from .models import Inventory

class JobForm(forms.ModelForm):

    class Meta:
        model = Sales
        exclude = ('job_date',)



class SkuForm(forms.ModelForm):

	class Meta:
		model = Inventory
		exclude = ('',)


class UpdateForm(forms.Form):
	quantity = forms.IntegerField(min_value = 0)
	



