// complex
let myObject = { name: "Tom", age: 34 };

// obj is 'copy by reference', changes to it will effect what was passed in
function incrementObjectAge(obj) {
    obj.age = obj.age + 1;
}

incrementObjectAge(myObject);

console.log(myObject); // { name: "Tom", age: 35 };

// If we didn't want this behavior, we would have to make a local 
// copy in the function, like so:

function incrementObjectAgeImmutable(obj) {
    const objCopy = Object.assign({}, obj); // helper function to create a new object, copy everything over
    objCopy.age = obj.age + 1;
    return objCopy;
}

const newObject = incrementObjectAgeImmutable(myObject);

// preserved original
console.log(myObject); // { name: "Tom", age: 35 };

// updated object
console.log(newObject); // { name: "Tom", age: 36 };