from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Render all fields except for user field
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Call default __init__() method
        super().__init__(*args, **kwargs)
        # Dictionary of placeholders displayed in form fields
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # default_phone_number autofocus attrib = true, so cursor starts here
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Ensure that code doesn't seek 'default_country' field
            if field != 'default_country':
                # If the form field is required
                if self.fields[field].required:
                    # Place a star next to it to indicate this
                    placeholder = f'{placeholders[field]} *'
                else:
                    # Otherwise, there is no star
                    placeholder = placeholders[field]
                # Set form placeholder attributes to respective
                # values in placeholder dict above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add site-appropriate CSS class to each field
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            # Remove label from each field
            self.fields[field].label = False
