'use strict';

function Completer() {
//Completer is basic constructor with no arguments
  this.elemList = [];
  this.addCompletion = function(str) {
    //Appends a word to an array
    var userInput = str;
    this.elemList.push(userInput);
  };
  this.removeCompletion = function(str) {
    /*finds the index of a string and removes it from the array using
    splice*/
    var removeWord = str;
    var index = this.elemList.indexOf(removeWord);
    if(index > -1) {
      this.elemList.splice(index, 1);
    }
  };
  this.complete = function(prefix) {
    /* this function takes the an entered prefix string then checks elemList for
    strings that that start with that prefix and returns a list of valid words*/
    var prefix = prefix;
    var returnList = [];
    for(var i in this.elemList) {
      var index = this.elemList[i].indexOf(prefix,0);
      if(index === 0) {
        returnList.push(this.elemList[i]);
      }
    } return returnList;
  };
}


//Test block for Completer
var x = new Completer();
//Adds worsds to elemList
x.addCompletion('apple');
x.addCompletion('banana');
x.addCompletion('avocado');
x.addCompletion('orange');
//removes a string (banana) from elemList
x.removeCompletion('banana');
//creates output list of words starting with 'a'
var finList = x.complete('a');

console.log(x.elemList);
console.log(finList);
