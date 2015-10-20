from django.db import models


class Student(models.Model):
    fio = models.CharField(max_length=500)
    bdata = models.DateField()
    bilet = models.CharField(max_length=50)
    cgrup = models.ForeignKey("grups.Grup")
    
    def __str__(self):
        return(self.fio)