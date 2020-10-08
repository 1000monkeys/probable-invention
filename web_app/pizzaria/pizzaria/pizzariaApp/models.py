from django.db import models


class Pizza(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        if len(self.name) > 20:
            return self.name[:20] + ...
        else:
            return self.name


class Topping(models.Model):
    name = models.TextField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.name) > 20:
            return self.name[:20] + ...
        else:
            return self.name
