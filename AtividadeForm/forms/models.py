from django.db import models


class Person(models.Model):
    choices = (
        ('S', 'Student'),
        ('T', 'Teacher')
    )

    name = models.CharField(max_length=50)
    role = models.CharField(choices=choices, max_length=1)
    date_birth = models.DateField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.name
