var expanded_4 = false;
var expanded_3 = false;
var expanded_3_2 = false;


function checkboxes_str4() {
  var checkboxes_str4 = document.getElementById("checkboxes_str4");
  if (!expanded_4) {
    checkboxes_str4.style.display = "block";
    expanded_4 = true;
  } else {
    checkboxes_str4.style.display = "none";
    expanded_4 = false;
  }
}

function checkboxes_str3() {
  var checkboxes_str3 = document.getElementById("checkboxes_str3");
  if (!expanded_3) {
    checkboxes_str3.style.display = "block";
    expanded_3 = true;
  } else {
    checkboxes_str3.style.display = "none";
    expanded_3 = false;
  }
}

function checkboxes_str3_2() {
    var checkboxes_str3_2 = document.getElementById("checkboxes_str3_2");
    if (!expanded_3_2) {
        checkboxes_str3_2.style.display = "block";
      expanded_3_2 = true;
    } else {
        checkboxes_str3_2.style.display = "none";
      expanded_3_2 = false;
    }
  }