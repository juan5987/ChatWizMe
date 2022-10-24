from xml.dom.minidom import Attr
from django.db import models
from django import forms

class InputModel(models.Model):
    text_msg = models.TextField(
        max_length = 1000,
        blank= False,
        null = True,
        default= "",
    )