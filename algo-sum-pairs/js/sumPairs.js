exports.sumPairs = function (numArray, targetSum) {
  let pairsArray = [];

  let index = 0;
  for (let i = 0; i < numArray.length; i += 1) {
    if (i === numArray.length) {
      index += 1;
      i = index;
      continue;
    }
    const sum = numArray[i] + numArray[i + 1];
    if (sum === targetSum) {
      pairsArray.push([numArray[i], numArray[i + 1]]);
    }
  }

  if (pairsArray.length === 0) {
    return "unable to find pairs";
  }
  return pairsArray;
};

console.log(this.sumPairs([1, 2, 3, 4, 5], 9));
