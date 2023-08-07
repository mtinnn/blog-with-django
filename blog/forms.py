from django import forms
from .models import post,Category

Choice=Category.objects.all().values_list('name','name')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','auth','category','snippet','body','header_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'title'
                }),
            'category': forms.Select( choices=Choice, attrs={
                "class": "form-control",
                'style': 'max-width: 300px;'
                ,}),

                
            'auth': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'value':'',
                'id': 'elder',
                'type': 'hidden',
                
                }),
            'body': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'snippet': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
                
        }


class CatForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

        widget={
            'title': forms.TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
         } )
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','category','snippet','body','header_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'title'
                }),
            'category': forms.Select( choices=Choice, attrs={
                "class": "form-control",
                'style': 'max-width: 300px;'
                ,}),

                
            'body': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'snippet': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),    
                
        }
