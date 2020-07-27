from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
