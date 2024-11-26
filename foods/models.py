from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to = 'food_image')

    def __str__(self) -> str:
        return self.name

