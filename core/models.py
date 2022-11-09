from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    # Se crea una tabla llamada core_employee

    name = models.CharField(max_length = 150, verbose_name='Nombres')
    dni = models.CharField(max_length = 10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(
        default=datetime.now,  verbose_name='Fecha de registro'
    )
    date_created = models.DateTimeField(auto_now=True) 
    date_updated = models.DateTimeField(auto_now_add=True) 
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='img/%Y/%m/%d', null=True, blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
    