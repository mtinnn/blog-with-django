from django.contrib import admin
from .models import post,Category,profile,comment
# Register your models here.

admin.site.register(post)
admin.site.register(Category)       
admin.site.register(profile)
admin.site.register(comment)