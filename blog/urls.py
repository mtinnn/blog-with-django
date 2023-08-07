
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path("articles/<int:pk>", DetailView.as_view(),name='detail-post'),
    path('add_post', CreateView.as_view(),name='add-post'),
    path('edit_post/<int:pk>', EditView.as_view(),name='edit-post'),
    path('delete_post/<int:pk>', DeleteView.as_view(),name='delete-post'),
    path('create/category', CreateCategorty.as_view(),name='create-category'),
    path('category/<str:cats>',CategoryList,name='category_list'),
    path('like/<int:pk>',LikeView,name='like-view'),
]
