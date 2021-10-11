from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Create Product form using Django instead of directly in the HTML.
        ProductForm to be imported and rendered in views.py """

    # Meta class defines model and fields
    class Meta:
        # Tell form which model it is associated with
        model = Product
        # Tell form which fields is should render:
        # Dunder string includes all fields
        fields = '__all__'

    # Replace form image field with image that uses widget
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput)

    # Override __intit__ method to customize category spelling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all categories
        categories = Category.objects.all()
        # Get each category's friendly name, insert into tuple
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use friendly names in form instead of name field
        self.fields['category'].choices = friendly_names
        # Add 'border-black rounded-0' classes to match site styles
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
