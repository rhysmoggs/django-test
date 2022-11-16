from django.contrib import admin
from .models import Wishlist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date_added',
    )

    ordering = ('-date_added',)


admin.site.register(Wishlist, ProductAdmin)
