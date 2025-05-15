from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    idproveedor = models.IntegerField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Longitud para hash (recomendado)
    rol = models.CharField(max_length=20)

    class Meta:
        db_table = 'usuario'
        managed = False