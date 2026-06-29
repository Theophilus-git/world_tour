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
    
    # This is a string representation of the tours
    def __str__(self):
        return (f"ID:{self.id}: From {self.orign_country} to {self.destination_country}, {self.number_of_nights} nigths cost ${self.price}")