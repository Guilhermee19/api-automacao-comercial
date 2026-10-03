from django.contrib import admin

# Register your models here.
from .models import User, Company, Brand, Collection, Product, Order, OrderProduct, PaymentMethod

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'type', 'created_at', 'updated_at', 'is_active')
  
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at', 'updated_at', 'is_active')
  
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at', 'updated_at', 'is_active')
  
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at', 'updated_at', 'is_active')
  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'description', 'brand', 'created_at', 'updated_at', 'is_active')
  
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at', 'updated_at', 'is_active')
  
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('company', 'salesperson', 'status', 'created_at', 'updated_at', 'is_active')
  
@admin.register(OrderProduct)
class OrderItemAdmin(admin.ModelAdmin):
  list_display = ('order', 'product', 'quantity', 'price', 'created_at', 'updated_at', 'is_active')
  