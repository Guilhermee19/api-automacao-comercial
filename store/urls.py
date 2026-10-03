from django.urls import path
from .views import *

urlpatterns = [
  path('users/', UsersViewSet.as_view(), name='user-list'),
  path('user/<int:pk>/', UserViewSet.as_view(), name='user-detail'),
  path('sales/', SalesViewSet.as_view(), name='sale-list'),
  path('customers/', CustomerViewSet.as_view(), name='customer-list'),
  
    path('companies/', CompaniesViewSet.as_view(), name='company-list'),
  path('company/<int:pk>/', CompanyViewSet.as_view(), name='company-detail'),
  
  path('brands/', BrandsViewSet.as_view(), name='brand-list'),
  path('brand/<int:pk>/', BrandViewSet.as_view(), name='brand-detail'),
  
  path('collections/', CollectionsViewSet.as_view(), name='collection-list'),
  path('collection/<int:pk>/', CollectionViewSet.as_view(), name='collection-detail'),
  
  path('products/', ProductsViewSet.as_view(), name='product-list'),
  path('product/<int:pk>/', ProductViewSet.as_view(), name='product-detail'),
  
  path('payment-methods/', PaymentMethodsViewSet.as_view(), name='payment-method-list'),
  path('payment-method/<int:pk>/', PaymentMethodViewSet.as_view(), name='payment-method-detail'),
  
  path('orders/', OrdersViewSet.as_view(), name='order-list'),
  path('order/<int:pk>/', OrderViewSet.as_view(), name='order-detail'),
  
  # path('order-products/', OrderProductViewSet.as_view(), name='order-product-list'),
  # path('order-products/<int:pk>/', OrderProductViewSet.as_view(), name='order-product-detail'),
]