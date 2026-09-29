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
      ("SALESPERSON", "SALESPERSON"),   # Vendedor
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
  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    ordering = ['id']
      
    def __str__(self):
      return self.name