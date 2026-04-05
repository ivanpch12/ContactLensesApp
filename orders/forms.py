from django import forms
from orders.models import Order


class OrderCreateFullForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']
        widgets = {
            'product': forms.CheckboxSelectMultiple(),
        }


class OrderCreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']
        widgets = {
            'product': forms.CheckboxSelectMultiple(),
        }


class OrderDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


class OrderFullForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'status']


class OrderCustomerForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']