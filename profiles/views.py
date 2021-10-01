from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    # Get user's profile info
    profile = get_object_or_404(UserProfile, user=request.user)

    # If the request method is POST
    if request.method == 'POST':
        # Create new instance of UserProfileForm using POST data
        # to update profile instance above
        form = UserProfileForm(request.POST, instance=profile)

        # If form is valid
        if form.is_valid():
            # Save it
            form.save()
            # Display success message
            messages.success(request, 'Profile updated successfully')

    # Populate form with profile info to send to template
    form = UserProfileForm(instance=profile)
    # Get user's orders to return to template
    orders = profile.orders.all()

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
