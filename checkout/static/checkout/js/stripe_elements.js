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

    // Trigger loading-overlay css
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Get user's save info preference
    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Object to send data to cache_checkout_data() to update payment intent
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // Create url to send data to cache_checkout_data() to update payment intent
    let url = '/checkout/cache_checkout_data/';

    // Post data to cache_checkout_data() to update payment intent
    // .done() ensures payment intent updated before confirmCardPayment() called
    $.post(url, postData).done( function() {
        // Use stripe.confirmCardPayment() to send card info securely to Stripe
        stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            // Provide card to Stripe
            card: card,
            // Get billing details from form
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        // In case user has different billing/shipping info
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address:{
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
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

                // Hide loading-overlay css
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);

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
    }).fail(function () {  // In case view sends back 400 request response
        // just reload the page, the error will be in django messages
        // User will not be charged
        location.reload();
    })    
});