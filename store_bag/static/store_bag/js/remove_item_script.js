// Remove item and reload on click
$('.remove-item').click(function (e) {
    let itemId = $(this).attr('id').split('remove_')[1];
    let url = `/bag/remove/${itemId}/`;
    let csrf = document.getElementsByTagName("meta")[7].content;
    let data = { 'csrfmiddlewaretoken': csrf};

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})



