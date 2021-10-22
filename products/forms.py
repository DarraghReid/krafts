from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Comment


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

    # Set min and max values for rating field
    rating = forms.IntegerField(initial=0, required=False, min_value=0, max_value=5)

    # Override __intit__ method to customize category spelling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all categories
        categories = Category.objects.all()
        # Get each category's friendly name, insert into tuple
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use friendly names in form instead of name field
        self.fields['category'].choices = friendly_names

        # Remove rating label from rating field
        self.fields['rating'].label = "Rate out of 5 : "

        # Add 'border-black rounded-0' classes to match site styles
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class CommentForm(forms.ModelForm):
    """ Create Comment form using Django instead of directly in the HTML.
    CommentForm to be imported and rendered in views.py """

    # Style comment field
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))

    # Meta class defines model and fields
    class Meta:
        # Tell form which model it is associated with
        model = Comment
        # Tell form which fields is should render:
        fields = '__all__'

    # Override __init__() method
    def __init__(self, *args, **kwargs):
        """
        Add placeholder, remove auto-generated
        label and set autofocus
        """
        # Call default __init__() method
        super().__init__(*args, **kwargs)
        # Dictionary of placeholder displayed in form
        placeholders = {
            'comment': 'Comment...',
        }

        # Add stripe-style-input CSS class field
        self.fields['comment'].widget.attrs['class'] = 'stripe-style-input'
        # Remove label from field
        self.fields['comment'].label = False
        # Set form placeholder attributes to respective
        # value in placeholder dict above
        self.fields['comment'].widget.attrs['placeholder'] = placeholders['comment']
