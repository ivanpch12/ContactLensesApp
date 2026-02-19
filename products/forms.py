from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Product Name'}),
            'product_type': forms.TextInput(attrs={'placeholder': 'Enter Product Type'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter Product Description'}),
        }
        help_texts = {
            'name': 'Max 100 characters allowed',
            'product_type': 'E.g., Soft, Hard'
        }
        error_messages = {
            'name': {
                'required': 'Please enter the Product Name',
                'max_length': 'Product Name too long',
            }
        }


class ProductCreateForm(ProductForm):
    ...


class ProductEditForm(ProductForm):
    ...


class ProductDeleteForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True