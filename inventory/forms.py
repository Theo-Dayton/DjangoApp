from django import forms
from .models import Ingredient,MenuItem,RecipeRequirement,Purchase

# CRUD - Create
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price', 'total_price')

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'price', 'image_link')

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'ingredient_quantity')

#CRUD - Update
class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price', 'total_price')

class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'price', 'image_link')

class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'ingredient_quantity')