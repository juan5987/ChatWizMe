from django.db import models

class InputModel(models.Model):
    text_msg = models.TextField(
        max_length = 1000,
        blank= False,
        null = True,
        default= "",
    )