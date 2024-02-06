const { toRomanLazy, toRoman } = require("./romanNumerals.js");

console.log(toRomanLazy(4) === "IIII");
console.log(toRomanLazy(150) === "CL");
console.log(toRomanLazy(944) === "DCCCCXXXXIIII");

console.log(toRoman(4) === "IV");
console.log(toRoman(150) === "CL");
console.log(toRoman(944) === "CMXLIV");
