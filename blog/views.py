from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import post,Category
from django.urls import reverse_lazy,reverse
from .forms import *
from django.http import HttpResponseRedirect




class HomeView(ListView):
    model = post
    template_name='home.html'
    ordering =['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context
    


class DetailView(DetailView):   
    model = post
    template_name='detail.html'

    def get_context_data(self, *args, **kwargs):
        context=super(DetailView,self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(post,id=self.kwargs['pk'])
        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True
        total_like=stuff.like.count()
        context['total_like']=total_like
        context['liked']=liked
        return context

class CreateView(CreateView):
    model = post
    form_class = UserInfoForm
    template_name='create.html'
    #  fields = '__all__'

class  EditView(UpdateView):
    model = post
    form_class=EditForm
    template_name='edit.html'


class DeleteView(DeleteView):
    model = post
    template_name='delete.html'
    success_url=reverse_lazy("home")

class CreateCategorty(CreateView):
    model = Category
    template_name='addcat.html'
    form_class = CatForm

def CategoryList(request,cats):
  category_list_post=post.objects.filter(category=cats)
  return render(request,'category.html',{'category_post':category_list_post,'cats':cats})


def LikeView(request,pk):
    poost=get_object_or_404(post,id=request.POST.get('post-id'))
    
    liked=False
    if poost.like.filter(id=request.user.id).exists():
        poost.like.remove(request.user)
    else:
        poost.like.add(request.user)
    return HttpResponseRedirect(reverse('detail-post',args=[str(pk)] ))
     