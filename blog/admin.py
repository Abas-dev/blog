from django.contrib import admin
from .models import BlogDetails,Blogger,Categories
# Register your models here.
admin.site.register(BlogDetails)
admin.site.register(Blogger)
admin.site.register(Categories)