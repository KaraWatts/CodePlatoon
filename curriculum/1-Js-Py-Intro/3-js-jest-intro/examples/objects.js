// objects can be nested
const database = {
    457: {
        name: "Tom",
        age: 34,
    },
    57782: {
        name: "Sally",
        age: 42,
    },
};

// an objects value can be referenced by key using [] syntax
const tomEntry = database[457];

// if the key is a string, you can also use . syntax
console.log(tomEntry.name); // "Tom"

// You can re-assign a key's value (mutable)
tomEntry.age = tomEntry.age + 1;

// this update changes the value at any reference (mutable)
console.log(database); // { ... 457: { ..., age: 35 } }
