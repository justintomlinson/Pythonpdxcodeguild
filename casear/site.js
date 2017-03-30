'use strict';
function caesarEncrypt(plainStr, key) {
	if (key < 0) {
		return caesarEncrypt(plainStr, key + 26);
}
  var output = '';
  for (var i = 0; i < plainStr.length; i ++) {
    var char = plainStr[i];
    var code = char.charCodeAt(0);
    if ((code >= 65) && (code <= 90)) {
				code = String.fromCharCode((code - 65 + key)% 26 + 65);
      }
	  output += code;
  }
	return output;
}

function caesarDecrypt(encStr, key) {
  if (key< 0){
    return caesarDecrypt(encStr, key + 26);
  }
  var x = 0;
  var orig = '';
  for (var i = 0; i < encStr.length; i++) {
    var char = encStr[i];
    var num= char.charCodeAt(0);
    if((num >= 65) && (num <= 90)) {
      num = String.fromCharCode((num - 65 - key + 26)% 26 +65);
    }
    orig += num;
  }
  return orig;
}



caesarEncrypt('BYE', 2); // DAG

caesarDecrypt('DAG', 2); //BYE
