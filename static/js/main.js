// 
$(document).ready(function () {
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



