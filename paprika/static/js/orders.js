$(document).ready(function() {
  $("#collapse_btn").click(function() {
    if($(".stages").is(":visible")) {
      $(".stages").slideUp(200);
      $(this).text("Expand");
    }
    else {
      $(".stages").slideDown(200);
      $(this).text("Collapse");
    }
  });

  $(".order").click(function() {
    if($(this).children(".stages").is(":hidden")) {
      $(this).children(".stages").slideDown(200);
    }
    else {
      $(this).children(".stages").slideUp(200);
    }
  });
  $(".stages").click(function(e) {
    e.stopPropagation();
  });

  //add order btn
  $("#add_order_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#add_order_dialog").fadeIn(200);
    });
  });

  //close the dialog
  $(".close_dialog, .close").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

  //hover over stages
  $(".stage").hover(function() {
    if(!$(this).hasClass('active')) {
      $(this).children(".status_bar").css("background-color", "#ff835d");
      $(this).children(".stage_title").hide();
      $(this).children(".start_here").show();
    }
  }, function() {
    if(!$(this).hasClass('active')) {
      $(this).children(".status_bar").css("background-color", "#888");
      $(this).children(".start_here").hide();
      $(this).children(".stage_title").show();
    }
  });

  // click stage to update position
  $(".stage").click(function() {
    if(!$(this).children('.status_bar').hasClass('active')) {
      // retreiving order id
      order_id = $(this).parent().parent().attr("data-orderid");
       
      // +1 because stage_nums start at 1
      stage_index = $(this).attr("data-stageid");

      //removing previous current stage
      $(this).siblings(".active").removeClass("active");

      //applying styling
      $(this).addClass("active"); 
      $(this).children(".status_bar").attr("style", "");  
 
      // making hte ajax request
      // beforeSend adds the CSRF token to the request header
      $.ajax({
        beforeSend : function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        type : "POST",
        url : "/ajax/move_stage/",
        data : {
          "stage_index" : stage_index,
          "order_id" : order_id,
        },
        async : true,
        success : function(response) {
          console.log(response);
        },
        error : function(response) {
          console.log(response);
        }
      });
    }
  });
  
  $(".delete_btn").click(function(e) {
    e.stopPropagation();
    currentFlow = $(this).parent().parent();
    $("#dialogs").fadeIn(200, function() {
      $("#delete_order_dialog").fadeIn(200);
    });
  });

  // yes delete buttn
  $("#yes_delete_btn").click(function() {
    orderId = $(currentFlow).attr("data-orderid");
    $.ajax({
      beforeSend : function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
      },
      type : "POST",
      url : "/ajax/delete_order/",
      data : {
        "order_id" : orderId
      },
      async: true,
      success : function(response) {
        console.log(response);
      },
      error : function(response) {
        console.log(response);
      }
    });

    $("#delete_order_dialog").fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
    
    $(currentFlow).delay(400).slideUp(200);

  });


  // current state btn
  $(".current_state").click(function(e) {
    state_options = $(this).siblings(".state_options");
    if($(state_options).is(":hidden")) {
      $(state_options).fadeIn(200);
    }
    else {
      $(state_options).fadeOut(200);
    }  
  e.stopPropagation();
  });


});
