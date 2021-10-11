from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Add a product to the store """


    # If request method is POST
    if request.method == 'POST':
        # Create instance of contact form, capture image file
        form = ContactForm(request.POST)

        # If form is valid
        if form.is_valid():
            # Save it
            # See add_product view for reference on how to redirect user to their messages.
            form.save()

            # Display success message to user
            messages.success(request, 'Message sent successfully!')

            # Redirect to new user's profile
            # See add_product view for reference on how to redirect user to their messages.
            return redirect(reverse('profile'))

        # If form is not valid
        else:
            # Display error message to the user
            messages.error(request, 'Failed to send message. Please ensure the you have provided all the necessary information.')

    # Otherwise
    else:
        # Create instance of product form
        form = ContactForm()

    # Get template to render
    template = 'contact/contact.html'

    # Create context to pass into form
    context = {
        'form': form,
    }

    # Render form along with context
    return render(request, template, context)
