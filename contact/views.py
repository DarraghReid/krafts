from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Add a product to the store """

    # If request method is POST
    if request.method == 'POST':
        # Create instance of contact form
        form = ContactForm(request.POST)

        # If form is valid
        if form.is_valid():
            # Save it
            form.save()

            # Display success message to user
            messages.success(request, 'Message sent successfully!')

            # Store user's information for confirmation email
            sender = request.POST['full_name']
            sender_email = request.POST['email']
            message = request.POST['message']

            # Subject of confirmation email
            subject = 'Message Received'

            # Confirmation of receipt of message
            confirmation_message = f"""Dear {sender},
            Thank you for contacting us!
            One of our team will be in contact with you shortly shortly.
            Your message:
            '{message}'
            Kind Regards,
            Krafts.
            """

            # Send email to user informing them that their message has been sent
            send_mail(
                subject,
                confirmation_message,
                sender_email,
                [settings.DEFAULT_FROM_EMAIL],
            )

            # Redirect to new user's profile
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
