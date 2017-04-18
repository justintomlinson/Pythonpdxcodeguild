'use strict';

var namesToAges = {
  'Alyssa': 22,
  'Charley': 25,
  'Dan': 25,
  'Jeff': 20,
  'Kasey': 20,
  'Kim': 20,
  'Morgan': 25,
  'Ryan': 25,
  'Stef': 22
};


function useCountBy(invar) {
var values = _.values(invar);
var valueToCount =_.countBy(values);
return _.minBy(values, function(value) {return valueToCount};
);
}
