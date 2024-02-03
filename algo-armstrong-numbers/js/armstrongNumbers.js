// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function() {
    numString = num.toString()
    let n = numString.length
    let sum = 0

    for (let i = 0; i < n; i++){
        digit = numString[i]
        sum +=  parseInt(digit)**n
    }


};

console.log(this.findArmstrongNumbers(371))
