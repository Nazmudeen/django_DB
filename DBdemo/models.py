from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    address=models.CharField(max_length=20)
