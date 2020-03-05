
var running_list = [];

var record_list_btn = document.querySelector("#sleep_record");
var record_btn = document.querySelector("#record_btn");
var submit = document.querySelector("#submit_record");
var slider = document.querySelector("#hours_slider");
var value_output = document.querySelector("#value_output");

record_btn.onclick = function () {
  var section = document.querySelector("#record_section");
  var hidden_section = document.querySelector("#sleep_record_list");
  hidden_section.style.display = "none";
  section.style.display = "block";
};

record_list_btn.onclick = function () {
  var section = document.querySelector("#sleep_record_list");
  var hidden_section = document.querySelector("#record_section");
  hidden_section.style.display = "none";
  section.style.display = "block";
  loadSleepLog();
};

slider.oninput = function () {
  value_output.innerHTML = this.value;
};

submit.onclick = function () {
  var day_input = document.querySelector("#day_select");
  var day = day_input.value;
  console.log("You chose:", day);
  var hours_input = document.querySelector("#hours_slider");
  var hours = hours_input.value;
  console.log("You chose:", hours);
  var data = "day=" + encodeURIComponent(day)
  + "&" + "hours=" + encodeURIComponent(hours);
  fetch("http://localhost:8080/sleeplogs", {
    method: "POST",
    body: data,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    }
  }).then(function (response) {
    loadSleepLog();
  });
};

function loadSleepLog () {
  fetch("http://localhost:8080/sleeplogs").then(function(response){
    response.json().then (function (listFromServer) {
      running_list = listFromServer;
      var sleep_record_list = document.querySelector("#sleep_record_list");
      sleep_record_list.innerHTML = "";
      running_list.forEach(function (item) {
        console.log("one log:", item);
        var listItem = document.createElement("li");
        listItem.innerHTML = item.day + " you slept: " + item.hours + " hours";
        sleep_record_list.appendChild(listItem);
      });
    });
  });
};
