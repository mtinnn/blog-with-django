from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from blog.models import profile,comment



class Editform(UserChangeForm):
        username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        first_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(max_length=150,widget=forms.EmailInput(attrs={'class':'form-control'}))     
        last_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        last_login=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        is_superuser=forms.CharField(max_length=150,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
        is_staff=forms.CharField(max_length=150,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
        is_active=forms.CharField(max_length=150,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
        password=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','type': 'hidden'}))

        

        
    
        class Meta:
         model=User           
         fields=['first_name', 'username', 'email', 'last_name','password','last_login','is_superuser','is_staff','is_active']
class Passworchange(UserChangeForm):
     old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type': 'password'}))
     new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type': 'password'}))
     new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type': 'password'}))
     
     class Meta:
          model=User
          fields=['old_password', 'new_password1','new_password2']
          


class ProfileEdit(UserChangeForm):
        bio = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        prof_image = forms.ImageField()

        class Meta:
             model=profile
             fields=['bio', 'prof_image']

class ProfileCreate(UserChangeForm):
        
        
        bio = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
        prof_image = forms.ImageField()

        class Meta:
          
          model=profile
          fields=['bio', 'prof_image',]

            
      
class AddcommentForm(forms.ModelForm):
     class Meta:
          model=comment
          fields=['name', 'body']


          widgets = {
               



            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'your name'
                }),
            'body': forms.Textarea(  attrs={
                "class": "form-control",
                'style': 'max-width: 300px;'
                ,}),}