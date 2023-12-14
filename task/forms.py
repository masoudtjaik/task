from django import forms
from .models import *
from django.contrib.auth.models import User
from .random_test import GetRandom
import random
class DutiesForm(forms.ModelForm):
    class  Meta:
        model=Task
        fields='__all__'
    

class UserForm(forms.Form):
    # x,y=GetRandom.get_random(),GetRandom.get_random()
    username=forms.CharField(label=' username '
                             ,max_length=10
                             ,required=True
                             ,error_messages={'required':'username is wrong'})
    password=forms.CharField(error_messages={'required':'username is wrong'},
        required=True,
        max_length=20,  
        label=' password',
        widget=forms.PasswordInput())
    random=forms.IntegerField(label='number')
    
    # @classmethod
    # def getrandom(cls):
    #     cls.x=GetRandom.get_random()
    #     cls.y=GetRandom.get_random()
    # def clean_random(self):
    #     if self.cleaned_data['random']==str(UserForm.x+UserForm.y):
    #         return self.cleaned_data['random']
    #     else :
    #         raise forms.ValidationError('number is wrong    ')

    
class SearchForm(forms.Form):
    search=forms.CharField(
       required=False,
       label='', 
       widget=forms.TextInput(attrs={'placeholder':'Searching.....' ,'class':'p-1' }))
    