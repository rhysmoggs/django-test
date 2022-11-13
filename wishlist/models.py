from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    """
    List user wishlist
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ displays wihslist by most recently added first """
        ordering = ['-date_added']

    def __str__(self):
        return f"({self.user})'s wishlist"
