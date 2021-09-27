/*  Create stripe elements & insert into checkout.html
    Core logic/payment flow for this comes from Stripe docs:
    https://stripe.com/docs/payments/accept-a-paymentm */

// Get stripe_public_key from checkout template
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);

// Get stripe_public_key from checkout template
let clientSecret = $('#id_client_secret').text().slice(1, -1);

// Set up Stripe by creating instance of Stripe and passing public key
let stripe = Stripe(stripePublicKey);

// Create instance of stripe elements
let elements = stripe.elements();

/*  Set style of card element below
    CSS from stripe docs: 
    https://stripe.com/docs/stripe-js */

let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Use stripe elements to create card element
let card = elements.create('card', {style: style});

// Mount card element to card-element div in checkout.html
card.mount('#card-element');

/* Handle realtime validation errors on the card element */

// Listen for change event on the card element
card.addEventListener('change', function (event) {
    // Save card-errors div to error-div variable to display errors from card element
    let errorDiv = document.getElementById('card-errors');
    // If there is an error from the card element
    if (event.error) {
        // Create html to display the error
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        // Insert the html error into card-errors div
        $(errorDiv).html(html);
    } else {
        // Otherwise, card-error div is blank
        errorDiv.textContent = '';
    }
});

/* Handle form submit */

// Save form to form variable
let form = document.getElementById('payment-form');

// On form submit:
form.addEventListener('submit', function(ev) {
    // Prevent form's default action (to post)
    ev.preventDefault();

    // Prevent multiple submissions by disabling card element & submit btn
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // Use stripe.confirmCardPayment() to send card info securely to Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            // Provide card to Stripe
            card: card,
        }
        // Execute the following function on the result of calling confirmCardPayment()
    }).then(function(result) {
        // If there is an error in payment
        if (result.error) {
            // Get card-errors div
            let errorDiv = document.getElementById('card-errors');
            // Create html to display error
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            // Insert the html error into card-errors div
            $(errorDiv).html(html);
            // Re-enable card element & submit btn to allow user to fix error
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // If payment has succeeded
            if (result.paymentIntent.status === 'succeeded') {
                // Submit the form
                form.submit();
            }
        }
    });
});