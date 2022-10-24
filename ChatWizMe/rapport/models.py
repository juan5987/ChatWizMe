from unittest.util import _MAX_LENGTH
from django.db import models


class Report(models.Model):
    ma_variable = "c'est quoi pip ?"
    content = models.CharField(max_length=1000)
