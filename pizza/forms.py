from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
# topping1 = forms.CharField(max_length=100, label='Topping 1')
# topping2 = forms.CharField(max_length=100, label='Topping 2')
# size = forms.ChoiceField(label='Size', choices=[
#     ('small','Small') , ('medium','Medium') , ('large','Large')
# ])


class PizzaForm(forms.ModelForm):

    # image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ["topping1", "topping2", "size"]
        labels = {"topping1": "Topping 1", "topping1": "Topping 1", "size": "Size"}
        widgets = {
            'topping1': forms.Textarea,
            'topping2': forms.Textarea,
        }

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)