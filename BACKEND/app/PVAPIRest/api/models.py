from django.db import models

class Irradiacion(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "irradiacion"
        managed = False

    def __str__(self):
        return f"{self.id} : {self.year} : {self.month} : {self.value}"


class Paneles(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    potencia = models.IntegerField()
    consumo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_vida = models.IntegerField()
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.IntegerField()
    alto = models.IntegerField()

    class Meta:
        db_table = "paneles"
        managed = False

    def __str__(self):
        return f"{self.id} : {self.modelo} : {self.precio} : {self.potencia} : {self.eficiencia}"


class Inversores(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    potencia = models.IntegerField()
    tension_admisible = models.IntegerField()
    consumo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_vida = models.IntegerField()
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "inversores"
        managed = False

    def __str__(self):
        return f"{self.id} : {self.modelo} : {self.precio} : {self.potencia} : {self.eficiencia}"


class Baterias(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    largo = models.IntegerField()
    ancho = models.IntegerField()
    alto = models.IntegerField()
    voltaje = models.IntegerField()
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=20)
    consumo_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "baterias"
        managed = False

    def __str__(self):
        return f"{self.id} : {self.modelo} : {self.precio} : {self.capacidad} : {self.eficiencia}"
