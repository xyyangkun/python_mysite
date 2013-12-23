from blog.models import blog
from django.contrib import admin
class Admin(admin.ModelAdmin):
    fields = (('title','time'), 'content')
admin.site.register(blog, Admin)
