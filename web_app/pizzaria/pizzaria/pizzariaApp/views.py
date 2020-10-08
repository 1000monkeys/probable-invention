from django.shortcuts import render

from pizzariaApp.models import Pizza, Topping


def toppings(request):
    """The toppings for the pizza"""

    pizza_name = request.GET['pizza']

    context = {
        'toppings': Topping.objects.filter(pizza=Pizza.objects.get(name=pizza_name)),
        'pizza': pizza_name
    }

    return render(request, 'toppings.html', context)


def pizzas(request):
    """A list of pizzas"""
    context = {
        'pizzas': Pizza.objects.all(),
    }

    return render(request, 'pizzas.html', context)


def index(request):
    """The home page for Learning Log"""
    return render(request, 'index.html')
