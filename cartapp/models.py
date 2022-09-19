from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(
        'название',
        max_length=100,
        db_index=True,
    )
    description = models.TextField(
        'описание',
        blank=True,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def format_price(self):
        return int(self.price * 100)

    def __str__(self):
        return self.name
