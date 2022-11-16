from django.contrib import admin
from .models import Blogger,Blog
# Register your models here.

@admin.register(Blogger)

class BloggerAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']