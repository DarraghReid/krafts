from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    # Get template to render
    template = 'profiles/profile.html'
    # Create context to access in template
    context = {
        'profile': profile,
    }

    # Render template with context
    return render(request, template, context)
