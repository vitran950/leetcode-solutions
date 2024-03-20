/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    const numWord = num.toString();
    let result = "";
    let flip = false;
    for (const c of numWord) {
        if (c === '6' && !flip) {
            flip = true;
            result += '9';
        } else {
            result += c;
        }
    }
    return result;
};