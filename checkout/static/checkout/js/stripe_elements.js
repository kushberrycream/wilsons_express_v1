let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
  base: {
    color: '#000',
    fontFamily: '"Montserrat", sans-serif',
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
let cardNumber = elements.create('cardNumber', {
  style: style, placeholder: 'Card Number',
});
let cardExpiry = elements.create('cardExpiry', { style: style });
let cardCvc = elements.create('cardCvc', { style: style });
cardNumber.mount('#card-number-element');
cardExpiry.mount('#card-expiry-element');
cardCvc.mount('#card-cvc-element');

// Handle realtime validation errors on the card element
cardNumber.addEventListener('change', function (event) {
  let errorDiv = document.getElementById('card-errors');
  if (event.error) {
    let html = `<span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>`;
    $(errorDiv).html(html);

  } else {
    errorDiv.textContent = '';
  }
});

cardExpiry.addEventListener('change', function (event) {
  let errorDiv = document.getElementById('card-errors');
  if (event.error) {
    let html = `<span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>`;
    $(errorDiv).html(html);

  } else {
    errorDiv.textContent = '';
  }
});

// Handle form submit
let form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  cardNumber.update({ 'disabled': true });
  cardExpiry.update({ 'disabled': true });
  cardCvc.update({ 'disabled': true });
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: cardNumber,
    }
  }).then(function (result) {
    if (result.error) {
      let errorDiv = document.getElementById('card-errors');
      let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
      $(errorDiv).html(html);
      cardNumber.update({ 'disabled': false });
      cardExpiry.update({ 'disabled': false });
      cardCvc.update({ 'disabled': false });
      $('#submit-button').attr('disabled', false);
    } else {
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
      }
    }
  });
});
