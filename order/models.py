from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name


class Order(models.Model):

    PIZZA_SIZE_30 = '30 cm'
    PIZZA_SIZE_50 = '50 cm'
    PIZZA_SIZE_CHOICES = (
        (30, PIZZA_SIZE_30),
        (50, PIZZA_SIZE_50)
    )
    pizza_id = models.ForeignKey(Pizza,
                                 on_delete=models.CASCADE)
    pizza_size = models.IntegerField(choices=PIZZA_SIZE_CHOICES)
    customer_name = models.ForeignKey(Customer,
                                      on_delete=models.CASCADE,
                                      to_field='full_name',
                                      null=True)

    customer_address = models.CharField(max_length=255,
                                        null=True,
                                        blank=True)

    def save(self, *args, **kwargs):
        if not self.customer_name:
            self.customer_name = Customer.objects.get_or_create(full_name="unknown")[0]
        super().save(*args, **kwargs)
