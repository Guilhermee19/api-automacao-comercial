from rest_framework import serializers
from django.db.models import Avg

from .models import User, Company, Brand, Collection, Product, PaymentMethod, Order, OrderProduct

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'type', 'is_active', 'created_at', 'updated_at')
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')
        
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'brand', 'collections', 'is_active', 'created_at', 'updated_at')
        

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'name', 'is_active', 'created_at', 'updated_at')
        

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'quantity', 'price', 'is_active', 'created_at', 'updated_at')
        

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'company', 'salesperson', 'customer', 'date_of_sale', 'payment_method', 'status', 'total', 'is_active', 'created_at', 'updated_at', 'order_products')