from django.shortcuts import render


from django.shortcuts import render, HttpResponse, redirect
# added manually
# from datetime import datetime
# from home.models import Contact, CreateCustomUserForm, TourData, Department, Employee

from django.contrib import messages
# manually added users
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

# login required method
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home(request):
    users = User.objects.all()
    recipes = Recipe.objects.all()
    # recipe = recipes[0]
    # allRecipeReview = Recipe.objects.get(name="Pankakes").review_set.all()
    recipe = recipes[0].ingredients.split(",")
    contacts = Contact.objects.all()
    reviews = Review.objects.all()
    context = {'users': users, 'recipes': recipes, 'recipe': recipe,'reviews': reviews}
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request, 'customuser/home.html', context)

# recipeReview = Recipe.objects.get(name="Pankakes").review_set.all()


# def home(request):
#     # return HttpResponse('Home page')
#     tours = TourData.objects.all()
#     context = {'tours': tours}
#     # print(request.user.id)
#     # print(request.user.is_superuser)
#     # messages.success(request, 'Test message for alert messages')
#     if request.user.is_anonymous:
#         return redirect("/login")
#     return render(request, 'home/home.html', context)