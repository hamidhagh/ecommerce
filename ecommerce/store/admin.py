from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from . models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    
    pass

    #prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatedFieldAdmin, admin.ModelAdmin):

    list_display = ['title', 'category', 'brand', 'price', 'datetime_created']

    #prepopulated_fields = {'slug': ('title',)}
