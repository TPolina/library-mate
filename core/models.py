from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    hobby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self):
        return f"{self.full_name} (birth: {self.birth_year})"
