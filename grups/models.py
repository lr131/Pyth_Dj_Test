from django.db import models

class Grup(models.Model):
    name = models.CharField("Название группы", max_length=200)
    starosta = models.ForeignKey("students.Student", blank = True, null = True, verbose_name="Староста")
    def __str__(self):
        return self.name