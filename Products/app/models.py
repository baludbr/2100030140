from django.db import models

class Product(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.FloatField()
    availability = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
