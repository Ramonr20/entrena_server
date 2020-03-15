from django.db import models
import re
from django.urls import reverse


class Room(models.Model):
    nombre_hab = models.CharField("Nombre habitación",max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.nombre_hab

    def get_absolute_url(self):
        return reverse('vistas:lista_rooms')
    
    class Meta():
        ordering = ['id']
        
class Node(models.Model):
    tipo_nodo = models.CharField("Tipo de nodo",max_length=100, blank=False)

    # ...
    """
    Adding a through option to the field will let Django know
    that it should use that model instead of creating one
    for you.
    """
    rooms = models.ManyToManyField(Room, through='Room_Node')

    def __str__(self):
        return self.tipo_nodo

    def get_absolute_url(self):
        return reverse('vistas:lista_nodes')

    class Meta:
        ordering = ['id']

class Room_Node(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

    class Meta():
        ordering = ['pk']

    # def save(self, *args, **kwargs):
    #     dig = re.sub("\D", "", self.room.nombre_hab)
    #     id_name = self.room.nombre_hab[:3] + dig
    #     id_name += self.node.tipo_nodo[:2]
    #     id_name += str(self.no_node)
        
    #     self.id_hab_nodo = id_name.upper()
        
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vistas:lista_room_node', kwargs={ 'pk':self.room.pk })

class Reg_Node(models.Model):
    voltaje = models.FloatField("Voltaje",default=0.0)
    corriente = models.FloatField("Corriente",default=0.0)
    fac_de_pot = models.FloatField("factor de potencia",default=0.0)
    pot_activa = models.FloatField("Potencia activa",default=0.0)
    pot_real = models.FloatField("Potencia real",default=0.0)
    pot_aparente = models.FloatField("Potencia aparente",default=0.0)
    flag = models.BooleanField("Estado", default=True)
    date = models.DateTimeField("Fecha de registro",auto_now_add=True)

    room_node = models.ForeignKey(Room_Node, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']
