from django.db import models

class Grup(models.Model):
    name = models.CharField(max_length=200)
    starosta = models.ForeignKey("students.Student", blank = True, null = True)
    def __str__(self):
        return self.name