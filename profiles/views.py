from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Django checks if user logged in before executing view
# If not, user is redirected to login page
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """

    # Get user's profile info
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # If the request method is POST
    if request.method == 'POST':
        # Create new instance of UserProfileForm using POST data
        # to update profile instance above
        form = UserProfileForm(request.POST, instance=user_profile)

        # If form is valid
        if form.is_valid():
            # Save it
            form.save()

            # Display success message
            messages.success(request, 'Profile updated successfully')

        # If form is not valid
        else:
            # Display error message to the user
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    # Otherwise
    else:
        # Populate form with profile info to send to template
        form = UserProfileForm(instance=user_profile)

    # Get user's orders to return to template
    orders = user_profile.orders.all()

    # Get template to render
    template = 'profiles/profile.html'

    # Create context to access in template
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    # Render template with context
    return render(request, template, context)


def order_history(request, order_number):
    """
    Retrieve and dispaly user's order history
    """
    # Retrieve order
    order = get_object_or_404(Order, order_number=order_number)

    # Inform user this is a historic transaction
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Use checkout_success.html template to render order history
    template = 'checkout/checkout_success.html'

    # Create context to access in template
    context = {
        'order': order,
        # Determine if checkout_success.html accessed through order_history
        'from_profile': True,
    }

    # Render template with context
    return render(request, template, context)
