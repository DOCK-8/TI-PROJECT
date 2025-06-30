from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    correo = models.CharField()

    def __str__(self):
        return self.id+" : "+selft.name+" : "+self.correo

class Book(models.Model):
    id = models.IntegerField()
    titulo = models.CharField()
    autor = models.CharField()
    avalible = models.BoolField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.id+" = "+self.avalible+" : "+selft.titulo+" : "+self.autor+"->"+self.user_id
