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
  //Hook up delete button to delete dialog 
  $(".delete_btn").click(function(e) {
    e.stopPropagation();
    currentFlow = $(this).parent().parent();
    orderId = $(currentFlow).attr("data-orderid");
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

  //Hook up edit button to this function
  $(".edit_btn").click(function(e) {
    e.stopPropagation();
    currentFlow = $(this).parent().parent();
    orderId = $(currentFlow).attr("data-orderid");
    $.ajax({
      beforeSend : function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
      },
      type : "GET",
      url : "/ajax/edit_order/",
      data : {
        "order_id" : orderId
      },
      async: true,
      success : function(response) {
        console.log(response);
        $("#dialogs").fadeIn(200, function() {
          $("#edit_order_dialog").fadeIn(200);
        });

        $("#edit_order_dialog input[name=order_id]").val(orderId);
        $("#edit_order_dialog input[name=cust_email]").val(response['cust_email']);
        $("#edit_order_dialog input[name=cust_phone]").val(response['cust_phone']);
        $("#edit_order_dialog input[name=cust_name]").val(response['cust_name']);
        $("#edit_order_dialog input[name=notes]").val(response['notes']);
        $("#edit_order_dialog input[name=flow_id]").val(response['flow']);
      },
      error : function(response) {
        console.log(response);
      }
    });
  });

  $(".submit_edit_btn").click(function(e) {
    orderId = $("#edit_order_dialog input[name=order_id]").val();
    cust_email = $("#edit_order_dialog input[name=cust_email]").val();
    cust_phone = $("#edit_order_dialog input[name=cust_phone]").val();
    cust_name= $("#edit_order_dialog input[name=cust_name]").val();
    notes = $("#edit_order_dialog input[name=notes]").val();
    flow_id = $("#edit_order_dialog input[name=flow_id]").val();
    $.ajax({
      beforeSend : function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
      },
      type : "POST",
      url : "/ajax/edit_order/",
      data : {
        "order_id" : orderId,
        "cust_email" : cust_email,
        "cust_name" : cust_name, 
        "cust_phone" : cust_phone, 
        "notes" : notes, 
        "flow" : flow_id,
      },
      async: true,
      success : function(response) {
        console.log(response);
        window.location.replace("/bu/orders/");
        $("#edit_order_dialog").fadeOut(200, function() {
          $("#dialogs").fadeOut(200);
        });
      },
      error : function(response) {
        console.log(response.responseText);
        alert(response.responseText);
      }
    });
  });


  // current state btn
  $(".current_state").click(function(e) {
    state_options = $(this).siblings(".state_options");
    if($(state_options).is(":hidden")) {
      $(".state_options").fadeOut(200);
      $(state_options).fadeIn(200);
    }
    else {
      $(state_options).fadeOut(200);
    }  
  e.stopPropagation();
  });

  $(".state_options .btn").click(function(e) {
    new_state = $(this).attr("data-state");
  
    orderdiv = $(this).parent().parent().parent();
    current_state = $(orderdiv).attr("data-orderstate");
    order_id = $(orderdiv).attr("data-orderid");
    
    if(current_state != new_state) {
      $(this).parent().slideDown(200, function() {
        $(orderdiv).slideUp(200);
      });

      $.ajax({
        beforeSend : function(xhr, settings) {
         xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        type : "POST",
        url : "/ajax/set_state/",
        data : {
          "order_id" : order_id,
          "new_state" : new_state
        },
        async: true,
        success : function(response) {
        },
        error : function(response) {
        }
      });
    }

    e.stopPropagation();
  });
});
