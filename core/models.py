from django.db import models

# Create your models here.
SEX = (('female', 'Female'), ('male', 'Male'))

class Customer(models.Model):
    name: models.CharField(max_length=255)
    se = models.CharField(max_length=SEX)

    
address = models.CharField(max_length=255)


def __str__(self) -> str:
    return self.name