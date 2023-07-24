from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, F

from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm, MenuItemCreateForm, MenuItemUpdateForm, RecipeRequirementCreateForm, RecipeRequirementUpdateForm


def home(request):
   return render(request, 'inventory/home.html')

   # CRUD - (R)ead
class IngredientList(ListView):
   model = Ingredient

class MenuItemList(ListView):
    model = MenuItem

class RecipeRequirementList(ListView):
    model = RecipeRequirement

class PurchaseList(ListView):
    model = Purchase

# CRUD - (C)reate
class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'

class CostsAndRevenue(TemplateView):
   template_name = 'inventory/costs_and_revenue.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["purchases"] = Purchase.objects.all()
      revenue = Purchase.objects.aggregate(
         revenue=Sum("menu_item__price"))["revenue"]
      total_cost = 0
      for purchase in Purchase.objects.all():
         for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
               total_cost += recipe_requirement.ingredient.unit_price * \
                  recipe_requirement.ingredient_quantity

      context["revenue"] = revenue
      context["total_cost"] = total_cost
      context["profit"] = revenue - total_cost

      return context

class IngredientCreate(CreateView):
   model = Ingredient
   template_name = 'inventory/ingredient_create_form.html'
   form_class = IngredientCreateForm

class MenuItemCreate(CreateView):
    model=MenuItem
    template_name = 'inventory/menuitem_create_form.html'
    form_class = MenuItemCreateForm

class RecipeRequirementCreate(CreateView):
    model=RecipeRequirement
    template_name = 'inventory/recipe_requirement_create_form.html'
    form_class = RecipeRequirementCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IngredientUpdate(UpdateView):
   model = Ingredient
   template_name = 'inventory/ingredient_update_form.html'
   form_class = IngredientUpdateForm

class MenuItemUpdate(UpdateView):
   model = MenuItem
   template_name = 'inventory/menuitem_update_form.html'
   form_class = MenuItemUpdateForm

class RecipeRequirementUpdate(UpdateView):
   model = RecipeRequirement
   template_name = 'inventory/reciperequirement_update_form.html'
   form_class = RecipeRequirementUpdateForm

# CRUD - (D)elete
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = '/ingredient/list'

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete_form.html'
    success_url = '/menuitem/list'

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_delete_form.html'
    success_url = '/reciperequirement/list'