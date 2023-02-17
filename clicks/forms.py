# -*- coding: utf-8 -*-
from django import forms
from .models import Click

class ClickForm(forms.ModelForm):
    class Meta:
        model = Click
        fields = ('clicks',)