from django.db import models

# Create your models here.

#modelos que voy a utilizar

#estados de las mesas
class Estado(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre

#mesas
class Mesas(models.Model):
    numerom=models.IntegerField()
    cantidad= models.IntegerField()
    #si borro una categoria no se borran los productos asociados
    estado= models.ForeignKey(Estado,on_delete=models.PROTECT)

    def __str__(self) :
        return str(self.numerom)
