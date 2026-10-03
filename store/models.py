from django.db import models

class Base(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)
  deleted_at = models.DateTimeField(null=True, blank=True)
  deleted_by = models.ForeignKey(
      "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="deleted_users"
  )
  class Meta:
    abstract = True
    
    
class User(Base):
  TYPE_PERMISSION = (
      ("SALES", "SALES"),               # Vendedor
      ("CUSTOMER", "CUSTOMER"),         # Cliente
      ("MANAGER", "MANAGER"),           # Gerente
  )
  
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
  type = models.CharField(max_length=10, choices=TYPE_PERMISSION, default="RETRIEVE")
  class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'
    ordering = ['id']
      
    def __str__(self):
      return self.name
    
    
class Company(Base):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Empresa'
    verbose_name_plural = 'Empresas'
    ordering = ['id']
      
    def __str__(self):
      return self.name
    

class Brand(Base):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'
    ordering = ['id']
      
    def __str__(self):
      return self.name
    

class Collection(Base):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Coleção'
    verbose_name_plural = 'Coleções'
    ordering = ['id']
      
    def __str__(self):
      return self.name
    
    
class PaymentMethod(Base):
  name = models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Forma de pagamento'
    verbose_name_plural = 'Formas de pagamento'
    ordering = ['id']
      
    def __str__(self):
      return self.name
    

class Product(Base):
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
    
    
class Order(Base):
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
  
class OrderProduct(Base):
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