/* Core logic/payment flow for this comes from Stripe docs:
    https://stripe.com/docs/payments/accept-a-paymentm */

// Get stripe_public_key from checkout template
let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);

// Get stripe_public_key from checkout template
let client_secret = $('#id_client_secret').text().slice(1, -1);

// Set up Stripe by creating instance of Stripe and passing public key
let stripe = Stripe(stripe_public_key);

// Create instance of stripe elements
let elements = stripe.elements();

// Set style of card element below
/* CSS from stripe docs: 
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