// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(numberArray) {
    armstrongNumbers = []
    numberArray.forEach( num => {
        numString = num.toString();
        let n = numString.length;
        let sum = 0;

        for (let i = 0; i < n; i++){
            digit = numString[i];
            sum +=  parseInt(digit)**n;
        }
        if (num === sum){
            armstrongNumbers.push(sum);
        }
    })   
    return armstrongNumbers;
};

// console.log(this.findArmstrongNumbers([343, 371]))
