// script to send user back to top of page
$('.btt-link').click(function (e) {
  window.scrollTo(0, 0)
})

// display toasts
$('.toast').toast('show');

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


$( '#sending-links' ).prepend( '<a href="/delivery/quote/" class="dropdown-item">Send a Parcel</a>' );
