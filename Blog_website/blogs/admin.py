from django.contrib import admin
from blogs.models import Post,Contact

# Register your models here.

# Registering Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']

# Registering Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','feedback']