/**
 * Give index of first matching variable in array
 * @param {any} searchTerm
 * @param {any} arr
 * @returns {any}
 */
function linearSearch(searchTerm, arr) {
  for (let i = 0; i <= arr.length-1; i++){
    if (arr[i]===searchTerm){
      return i
    }
  }
  return undefined;
}

/**
 * Give index of all matches to search term throughout given array
 * @param {any} searchTerm
 * @param {any} arr
 * @returns {any}
 */
function globalLinearSearch(searchTerm, arr) {
  let output = []
  for (let i = 0; i <= arr.length-1; i++){
    if (arr[i]===searchTerm){
      output.push(i)
    }
  }
  if (output.length === 0){
    return undefined;
  }
  return output
}

module.exports = { linearSearch, globalLinearSearch };
