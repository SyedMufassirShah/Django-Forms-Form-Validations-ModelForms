from django.contrib import admin

# Register your models here.
from .models import Pizza, Size

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'size' , 'topping1', "topping2")

admin.site.register(Size)
admin.site.register(Pizza, OrderAdmin)