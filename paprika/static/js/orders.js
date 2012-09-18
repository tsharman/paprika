$(document).ready(function() {
  //add order btn
  $("#add_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#add_order_dialog").fadeIn(200);
    });
  });
  $(".close_dialog").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });
});
