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
 
    stage_form.append("<input type='text' class='title' name='stage_titles' placeholder='Stage title' />"); 
    stage_form.append("<input type='text' class='description' name='stage_descriptions' placeholder='Stage description' />");
    stage_form.append("<div class='btn btn_red remove_stage'>x</div>"); 
   
    container.append(stage_form);
  });
  
  // remove stage
  $(".remove_stage").live('click', function() {
    var stage_form = $(this).parent();
    stage_form.remove();
  });

});
