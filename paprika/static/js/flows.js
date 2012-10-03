$(document).ready(function() {
  //add order btn
  $("#add_flow_btn").click(function() {
    $("#dialogs").fadeIn(200, function() {
      $("#add_flow_dialog").fadeIn(200);
    });
  });

  //close the dialog
  $(".close_dialog").click(function() {
    $(this).parent().fadeOut(200, function() {
      $("#dialogs").fadeOut(200);
    });
  });

  // add a stage
  $("#add_stage_btn").click(function() {
    var container = $("#stage_form_list");

    var stage_form = $("<div class='stage_form'></div>");
 
    stage_form.append("<input type='text' class='title' placeholder='Stage title' />"); 
    stage_form.append("<input type='text' class='description' placeholder='Stage description' />");
    
    container.append(stage_form);
  });

});
