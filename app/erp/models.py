from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from datetime import datetime


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipos'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    tipo = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique= True, verbose_name='DNI')
    age = models.PositiveIntegerField(default=0, verbose_name='Edad')
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Salario')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateField(auto_now_add=True, verbose_name='Fecha de actualización')
    state = models.BooleanField(default=True, verbose_name='Estado')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True, verbose_name='Avatar')
    cv = models.FileField(upload_to='cv/%Y/%m/%d', verbose_name='Curriculum vitae')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
