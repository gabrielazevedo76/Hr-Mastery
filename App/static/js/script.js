/* --------------------------
# FULL VALIDATION FORM
-----------------------------*/

// 1) Inputmask (PHONE)
$(document).ready(function() {
  $(".phone").inputmask("(99) 99999-9999", {"onincomplete": function(){
    $(".phone").val("");
    swal("Opss !", "Incomplete phone. Please review !", "info");
    return false;
  }})
})

// 2) INPUT VALIDATION
// a) Frontend form
function validadeEmail(email) {
  const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function validateForm() {
  const name = document.getElementById("name").value;
  const age = document.getElementById("age").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const address = document.getElementById("address").value;
  const experience = document.getElementById("experience").value;
  const skills = document.getElementById("skills").value;
  const file = document.getElementById("file").value;

  if(name == ""){
    swal("Opss !", "Name field cannot be empty.", "error");
    return false;
  }
  else if (age == ""){
    swal("Opss !", "Age field cannot be empty.", "error");
    return false;
  }
  else if (email == ""){
    swal("Opss !", "Email field cannot be empty.", "error");
    return false;
  }
  else if (phone == ""){
    swal("Opss !", "Phone field cannot be empty.", "error");
    return false;
  }
  else if (address == ""){
    swal("Opss !", "Address field cannot be empty.", "error");
    return false;
  }
  else if (experience == ""){
    swal("Opss !", "Experience field cannot be empty.", "error");
    return false;
  }
  else if (skills == ""){
    swal("Opss !", "Skills field cannot be empty.", "error");
    return false;
  }
  else if (file == ""){
    swal("Opss !", "File field cannot be empty.", "error");
    return false;
  }
  else {
    return true;
  }
}
