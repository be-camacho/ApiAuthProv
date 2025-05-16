from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128) 
    rol = models.CharField(max_length=1)
    idproveedor = models.IntegerField()

    class Meta:
        db_table = 'regprovs_user'
        managed = False