/**
 * Give nth number in the fibonacci sequence
 * @param {int} num
 * @returns {int}
 */
function fibonacci(num) {
    if (num <= 1){
        return num
    }
    let count = num;
    let fib = 0;
    let arr = [0,1];
    while (count > 1){
        count -= 1;
        fib = arr[0]+arr[1];
        arr = [ arr[1], fib ];
    }

    return fib
}

module.exports = fibonacci;
