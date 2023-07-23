from django.db import models

class Ingredient(models.Model):
    name = models.CharField()
    quantity = models.IntegerField(default=0)
    unit = models.CharField()
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

class MenuItem(models.Model):
    name = models.CharField()
    price = models.IntegerField(default=0)
    image_link = models.CharField()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.IntegerField(default=0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()