function toRomanLazy(num) {
  const conversionObject = {
    M : 1000,
    D : 500,
    C : 100,
    L : 50,
    X : 10,
    V : 5,
    I : 1
  }
  let result = ""
  for (let key in conversionObject){
    if (conversionObject[key] <= num){
      const iteration = Math.floor(num/conversionObject[key]);
      for (let i = 0; i < iteration; i++){
        result += key
      }
      num -= conversionObject[key]*iteration
    }
  }
  return result
}


function toRoman(num) {
  const conversionObject = {
    M : 1000,
    CM : 900,
    D : 500,
    CD : 400,
    C : 100,
    L : 50,
    XL : 40,
    X : 10,
    IX : 9,
    V : 5,
    IV : 4,
    I : 1
  }
  let result = ""
  for (let key in conversionObject){
    if (conversionObject[key] <= num){
      const iteration = Math.floor(num/conversionObject[key]);
      for (let i = 0; i < iteration; i++){
        result += key
      }
      num -= conversionObject[key]*iteration
    }
  }
  return result
}

module.exports = { toRoman, toRomanLazy };
