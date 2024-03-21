/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    let hashmap = new Map();
    for (const num of nums) {
        const converted = num.toString().split('').reduce((a,b) => parseInt(a) + parseInt(b), 0);
        if (!hashmap.has(converted)) {
            hashmap.set(converted, []);
        }
        hashmap.get(converted).push(num);
    }
    
    result = -1;
    for (const arr of hashmap.values()) {
        if (arr.length > 1) {
            arr.sort((a,b) => b-a);
            result = Math.max(result, arr[0]+arr[1]);
        }
    }
    return result;
};