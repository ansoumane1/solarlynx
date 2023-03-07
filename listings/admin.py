from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.
class orderReviewInlines(admin.TabularInline):
    model = Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'price', 'available')
    list_filter = ('category', 'available')
    list_editable = ('price','available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [orderReviewInlines]



