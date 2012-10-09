$(document).ready(function() {
  //add order btn
  $("#add_order_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#add_order_dialog").fadeIn(200);
    });
  });

  //close the dialog
  $(".close_dialog").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

  //hover over stages
  $(".stage").hover(function() {
    if(!$(this).children('.status_bar').hasClass('active')) {
      $(this).children(".status_bar").css("background-color", "#ff835d");
      $(this).children(".stage_title").hide();
      $(this).children(".start_here").show();
    }
  }, function() {
    if(!$(this).children('.status_bar').hasClass('active')) {
      $(this).children(".status_bar").css("background-color", "#888");
      $(this).children(".start_here").hide();
      $(this).children(".stage_title").show();
    }
  });
});
