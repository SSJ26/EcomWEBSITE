from django.contrib import admin
from .models import *
# Register your models here.
class Imageshow(admin.ModelAdmin):
    list_display=['name','desc','img','category','created_by']
admin.site.register(Product, Imageshow)
class AdminContact(admin.ModelAdmin):
    list_display=['name','email','phone','concern']

admin.site.register(Contact,AdminContact)
admin.site.register(Category)
class listCart(admin.ModelAdmin):
    list_display=['product_id','user_id','time']
admin.site.register(Cart,listCart)
admin.site.register(Buy)
admin.site.register(StoreUser)