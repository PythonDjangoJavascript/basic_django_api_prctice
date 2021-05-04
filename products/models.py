from django.db import models


class Manufacturer(models.Model):
    """Define Manufacturer database model"""

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Define product database model"""

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='porducts'
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantitiy = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
