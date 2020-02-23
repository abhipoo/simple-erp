from django import forms
from .models import Sales, Inventory
from django.db import models
from django.forms import Select


class JobForm(forms.ModelForm):

    class Meta:
        model = Sales

        #The first item in the (tuple) is the value and second is the label to be shown on the radio button
        sales_type_CHOICES = [
            ('immediate_sales','Immediate Sales (white slip)'),
            ('dtp_task','Dtp Task (job card)')
        ] 

        color_type_CHOICES = [
            ('bw','Black and White'),
            ('color','Color')
        ]

        page_type_CHOICES = [
            ('single','Single'),
            ('double','Back to back')
        ]

        #Overriding the default fields
        widgets = {
            'sales_type': Select(choices=sales_type_CHOICES),
            'color_type': Select(choices=color_type_CHOICES),
            'page_type': Select(choices=page_type_CHOICES),
        }

        exclude = ('job_date', 'operator', 'sku', )


class SkuForm(forms.ModelForm):

	class Meta:
		model = Inventory
		exclude = ('',)


class UpdateForm(forms.Form):
	quantity = forms.IntegerField(min_value = 0)
	CHOICES = [('add', 'add'), ('subtract', 'subtract'), ('update', 'update')]
	action = forms.ChoiceField(choices = CHOICES)
	comment = forms.CharField(widget=forms.Textarea)




	



