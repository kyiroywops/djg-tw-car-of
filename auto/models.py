from django.db import models

# Create your models here.

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, verbose_name='Marca')
    imagen = models.ImageField(upload_to="imagenes/", null=True, verbose_name='Imagen')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    valor = models.IntegerField(verbose_name='Valor')
    fabricacion = models.IntegerField(verbose_name='Año')
    disponibilidad = models.CharField(max_length=1, verbose_name='Disponibilidad')
    categoria = models.CharField(max_length=20, verbose_name='Categoria')

    def __str__(self):
        fila = "Marca: " + self.marca + " Modelo: " + self.modelo + " Valor: " + self.valor + " Año: " + self.fabricacion + " Disponibilidad: " + self.disponibilidad + " Categoria: " + self.categoria
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

  
class Compradores(models.Model):
  compradorRut = models.IntegerField(verbose_name='Rut Comprador', primary_key=True)
  compradorNombre = models.CharField(max_length=50, verbose_name='Comprador Nombre')
  compradorApellidoPat = models.CharField(max_length=50, verbose_name='Comprador Apellido Pat')
  compradorApellidoMat = models.CharField(max_length=50, verbose_name='Comprador Apellido Mat')
  compradorTelefono = models.IntegerField(verbose_name='Telefono')
  compradorClave = models.CharField(max_length=100, verbose_name='Contraseña')
  
class Vendedores(models.Model):
  vendedorRut = models.IntegerField(verbose_name='Rut Vendedor', primary_key=True)
  vendedorNombre = models.CharField(max_length=50, verbose_name='Comprador Nombre')
  vendedorApellidoPat = models.CharField(max_length=50, verbose_name='Comprador Vendedor Pat')
  vendedorApellidoMat = models.CharField(max_length=50, verbose_name='Comprador Vendedor Mat')
  vendedorClave = models.CharField(max_length=100, verbose_name='Contraseña')

class Detalles(models.Model):
  id_detalle = models.AutoField(primary_key=True)
  autoCod = models.ForeignKey(Auto, on_delete=models.CASCADE)

class Ventas(models.Model):
  id = models.AutoField(primary_key=True)
  vendedorrut = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
  idauto = models.ForeignKey(Auto, on_delete=models.CASCADE)
  fechaventa = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
  compradorrut = models.ForeignKey(Compradores, on_delete=models.CASCADE)
  id_detalle = models.ForeignKey(Detalles, on_delete=models.CASCADE)