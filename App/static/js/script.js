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
function validateEmail(email) {
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
  else if (name == name.toUpperCase()){
    document.getElementById('name').value='';
    swal("Opss !", "Name field cannot be UPPERCASE.", "info");
    return false;
  }
  else if (name.split(' ').length < 2){
    document.getElementById('name').value='';
    swal("Opss !", "Your full name in required.", "info");
    return false;
  }
  else if (age == ""){
    swal("opss !", "age field cannot be empty.", "error");
    return false;
  }
  else if ((age < 18) || (age > 50)){
    swal("Opss !", "This job requires you to be between 18 and 50 years old.", "info");
    return false;
  }
  else if (email == ""){
    swal("Opss !", "Email field cannot be empty.", "error");
    return false;
  }
  else if (!(validateEmail(email))){
    document.getElementById('email').value='';
    swal("Opss !", "Put a valid email address.", "info");
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

// b) Backend form
function validateEmail2(email) {
  const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function validateForm2() {
  const name = document.getElementById("name2").value;
  const age = document.getElementById("age2").value;
  const email = document.getElementById("email2").value;
  const phone = document.getElementById("phone2").value;
  const address = document.getElementById("address2").value;
  const experience = document.getElementById("experience2").value;
  const skills = document.getElementById("skills2").value;
  const file = document.getElementById("file2").value;

  if(name == ""){
    swal("Opss !", "Name field cannot be empty.", "error");
    return false;
  }
  else if (name == name.toUpperCase()){
    document.getElementById('name2').value='';
    swal("Opss !", "Name field cannot be UPPERCASE.", "info");
    return false;
  }
  else if (name.split(' ').length < 2){
    document.getElementById('name2').value='';
    swal("Opss !", "Your full name in required.", "info");
    return false;
  }
  else if (age == ""){
    swal("opss !", "age field cannot be empty.", "error");
    return false;
  }
  else if ((age < 18) || (age > 50)){
    swal("Opss !", "This job requires you to be between 18 and 50 years old.", "info");
    return false;
  }
  else if (email == ""){
    swal("Opss !", "Email field cannot be empty.", "error");
    return false;
  }
  else if (!(validateEmail2(email))){
    document.getElementById('email2').value='';
    swal("Opss !", "Put a valid email address.", "info");
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

// c) Fullstack form
function validateEmail3(email) {
  const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function validateForm3() {
  const name = document.getElementById("name3").value;
  const age = document.getElementById("age3").value;
  const email = document.getElementById("email3").value;
  const phone = document.getElementById("phone3").value;
  const address = document.getElementById("address3").value;
  const experience = document.getElementById("experience3").value;
  const skills = document.getElementById("skills3").value;
  const file = document.getElementById("file3").value;

  if(name == ""){
    swal("Opss !", "Name field cannot be empty.", "error");
    return false;
  }
  else if (name == name.toUpperCase()){
    document.getElementById('name3').value='';
    swal("Opss !", "Age field cannot be UPPERCASE.", "info");
    return false;
  }
  else if (name.split(' ').length < 2){
    document.getElementById('name3').value='';
    swal("Opss !", "Your full name in required.", "info");
    return false;
  }
  else if (age == ""){
    swal("opss !", "age field cannot be empty.", "error");
    return false;
  }
  else if ((age < 18) || (age > 50)){
    swal("Opss !", "This job requires you to be between 18 and 50 years old.", "info");
    return false;
  }
  else if (email == ""){
    swal("Opss !", "Email field cannot be empty.", "error");
    return false;
  }
  else if (!(validateEmail3(email))){
    document.getElementById('email3').value='';
    swal("Opss !", "Put a valid email address.", "info");
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

// 3) Maximum allowed upload size
$(document).ready(function(){
  $("#file, #file2, #file3").bind('change', function(){
    var a = (this.files[0].size);

    if (a > 2 * 1048576){
      swal("Attention!", "Maximum allowed size id 2mb", "info");
      this.value = "";
    };
  });
});

// 4) Allow only letters in Name
$(".name").keyup(function() {
  if (!/^[a-zA-Z _]*$/.test(this.value)) {
    this.value = "";
  }
})

// 5) Prevent more than 2 white spaces inside the input NAME
$(".name").on('keydown', function(){
  var $this = $(this);
  $(this).val($this.val().replace(/(\s{2,})|[^a-zA-Z0-9_']/g, ' ').replace(/^\s*/, ''));
})

// 6) Prevent starting with space in all inputs (including textarea)
$("input[type='text'], textarea").on("keypress", function(e){
  if(e.which === 32 && ! this.value.length)
  e.preventDefault();
});

// 7) Allow only numbers in AGE
$(".age").keyup(function(){
  if(!/^[0-9]*$/.test(this.value)) {
    this.value = "";
  }
});

// 8) if AGE is greater than 50, auto clear
$(".age").keyup(function(){
  if ( ((this.value) > 50)) {
    this.value = "";
  }
});

// 9) Prevent startting by zero in AGE field
$(".age").on("input", function () {
  if(/^0/.test(this.value)) {
    this.value = this.value.replace(/^0/, "")
  }
});

// 10) Script to LOWERCASE input email
$(document).ready(function() {
  $(".email").keyup(function() {
    this.value = this.value.toLowerCase();
  })
});