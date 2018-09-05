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

//   function to prompt the admin to mark order as completed 
function editItems(){
  return confirm("Item has been successfully updated!");
}

//   function to to add items in shopping cart 
function shoppingCart(){
  return confirm("Contains items waiting for checkout!");
}

//   function to to add items by admin 
function addItems(){
  return confirm("Items successfully added!");
}

//   function to place order 
function placeOrder(){
  return confirm("Order successfully placed!");
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

// function to authenticate users and admin
function authenticateUsers(){
  var email = document.querySelector("#email").value;
  var password = document.querySelector("#field").value;
  if(email==='user@gmail.com' && password ==="user123"){
     window.location.href ="home.html";
  }else if(email==='admin@gmail.com' && password ==="admin123"){
    var email = document.querySelector("#email").value;
    var password = document.querySelector("#field").value;
    window.location.href ="admin_home.html";

  }
}
  