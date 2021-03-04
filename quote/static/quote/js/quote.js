// Style and handle Checkboxes so they act as radio buttons on document ready.
$(document).ready(function () {
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
