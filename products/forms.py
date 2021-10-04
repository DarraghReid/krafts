from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    # Meta class defines model and fields
    class Meta:
        model = Product
        # Dunder string includes all fields
        fields = '__all__'

    # Replace form image field with image that uses widget
    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    # Override __intit__ method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all categories
        categories = Category.objects.all()
        # Create list of tuples of categories' friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use friendly names in form instead of name field
        self.fields['category'].choices = friendly_names
        # Add 'border-black rounded-0' classes to match site styles
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
