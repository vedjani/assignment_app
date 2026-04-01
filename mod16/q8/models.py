from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    experience_years = models.PositiveSmallIntegerField(default=0)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30, blank=True)
    hospital = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['-experience_years', 'name']

    def __str__(self):
        return f"{self.name} ({self.speciality})"
