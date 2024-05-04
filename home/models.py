from django.db import models


class Destination(models.Model):

    name = models.CharField(max_length=100)
    review = models.IntegerField()
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='my_pics')
    offer = models.BooleanField(default=False)


    