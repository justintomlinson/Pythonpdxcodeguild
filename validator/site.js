'use strict';
//$('.error').hide();

function checkNameFormat(userInput) {
  /* This function checks the format of a name text entry with a space
  between the first and second name (ex First Last). The text box will be
   highlighted yellow until the entry is acceptable*/
  var alphaExp = /^[A-Za-z]+ +[A-Za-z]+$/;
  if(userInput.match(alphaExp)) {
    $('#nametext').css('background-color', 'white');
    //$('.error').hide().focus();
    return true;
  }else {
    //$('.error').show();
    $('#nametext').css('background-color', 'yellow');
    return false;
  }
}
/*  ('#nametext').keypress(function(){

});*/

function checkphoneFormat(userInput) {
  /*This function checks the format on an enter phone number with the desired
  entry as ###-###-####. The text box will be highlighted yellow until the entry
  is acceptable */
  var phoneExp = /^(\d\d\d)-(\d\d\d)-(\d\d\d\d)+$/;
  //$('.error').hide();
  if(userInput.match(phoneExp)) {
    $('#phonetext').css('background-color', 'white');
    return true;
  }else {
    $('#phonetext').css('background-color', 'yellow');
    return false;
  }
}

function checkbirthdateFormat(userInput) {
  /*This function checks the format on an enter a birthdate with the desired
  entry as YYYY-MM-DD. The text box will be highlighted yellow until the entry
  is acceptable */
  var dobExp = /^(\d\d\d\d)-(\d\d)-(\d\d)$/;
  //$('.error').hide();
  if(userInput.match(dobExp)) {
    $('#dobtext').css('background-color','white');
    return true;
  }else {
    $('#dobtext').css('background-color', 'yellow');
    return false;
  }
}
/*$( "input[type=text]" ).focus(function() {
  $( this ).bl
  ur();
});*/
$('#nametext').on('input',function() {
  var nameInput = $('#nametext').val();
  checkNameFormat(nameInput);
});

$('#dobtext').on('input', function() {
  var dobInput = $('#dobtext').val();
  checkbirthdateFormat(dobInput);
});

$('#phonetext').on('input', function() {
  var phoneInput = $('#phonetext').val();
  checkphoneFormat(phoneInput);
});
