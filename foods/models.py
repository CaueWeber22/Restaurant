from django.db import models
from django.utils.translation import gettext_lazy as _

class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE)
    description = models.CharField(_(""), max_length=50, default="No description")
    image = models.ImageField(upload_to = 'food_image', default="no_image")
    is_available = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    category_type = models.CharField(_(""), max_length = 50)

    def __str__(self) -> str:
        return self.category_type
