/**
 * Calculate Factorial of given integer
 * @param {int} num
 * @returns {int}
 */
function factorial(num) {
  if (num == 0){
    return 1
  }
  return num * factorial(num-1)
}

module.exports = factorial;
