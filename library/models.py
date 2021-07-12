from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField('Titulo',max_length=100, blank=False)
    type = models.CharField('Tipo', max_length=40,blank=False)
    author = models.CharField('Autor', max_length=100,blank=False)
    creation_date = models.DateField('Fecha alta',null=False)
    number_of_pages=models.IntegerField(null=True)
    user=models.CharField(max_length=30,null=False)
    borrow_date= models.DateField('Fecha de prestamo',null=False)  