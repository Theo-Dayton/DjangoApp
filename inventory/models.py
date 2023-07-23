from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=30)
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    image_link = models.CharField(max_length=60)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.IntegerField(default=0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()