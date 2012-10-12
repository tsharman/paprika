$(document).ready(function() {
  $(".close_dialog").click(function() {
    $("#sign_up_dialog").fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

  $("#sign_up_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#sign_up_dialog").fadeIn(200);
    });
  });
});
