$(document).ready(function() {
  currentSlide = $("#slide2");
  $(document).keydown(function(e) {
    if(e.keyCode == 40 && $(currentSlide).hasClass('slide')) {
      $('html, body').animate({ scrollTop: currentSlide.offset().top + 200 }, { duration : 'slow', easing : 'swing' });
      currentSlide = $(currentSlide).next();
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
