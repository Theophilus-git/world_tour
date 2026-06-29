from django.db import models

# Create your models here.
class tour(models.Model):
    # We need a origin country
    # We need a destination country
    # we need number of nights
    # we need price

    orign_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # Object Relation Mapping : Takes care of create, delete, read, and update