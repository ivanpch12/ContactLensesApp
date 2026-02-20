from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'product',
            'status'
        ]
        widgets = {
            'product': forms.CheckboxSelectMultiple(),
        }


class OrderCreateForm(OrderForm):
    ...


class OrderEditForm(OrderForm):
    ...


class OrderDeleteForm(OrderForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
