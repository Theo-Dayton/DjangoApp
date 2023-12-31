from django import forms
from .models import Ingredient,MenuItem,RecipeRequirement,Purchase

# CRUD - Create
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'price')

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'ingredient_quantity')

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item','timestamp')

#CRUD - Update
class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')

class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'price')

class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'ingredient_quantity')