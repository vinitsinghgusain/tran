from django.db import models


class trainer(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Country = models.CharField(max_length=100, blank=False)
    Skills = models.TextField(blank=False)
    Email = models.EmailField(blank=False)
    Mobile_number = models.CharField(max_length=100, blank=False)
    Profession = models.CharField(max_length=100, blank=False)
    Address = models.TextField(blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.Name
