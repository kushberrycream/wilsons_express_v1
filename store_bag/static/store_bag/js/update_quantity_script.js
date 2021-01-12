// Update quantity on click
$('.update-link').click(function (e) {
    let form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function (e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('product_size');
    let url = `/bag/remove/${itemId}/`;
    let data = { 'csrfmiddlewaretoken': csrfToken, 'product_size': size };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})

// Remove Elements based on viewport width
jQuery(document).ready(function($) {
  
  let mobileBag  = document.getElementById('mobile-bag');
  let desktopBag = document.getElementById('desktop-bag');
  let bagParent = document.getElementById("bag-parent");
  let alterClass = function() {
    let ww = document.body.clientWidth;
    if (ww <= 751) {
      $(desktopBag).remove();
      $(bagParent).append(mobileBag);
    } else if (ww > 750) {
      
      $(mobileBag).remove();
      $(bagParent).append(desktopBag)
    };
  };
  $(window).resize(function(){
    let itemId = $('.qty_input').data('item_id');  
    alterClass();
    handleEnableDisable(itemId);
  });
  //Fire it when the page first loads:
  alterClass();
  let itemId = $('.qty_input').data('item_id'); 
  handleEnableDisable(itemId); 
});

