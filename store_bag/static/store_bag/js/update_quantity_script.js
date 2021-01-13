// Update quantity on click
$('.update-link').click(function (e) {
    let form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function (e) {
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('product_size');
    let url = `/bag/remove/${itemId}/`;
    let data = { 'csrfmiddlewaretoken': window.csrf_token, 'product_size': size };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})



