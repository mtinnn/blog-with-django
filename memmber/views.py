from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy ,reverse  
from .form import *
from blog.models import profile,comment,post
from django.shortcuts import get_object_or_404


class AddCommentView(CreateView):
	model = comment
	form_class = AddcommentForm
	template_name = 'comments/addcomment.html'
	
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
    
	success_url= reverse_lazy("home")
		      
    
     


      


class ProfileCreateView(generic.CreateView):
    model=profile
    template_name="registration/profile_create.html"
    form_class=ProfileCreate
    success_url=reverse_lazy('home') 

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class  ProfileEditView(generic.UpdateView):
    model=profile
    template_name='registration/profile_edit.html'
    fields=['bio','prof_image']
    
    success_url=reverse_lazy('home')
    



class profileView(DetailView):
    model = profile
    template_name = 'registration/profile.html'

    def get_context_data(self,*args, **kwargs):

        context=super(profileView, self).get_context_data(*args, **kwargs)
        page_user=get_object_or_404(profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context

class UserRegisterForm(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url=reverse_lazy('login')
    
    def get_object(self):
        return self.request.user

    


class userUpdateForm(generic.UpdateView):
    form_class=Editform
    template_name='registration/edit.html   '
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class PassworchangeForm(generic.UpdateView):
    form_class=Passworchange
    success_url=reverse_lazy('change-success')

    
def PassChangeSuccess(request):
    return render(request,'registration/passSuccess.html',{})