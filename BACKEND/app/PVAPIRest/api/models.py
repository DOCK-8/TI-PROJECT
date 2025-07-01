from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    correo = models.CharField( max_length = 100)

    class Meta:
        db_table = "usuarios"
        managed = False
        
    def __str__(self):
        return f"{self.id} : {self.nombre} : {self.correo}"

class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    titulo = models.CharField(max_length = 150)
    autor = models.CharField(max_length = 100)
    disponible = models.BooleanField(default = True)
    usuario_id = models.ForeignKey(User, on_delete = models.DO_NOTHING, db_column = "usuario_id")

    class Meta:
        db_table = "libros"
        managed = False

    def __str__(self):
        return f"{self.id} = {self.disponible} : {self.titulo} : {self.autor}->{self.usuario_id}"
