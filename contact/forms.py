from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        # Model that form is assossiated with
        model = Message
        # Fields to be rendered
        fields = '__all__'

    # Override __init__() method
    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels and set autofocus on first field
        """
        # Call default __init__() method
        super().__init__(*args, **kwargs)
        # Dictionary of placeholders displayed in form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message (max 500 characters)',
        }

        # full_name autofocus attribute set to true, so cursor starts here
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Place a star next to placeholder to indicate field is required
            placeholder = f'{placeholders[field]} *'
            # Set form placeholder attributes to respective
            # values in placeholder dict above
            self.fields[field].widget.attrs['placeholder'] = placeholder
        # Add stripe-style-input CSS class to each field
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        # Remove label from each field
        self.fields[field].label = False