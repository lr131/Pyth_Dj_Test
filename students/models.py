from django.db import models


class Student(models.Model):
    fio = models.CharField("ФИО", max_length=500)
    bdata = models.DateField("Дата рождения")
    bilet = models.CharField("Номер студ.билета", max_length=50, unique=True)
    cgrup = models.ForeignKey("grups.Grup", verbose_name="В какой группе")
    
    def __str__(self):
        return(self.fio)