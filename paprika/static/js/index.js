$(document).ready(function() {
  currentSlide = $("#heading");
  $(document).keydown(function(e) {
    if(e.keyCode == 40) {
      if($(currentSlide).next().hasClass('slide')) {
        currentSlide = $(currentSlide).next();
      }
      $('html, body').animate({ scrollTop: currentSlide.offset().top + 200 }, { duration : 'slow', easing : 'swing' });
    }
    else if(e.keyCode == 38) {
      if($(currentSlide).prev().hasClass('slide')) {
        currentSlide = $(currentSlide).prev();
      }
      $('html, body').animate({ scrollTop: currentSlide.offset().top + 200 }, { duration : 'slow', easing : 'swing' });
    }
  });
  
  $(".close_dialog").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

  $("#sign_up_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#sign_up_dialog").fadeIn(200);
    });
  });
  $("#login_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#login_dialog").fadeIn(200);
    });
  });
});
