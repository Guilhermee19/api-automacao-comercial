from rest_framework import generics
from rest_framework import permissions


from .models import User, Company, Brand, Collection, Product, Order, OrderProduct, PaymentMethod
from .serializers import UserSerializer, CompanySerializer, BrandSerializer, CollectionSerializer, ProductSerializer, OrderSerializer, OrderProductSerializer, PaymentMethodSerializer


# -----------| Users |-----------
class UsersViewSet(generics.ListCreateAPIView):
  permission_classes = (
    permissions.DjangoModelPermissions, 
  )
  queryset = User.objects.all()
  serializer_class = UserSerializer
    
class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SalesViewSet(generics.ListAPIView):
  permission_classes = (
    permissions.DjangoModelPermissions, 
    
  )
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def get_queryset(self):
    return self.queryset.filter(type='SALES')
  
class CustomerViewSet(generics.ListAPIView):
  permission_classes = (
    permissions.DjangoModelPermissions, 
  )
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def get_queryset(self):
    return self.queryset.filter(type='CUSTOMER')
    
# -----------| Companies |-----------
class CompaniesViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
# -----------| Brands |-----------
class BrandsViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class BrandViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
# -----------| Collections |-----------
class CollectionsViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
class CollectionViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions,
    )
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
# -----------| Products |-----------
class ProductsViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# -----------| Payment Methods |-----------
class PaymentMethodsViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer  

class PaymentMethodViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions,
    )
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer  
    
# -----------| Orders |-----------
class OrdersViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# -----------| Order Products |-----------

class OrderProductViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    
    def get_queryset(self):
      if self.kwargs.get('order_pk'):
        return self.queryset.filter(order_id=self.kwargs.get('order_pk'))
      return self.queryset.all()
    
    
class OrderProductViewSet(generics.ListCreateAPIView):
    permission_classes = (
      permissions.DjangoModelPermissions, 
    )
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    
    def get_queryset(self):
      if self.kwargs.get('order_pk'):
        return self.queryset.filter(order_id=self.kwargs.get('order_pk'))
      return self.queryset.all()
    