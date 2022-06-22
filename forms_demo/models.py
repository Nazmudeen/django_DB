from django.db import models


class Customer(models.Model):
    firstname=models.CharField(max_length=20,default='name')
    def __str__(self):
        return self.firstname
    lastname=models.CharField(max_length=20,verbose_name='surname',blank=True,default='surname')
    address=models.CharField(max_length=20)
    phone=models.BigIntegerField()

# Create your models here.