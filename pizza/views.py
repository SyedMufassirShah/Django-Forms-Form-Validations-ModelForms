from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "pizza/home.html"


def Order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        # filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_order = filled_form.save()
            created_order_pk = created_order.id
            note = (
                "Your Order has been placed.\nIn a while your %s %s and %s pizza will be at your Door Steps!"
                % (
                    filled_form.cleaned_data["size"],
                    filled_form.cleaned_data["topping1"],
                    filled_form.cleaned_data["topping2"],
                )
            )
            filled_form = PizzaForm()
        else:
            created_order_pk = None
            note = "Order Failed. Please Try Again!"
        return render(
            request,
            "pizza/order.html",
            {
                "form": filled_form,
                "note": note,
                "multiple_form": multiple_form,
                "created_order_pk": created_order_pk,
            },
        )
    else:
        form = PizzaForm()
        return render(
            request, "pizza/order.html", {"form": form, "multiple_form": multiple_form}
        )


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data["number"]
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["topping1"])
            note = "Your Orer Has Been Placed Successfully!"
        else:
            note = "Order was not Created! Please try again..."
        return render(request, "pizza/pizzas.html", {"formset": formset, "note": note})
    else:
        return render(request, "pizza/pizzas.html", {"formset": formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    note = ""
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Your Order Has Been Updated Successfully!"
            form = filled_form
        else:
            note = "Order was not Updated! Please try again..."
    return render(
        request,
        "pizza/edit_order.html",
        {"pizzaform": form, "pizza": pizza, "note": note},
    )
