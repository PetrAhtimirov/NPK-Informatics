function validate(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode( key );
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }

let onSubmit = function(event) {
  event.preventDefault();
}

let form = document.querySelector("form")
form.addEventListener('submit', onSubmit);

let createtext = function () {
  let textarea = document.getElementById("textar")
  textarea.classList.remove("zero-opacity")
}