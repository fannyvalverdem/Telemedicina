function myFunction() {
  var checkBox = document.getElementById("id_lunes");
  var text = document.getElementById("horario");
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
     text.style.display = "none";
  }
}