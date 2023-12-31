from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth import logout

from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm, PurchaseCreateForm, MenuItemCreateForm, MenuItemUpdateForm, RecipeRequirementCreateForm, RecipeRequirementUpdateForm


class Home(LoginRequiredMixin, TemplateView):
   template_name = 'inventory/home.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["ingredients"] = Ingredient.objects.all()
      context["menuitems"] = MenuItem.objects.all()
      context["reciperequirements"] = RecipeRequirement.objects.all()
      context["purchases"] = Purchase.objects.all()
      return context

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect("home")

class CostsAndRevenue(LoginRequiredMixin, TemplateView):
   template_name = 'inventory/costs_and_revenue.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      purchases = Purchase.objects.all()
      total_revenue = Purchase.objects.aggregate(
         total_revenue=Sum("menu_item__price"))["total_revenue"]
      total_cost = 0
      revenue = []
      costs= []

      for purchase in Purchase.objects.all():
         revenue.append(purchase.menu_item.price)
         current_cost = 0
         for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
               total_cost += recipe_requirement.ingredient.unit_price * \
                  recipe_requirement.ingredient_quantity
               current_cost += recipe_requirement.ingredient.unit_price * \
                  recipe_requirement.ingredient_quantity
         costs.append(current_cost)

      profit = []
      for i in range(len(purchases)):
         current_profit = revenue[i] - costs[i]
         profit.append(current_profit)

      context["purchases"] = purchases
      context["total_revenue"] = total_revenue
      context["total_cost"] = total_cost
      context["total_profit"] = total_revenue - total_cost
      context["ingredients"] = Ingredient.objects.all()
      context["menuitems"] = MenuItem.objects.all()
      context["reciperequirements"] = RecipeRequirement.objects.all()
      context['revenue'] = revenue
      context['costs'] = costs
      context['profit'] = profit


      return context

# CRUD - (C)reate
class IngredientCreate(LoginRequiredMixin, CreateView):
   model = Ingredient
   template_name = 'inventory/ingredient_create_form.html'
   form_class = IngredientCreateForm

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model= MenuItem
    template_name = 'inventory/menuitem_create_form.html'
    form_class = MenuItemCreateForm

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model= RecipeRequirement
    template_name = 'inventory/reciperequirement_create_form.html'
    form_class = RecipeRequirementCreateForm

class PurchaseCreate(LoginRequiredMixin, CreateView):
   model = Purchase
   template_name = 'inventory/purchase_create_form.html'
   form_class = PurchaseCreateForm

# CRUD - (R)ead
class IngredientList(LoginRequiredMixin, ListView):
   model = Ingredient

class MenuItemList(LoginRequiredMixin, ListView):
   model = MenuItem

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["reciperequirement_list"] = RecipeRequirement.objects.all()
      return context

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["menuitems"] = MenuItem.objects.all()
      return context
    

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase

# CRUD - (U)pdate
class IngredientUpdate(LoginRequiredMixin, UpdateView):
   model = Ingredient
   template_name = 'inventory/ingredient_update_form.html'
   form_class = IngredientUpdateForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
   model = MenuItem
   template_name = 'inventory/menuitem_update_form.html'
   form_class = MenuItemUpdateForm

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
   model = RecipeRequirement
   template_name = 'inventory/reciperequirement_update_form.html'
   form_class = RecipeRequirementUpdateForm

# CRUD - (D)elete
class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = '/ingredient/list'

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete_form.html'
    success_url = '/menuitem/list'

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_delete_form.html'
    success_url = '/reciperequirement/list'