from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(blank=True)

    def __str__(self):
       return self.name

class Ods(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.name

class InformationSources(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    institutions = models.TextField()
    year = models.DateField()
    tipe = models.CharField(max_length=30)
    number_of_queries = models.IntegerField()
    description = models.TextField()
