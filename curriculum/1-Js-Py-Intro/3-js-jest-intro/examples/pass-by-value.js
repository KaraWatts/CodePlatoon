// primitive
let myNumber = 42;

// primitives are 'copy by value', when passed to a function, the function
// gets a copy, changes to the copy don't effect the original
function incrementNumber(num) {
    num = num + 1;
}

incrementNumber(myNumber);

// no change because change was applied to copy only
console.log(myNumber); // 42

// if we wanted this function to actually update the variable 
// we would need to do something like:

function incrementNumberAndReturn(num) {
    return num + 1;
}

myNumber = incrementNumberAndReturn(myNumber);

console.log(myNumber); // 43