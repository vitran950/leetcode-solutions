/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let hash = new Set();
    for (const num of nums) {
        if (hash.has(num)) {
            return num
        }
        hash.add(num);
    }    
};