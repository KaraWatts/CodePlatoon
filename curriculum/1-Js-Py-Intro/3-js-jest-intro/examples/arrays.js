// Arrays hold an ordered list of values.
// These values can be anything: strings, numbers, objects, even other arrays!
const daysOfTheWeek = ["mon", "tues", "wed"];

// You can access the values in the array by reference to its 'index', which is 0 - based.
daysOfTheWeek[0] = "sun";
console.log(daysOfTheWeek); // ["sun", "tues", "wed"]

// Like strings, arrays have many great methods to help you with manipulating 
// them effectively

const daysOfTheWeek = ["mon", "tues", "wed"];
daysOfTheWeek.push("thurs");
console.log(daysOfTheWeek); // ["mon", "tues", "wed", "thurs"];
