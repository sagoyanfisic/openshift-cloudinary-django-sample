# -*- coding: utf-8 -*-
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    name_user = models.CharField("Nombre", max_length=200, blank=False)
    description = models.CharField("Descripción", max_length=500, blank=False)
    image = CloudinaryField('Imagen',blank=True)

    def __unicode__(self):
        try:
            public_id = self.image.name_user
        except AttributeError:
            public_id = ''
        return "Perfil-%s:%s" % (self.name_user, public_id)
