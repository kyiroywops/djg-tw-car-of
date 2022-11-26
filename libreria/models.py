from django.db import models

# Create your models here.

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, verbose_name='Marca')
    imagen = models.ImageField(upload_to="imagenes/", null=True, verbose_name='Imagen')
    modelo = models.Charfield(max_length=50, verbose_name='Modelo')
    valor = models.IntegerField(verbose_name='Valor')
    fabricacion = models.IntegerField(verbose_name='Año')
    disponibilidad = models.Charfield(max_length=20, verbose_name='Disponibilidad')
    categoria = models.Charfield(max_length=20, verbose_name='Categoria')

    def __str__(self):
        fila = "Marca: " + self.marca + " Modelo: " + self.modelo + " Valor: " + self.valor + " Año: " + self.fabricacion + " Disponibilidad: " + self.disponibilidad + " Categoria: " + self.categoria
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()