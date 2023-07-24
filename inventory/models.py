from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0)
    total_price = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/ingredient/list'

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/menuitem/list'

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/reciperequirement/list'


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()