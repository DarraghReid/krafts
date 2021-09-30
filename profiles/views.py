from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    # Get template to render
    template = 'profiles/profile.html'
    # Create context to access in template
    context = {}

    # Render template with context
    return render(request, template, context)
