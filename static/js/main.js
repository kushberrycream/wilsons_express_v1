$(document).ready(function () {
  $('<a href="/delivery/quote/" class="dropdown-item">Send a Parcel</a>').insertAfter(".dropdown-item.account");
  $( '#home_quote' ).removeClass( 'd-none' )
  $( '#dark-overlay' ).removeClass( 'h-100' )
});

// script to send user back to top of page
$('.btt-link').click(function (e) {
  window.scrollTo(0, 0)
});


//add tooltips from bootstrap documentation
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
$(function () {
  $(document).on('shown.bs.tooltip', function (e) {
    setTimeout(function () {
      $(e.target).tooltip('hide');
    }, 750);
  });
});



