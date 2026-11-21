from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title