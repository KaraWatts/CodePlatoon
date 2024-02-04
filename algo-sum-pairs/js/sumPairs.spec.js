const sumPairs = require("./sumPairs.js");

// Don't forget to add your tests :)

//Single Pair found in string
test('test sumPairs([1, 2, 3, 4, 5], 9) = [[4,5]]', () => {
    expect(sumPairs([1, 2, 3, 4, 5], 9)).toStrictEqual([[4, 5]]);
})
//Miltuple pairs found in string
test('test sum_pairs([1,2,3,4,5], 7) = [[2,5], [3,4]]', () => {
    expect(sumPairs([1,2,3,4,5], 7)).toStrictEqual([[2, 5], [3, 4]]);
})
// No Pairs found in array
test("test sum_pairs([3, 1, 5, 8, 2], 27) = 'unable to find pairs') = [[2,5], [3,4]]", () => {
    expect(sumPairs([3, 1, 5, 8, 2], 27)).toStrictEqual('unable to find pairs');
})

