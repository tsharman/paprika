$(document).ready(function() {
  //add order btn
  $("#add_btn").click(function() {
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
    $(this).children(".status_bar").css("background-color", "#54c56f");
    $(this).children(".stage_title").slideUp(100, function() {
      $(this).siblings(".start_here").slideDown(100);
    });
  }, function() {
    $(this).children(".status_bar").css("background-color", "#888");
    $(this).children(".start_here").slideUp(100, function() {
      $(this).siblings(".stage_title").slideDown(100);
    });
  });
});
