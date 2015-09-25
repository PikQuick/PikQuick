# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Todas las Publicaciones"
        ordering = ['-fecha']

    usuario = models.CharField(u'Usuario', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    img1 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    img2 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    desc1 = models.TextField(u'Epigrafe Imagen 1' , max_length = 100 , default='')
    desc2 = models.TextField(u'Epigrafe Imagen 2' , max_length = 100 , default='')
    descPub = models.TextField(u'Descripcion de la Publicacion' , max_length = 100 , default='¿?')
    published = models.BooleanField(u'Publicado?', default=True)

    def __str__(self):
        return self.usuario + " / "+self.descPub

class Coment(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    postDelComent = models.ForeignKey(Entrada)
    fecha = models.DateTimeField(u'Fecha del comentario',auto_now_add=True)
    def __str__(self):
        return "Nombre: "+self.nombre+" / Mensaje: "+self.mensaje
