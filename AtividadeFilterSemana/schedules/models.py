from django.db import models
from datetime import date


class Schedule(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255, null=True, blank=True)
    observation = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    @property
    def weekday(self):
        weekdays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        return weekdays[self.date.weekday()]
    
    @property
    def is_today(self):
        return self.date == date.today()

    def __str__(self):
        return self.title
