var ana = require("./characterMatch");

// Part 1
console.log(ana.isCharacterMatch('charm', 'march') === true);
console.log(ana.isCharacterMatch('zach', 'attack') === false);
console.log(ana.isCharacterMatch('CharM', 'mARcH') === true);
console.log(ana.isCharacterMatch('abcde2', 'c2abed') === true);

console.log("This test is for the challenge quesiton");
console.log(ana.isCharacterMatch('Anna Madrigal', 'A man and a girl') === true);


// Part 2
listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

console.log(ana.anagramsFor("threads", listOfWords).length == 4);
console.log(ana.anagramsFor("threads", listOfWords)[0] == "threads");
console.log(ana.anagramsFor("threads", listOfWords)[1] == "trashed");
console.log(ana.anagramsFor("threads", listOfWords)[2] == "hardest");
console.log(ana.anagramsFor("threads", listOfWords)[3] == "hatreds");

console.log(ana.anagramsFor("apple", listOfWords).length == 0);
