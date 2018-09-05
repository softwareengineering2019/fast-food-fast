  //   function to prompt the admin to delete an item 
  function confirmDelete(){
    return confirm("Are you sure you want to delete this item?");
}

 //   function to prompt the admin to reject an order 
 function confirmReject(){
    return confirm("Order has been rejected!");
}

 //   function to prompt the admin to mark order as completed 
 function confirmComplete(){
    return confirm("Order has been marked as Complete!");
}

// function to search an item by Id number
function myFunction() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }