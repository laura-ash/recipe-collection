/* Date picker */
    $(document).ready(function(){
      var date_input=$('input[name="date_baked"]'); //our date input has the name "date"
      var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
      var options={
        format: 'mm/dd/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
      };
      date_input.datepicker(options);
    })

/* Confirm if recipe should be deleted */

document.getElementById("remove").onclick = function() {
   var check = confirm("Are you sure you want to delete this recipe? This action can't be undone!");
   if (check === true) {
        window.location.href="{{ url_for('delete_recipe', recipe_id=recipe._id )}}"
   } else {
       reload();
   }
}

