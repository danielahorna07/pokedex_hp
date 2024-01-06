from django.db import models

class Pokemon(models.Model):
    id     = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=100)
    tipo   = models.ManyToManyField('Type', related_name = 'pokemons')
    altura = models.IntegerField()
    peso   = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
# Clase necesaria al ser relación 1:M -> 1 pokemón puede tener múltiples tipos
class Type(models.Model):
    id     = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

   
