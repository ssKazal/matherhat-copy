from django.db import models


class MadrasahFigure(models.Model):
    teacher = models.CharField(max_length=10, null=True)
    teacher_bn = models.CharField(max_length=10, null=True)
    student = models.CharField(max_length=10, null=True)
    student_bn = models.CharField(max_length=10, null=True)
    staff = models.CharField(max_length=10, null=True)
    staff_bn = models.CharField(max_length=10, null=True)
    active_year = models.CharField(max_length=10, null=True)
    active_year_bn = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.id)
