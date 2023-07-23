from django.urls import path, include

from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('ingredient/list', views.IngredientList.as_view(), name="ingredientlist"),
   path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
   path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name="ingredientupdate"),
   path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name="ingredientdelete"),
   path('menuitem/list', views.MenuItemList.as_view(), name="menuitemlist"),
   path('menuitem/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),
   path('menuitem/update/<pk>', views.MenuItemUpdate.as_view(), name="menuitemupdate"),
   path('menuitem/delete/<pk>', views.MenuItemDelete.as_view(), name="menuitemdelete"),
   path('reciperequirement/list', views.RecipeRequirementList.as_view(), name="reciperequirementlist"),
   path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
   path('reciperequirement/update/<pk>', views.RecipeRequirementUpdate.as_view(), name="reciperequirementupdate"),
   path('reciperequirement/delete/<pk>', views.RecipeRequirementDelete.as_view(), name="reciperequirementdelete"),
   path('purchase/list', views.PurchaseList.as_view(), name="purchaselist"),
]