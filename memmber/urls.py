from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',UserRegisterForm.as_view(),name='register'),
    path('setting/',userUpdateForm.as_view(),name='setting'),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/chnagpass.html', success_url=reverse_lazy('change-success')),name='change-password'),
    path('password/sucsses/',PassChangeSuccess ,name='change-success'),
    path('<int:pk>/profile/',profileView.as_view(),name='profile-user'),
    path('<int:pk>/profile-edit/',ProfileEditView.as_view(),name='profile-edit'),
    path('<create/profile/',ProfileCreateView.as_view(),name='profile-create'),
    path("<int:pk>/add-comment>",AddCommentView.as_view(),name='add-comment'),
    
]
