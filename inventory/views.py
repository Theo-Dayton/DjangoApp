from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm, MenuItemCreateForm, MenuItemUpdateForm, RecipeRequirementCreateForm, RecipeRequirementUpdateForm


def home(request):
   return render(request, 'inventory/home.html')

   # CRUD - (R)ead
class IngredientList(LoginRequiredMixin, ListView):
   model = Ingredient

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement

# CRUD - (C)reate
class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'

class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Ingredient
   template_name = 'inventory/ingredient_create_form.html'
   form_class = IngredientCreateForm

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model=MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    form_class = MenuItemCreateForm

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model=RecipeRequirement
    template_name = 'inventory/recipe_requirement_create_form.html'
    form_class = RecipeRequirementCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)