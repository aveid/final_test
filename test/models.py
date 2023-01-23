from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent:
            return f"{self.name} -> {self.parent.name}"
        return self.name


class Product(models.Model):
    PRODUCT_TYPE = (
        (1, "на складе есть"),
        (2, "на складе нет"),
        (3, "под заказ")
    )
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

