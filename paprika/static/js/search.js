$(document).ready(function() {
//close the dialog
  $(".close_dialog, .close").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

 
  $(".feed_btn").click(function(e) {
    orderdiv = $(this).parent();
    order_id = $(orderdiv).attr("data-orderid"); 
    $.ajax({
      beforeSend : function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
      },
      type : "GET",
      url : "/ajax/feed/",
      data : {
        "order_id" : order_id,
      },
      async: true,
      success : function(response) {
        $("#feed_list").html(response)
      },
      error : function(response) {
      }
    });
    $("#dialogs").fadeIn(200, function() {
      $("#feed_dialog").fadeIn(200);
    });
    e
  });
});
