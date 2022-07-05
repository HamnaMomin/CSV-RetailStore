from django.db import models
import uuid

# Create your models here.

class RetailStore(models.Model):
    store_id = models.IntegerField(default=111)
    sku = models.CharField(max_length=200,unique=True)
    product_name = models.CharField(max_length=200,unique=True)
    price = models.FloatField(blank=True)
    date = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
        unique_together = ['sku', 'product_name']


    def __str__(self):
        return f"{self.store_id} -- {self.sku}"





