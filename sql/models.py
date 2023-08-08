from django.db import models

# Create your models here.
class DataEntry(models.Model):
    sql_statement = models.CharField(max_length=200)
