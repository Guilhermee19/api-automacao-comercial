from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)
  deleted_at = models.DateTimeField(null=True, blank=True)
  deleted_by = models.ForeignKey(
      "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="deleted_users"
  )
  class Meta:
    abstract = True


class UserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('O email é obrigatório')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('type', 'MANAGER')
    return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
  TYPE_PERMISSION = (
      ("SALES", "SALES"),               # Vendedor
      ("CUSTOMER", "CUSTOMER"),         # Cliente
      ("MANAGER", "MANAGER"),           # Gerente
  )
  
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
  type = models.CharField(max_length=10, choices=TYPE_PERMISSION, default="CUSTOMER")
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'
    ordering = ['id']

  def __str__(self):
    return self.name
    
    
class Company(BaseModel):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Empresa'
    verbose_name_plural = 'Empresas'
    ordering = ['id']
      
  def __str__(self):
    return self.name
    

class Brand(BaseModel):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'
    ordering = ['id']
      
  def __str__(self):
    return self.name
    

class Collection(BaseModel):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Coleção'
    verbose_name_plural = 'Coleções'
    ordering = ['id']
      
  def __str__(self):
    return self.name
    
    
class PaymentMethod(BaseModel):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Forma de pagamento'
    verbose_name_plural = 'Formas de pagamento'
    ordering = ['id']
      
  def __str__(self):
    return self.name
    

class Product(BaseModel):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=15, decimal_places=2)
  description = models.CharField(max_length=255)
  brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
  collections = models.ManyToManyField('Collection', related_name='products')
  
  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    ordering = ['id']
      
  def __str__(self):
    return self.name
    
    
class Order(BaseModel):
  STATUS_CHOICES = (
      ("PENDING", "PENDING"),       # Pendente
      ("COMPLETED", "COMPLETED"),   # Concluído
  )
  
  company = models.ForeignKey(Company, related_name='orders', on_delete=models.PROTECT)
  salesperson = models.ForeignKey(User, limit_choices_to={'type': 'SALES'}, related_name='sales', on_delete=models.PROTECT)
  customer = models.ForeignKey(User, limit_choices_to={'type': 'CUSTOMER'}, related_name='orders', on_delete=models.PROTECT)
  date_of_sale = models.DateField()
  payment_method = models.ForeignKey(PaymentMethod, related_name='orders', on_delete=models.PROTECT)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
  total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

  class Meta:
    verbose_name = 'Pedido'
    verbose_name_plural = 'Pedidos'
    ordering = ['id']

  def __str__(self):
    return f'Pedido {self.id} - {self.status}'
  
  
class OrderProduct(BaseModel):
  order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name='order_products', on_delete=models.PROTECT)
  quantity = models.PositiveIntegerField()
  price = models.DecimalField(max_digits=15, decimal_places=2)

  class Meta:
    verbose_name = 'Produto do Pedido'
    verbose_name_plural = 'Produtos do Pedido'
    ordering = ['id']
    unique_together = ('order', 'product')

  def __str__(self):
    return f'Produto {self.product.name} no Pedido {self.order.id}'