// Array Iterations: 8 Methods

// forEach - iterate like enumerate()
[1, 2, 3].forEach(function (item, index) {
  console.log(item, index);
});

// map - takes items, does something, put new thing back into the array
const three = [1, 2, 3];
const doubled = three.map(function (item) {
  return item * 2;
});
console.log(doubled);

// filter - Take an array and check each item in the array to see if it's true or false
// if true goes back in array, else it doesn't
const ints = [1, 2, 3];
const evens = ints.filter(function (item) {
  return item % 2 === 0;
});
console.log(evens);

// reduce - Take an array and do something and pass the resutls in the next iteration along the next item
const sum = [1, 2, 3].reduce(function (result, item) {
  return result + item;
}, 0);
console.log(sum);

// some - Do any number in the array meet this condition?
const hasNegativeNumbers = [1, 2, 3, -1, 4].some(function (item) {
  return item < 0;
});
console.log(hasNegativeNumbers);

// every - Every number must meet the condition
const allPositiveNumbers = [1, 2, -3].every(function (item) {
  return item > 0;
});
console.log(allPositiveNumbers);

// find - goes through all items and check against condition - returns that item if condition is true
// returns undefined if nothing
const objects = [{ id: "a" }, { id: "b" }, { id: "c" }];
const found = objects.find(function (item) {
  return item.id === "e";
});
console.log(found);

// find index - same as find except instead of getting the item, we are getting the index of the item.
// returns -1 if no values are found
const objects2 = [{ id: "a" }, { id: "b" }, { id: "c" }];
const foundIndex = objects2.findIndex(function (item) {
  return item.id === "b";
});
console.log(foundIndex);
