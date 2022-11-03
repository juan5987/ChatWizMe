from django.db import models
from django.contrib.auth.models import User

class InputModel(models.Model):
    text_msg = models.TextField(
        max_length = 1000,
        blank= False,
        null = True,
        default= "",
    )
    # user = models.ForeignKey(User, on_delete = models.CASCADE)