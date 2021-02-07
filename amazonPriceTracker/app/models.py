from django.db import models
from .utils import get_product_info

class Product(models.Model):
    name = models.CharField(max_length=350, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    rate = models.FloatField(blank=True)
    rating = models.IntegerField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        name, price, rate, rating, image = get_product_info(self.url)
        old_price = self.current_price
        if self.current_price:
            if old_price != price:
                self.price_difference = round(price - old_price, 2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0
        self.name = name
        self.current_price = price
        self.rate = rate
        self.rating = rating
        self.image = image

        super().save(*args, **kwargs)
