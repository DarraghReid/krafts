from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        # Model that form is assossiated with
        model = Order
        # Fields to be rendered (not automatically calculated)
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Override __init__() method
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Call default __init__() method
        super().__init__(*args, **kwargs)
        # Dictionary of placeholders displayed in form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # full_name autofocus attribute set to true, so cursor starts here
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # If the form field is required
            if self.fields[field].required:]
            # Place a star next to it to indicate this
                placeholder = f'{placeholders[field]} *'
            else:
                # Otherwise, there is no star
                placeholder = placeholders[field]
            # Set form placeholder attributes to respective values in placeholder dict above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add stripe-style-input CSS class to each field
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removing label from each field
            self.fields[field].label = False