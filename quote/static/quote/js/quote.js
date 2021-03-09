// Style and handle Checkboxes so they act as radio buttons on document ready.
$(document).ready(function () {
  $("#quote-form").submit(function (e) {
    $('#loading-overlay').fadeToggle(100);
  })

  $("#div_id_service").children('div').addClass("d-flex flex-row flex-wrap service");
  $(".d-flex.flex-row.service").children().children('input').addClass("time m-3");
  $(".d-flex.flex-row.service").children('div').addClass("m-3");
  $('input.time').on('change', function () {
    $('input.time').not(this).prop('checked', false);
  });


  $("#div_id_spec_service").children('div').addClass("d-flex flex-row flex-wrap special");
  $(".d-flex.flex-row.special").children().children('input').addClass("special m-3");
  $(".d-flex.flex-row.special").children('div').addClass("m-3");
  $('input.special').on('change', function () {
    $('input.special').not(this).prop('checked', false);
  });


  if ($('#id_spec_service_4').prop("checked") == true) {
    $("#id_service_3").attr("disabled", true);
    if ($('#id_service_3').prop("checked", false)) {
      $('#id_service_3').removeAttr('checked');
    }
  }


  if ($( "#item_2" ).hasClass("d-none")) {
        $("#less_items").prop('disabled', true);
  }

  $("#more_items").click(function () {
    $('.d-none.justify-content-around.row:first').addClass('d-flex').removeClass('d-none');
    if ($( "#item_5" ).hasClass("d-flex")) {
        $("#more_items").prop('disabled', true);
    }
    if ($( "#item_2" ).hasClass("d-flex")) {
        $("#less_items").prop('disabled', false);
    }
  });
  $("#less_items").click(function () {
    $('.justify-content-around.d-flex:last').addClass('d-none').removeClass('d-flex');
    if ($( "#item_5" ).hasClass("d-none")) {
        $("#more_items").prop('disabled', false);
    }
    if ($( "#item_2" ).hasClass("d-none")) {
        $("#less_items").prop('disabled', true);
    }
  });

  $('.input-group-append').children('span').addClass('stripe-style-input small').removeClass('input-group-text');
  // on() method to attatch the on click and on change event handlers.
  $('#services').on("click change", function (e) {
    if (e.type === "click") {
      if ($('#id_spec_service_3').prop("checked") == true) {
        $("#id_service_3").removeAttr("disabled");
      } else if ($('#id_spec_service_2').prop("checked") == true) {
        $("#id_service_3").removeAttr("disabled");
      } else if ($('#id_spec_service_1').prop("checked") == true) {
        $("#id_service_3").removeAttr("disabled");
      }

    }
    if ($('#id_spec_service_4').prop("checked") == true) {
      $("#id_service_3").attr("disabled", true);
      if ($('#id_service_3').prop("checked", false)) {
        $('#id_service_3').removeAttr('checked');
      }
    } else {
      $("#id_service_3").removeAttr("disabled");
    }
  });

});

