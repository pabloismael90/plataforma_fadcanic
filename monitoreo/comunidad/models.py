# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from cambiaahora.utils import get_file_path
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from actividades.fadcanic.models import *
from actividades.lugar.models import *
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Recolector(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Recolector Datos"
        verbose_name_plural = "Recolectores Datos"

    def __unicode__(self):
        return self.nombre

class Monitoreo(models.Model):
    recolector = models.ForeignKey(Recolector)
    fecha = models.DateField()
    eje = models.ForeignKey(EjeTransversal)
    resultado = models.ForeignKey(ResultadoPrograma)
    municipio = models.ForeignKey(Municipio)
    comunidad = ChainedForeignKey(
                                Comunidad,
                                chained_field="municipio", 
                                chained_model_field="municipio",
                                show_all=False, auto_choose=True,null=True, blank=True)
    actividad = models.ForeignKey(TipoActividad)
    resultados  = RichTextField('Resultados y/o logros de la actividad')
    #Participantes
    masculino = models.IntegerField()
    femenino = models.IntegerField()
    #participantes por edad
    menor_12 = models.IntegerField('Menor a 12 años')
    mayor_12 = models.IntegerField('12 a 18 años')
    mayor_18 = models.IntegerField('18 a 30 años')
    mayor_30 = models.IntegerField('30 a más años')
    #identidad etnica
    creole = models.IntegerField()
    miskito = models.IntegerField()
    ulwa = models.IntegerField()
    rama = models.IntegerField()
    mestizo = models.IntegerField()
    mayagna = models.IntegerField()
    garifuna = models.IntegerField()
    extranjero = models.IntegerField()
    #tipos de actores
    estudiante = models.IntegerField()
    docente = models.IntegerField()
    periodista = models.IntegerField('Periodista/comunicador')
    lideres = models.IntegerField('Líderes comunitarios')
    representantes = models.IntegerField('Representantes de Organizaciones')
    autoridades = models.IntegerField('Autoridades comunitarias')
    comunitarios = models.IntegerField('Comunitarios/Pobladores')
    user = models.ForeignKey(User) 

    class Meta:
        verbose_name = "Monitoreo Actividad"
        verbose_name_plural = "Monitoreo Actividades"

    


    
