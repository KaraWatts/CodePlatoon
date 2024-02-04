sumPairs = function (numArray, targetSum) {
  let pairsArray = [];


  for (let i = 0; i <= numArray.length; i += 1) {
    for (let j = i + 1; j < numArray.length; j += 1){
      if (numArray[i] + numArray[j] === targetSum) {
        pairsArray.push([numArray[i], numArray[j]]);
      }
    }
  }

  if (pairsArray.length === 0) {
    return "unable to find pairs";
  }
  return pairsArray;
};


console.log(sumPairs([1,2,3,4,5], 7))
module.exports = sumPairs
