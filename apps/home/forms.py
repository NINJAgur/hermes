from dataclasses import fields
from . models import Record, Update
from django.contrib.auth.models import User
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateInput):
    input_type = 'datetime'

class RecordForm(forms.ModelForm):
    created_by=forms.ModelChoiceField(queryset=User.objects.all(),empty_label="מטפל אחראי", to_field_name="id")
    class Meta:
        model=Record
        fields=['system_type', 'status', 'network', 'date_start', 'date_finish', 'progression', 
        'short_description', 'long_description', 'short_solution', 'long_solution']
        widgets = {
            'date_start': DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','type': 'date'}),
            'date_finish': DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','type': 'date'}),
            'short_description': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
            'long_description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'short_solution': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
            'long_solution': forms.Textarea(attrs={'rows': 5, 'cols': 50})
        }

class UpdateForm(forms.ModelForm):
    record = forms.ModelChoiceField(queryset=Record.objects.all(),empty_label="תקלה", to_field_name="id")
    class Meta:
       model = Update
       fields = ['desc'] 
       widgets = {
            'desc': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
       }

class InfoForm(forms.ModelForm):
    class Meta:
       pass 