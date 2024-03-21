/**
 * @param {number[]} cards
 * @return {number}
 */
var minimumCardPickup = function(cards) {
    let set = new Set();
    let left = 0;
    let result = Number.POSITIVE_INFINITY;
    for (let right = 0; right < cards.length; right++) {
        if (set.has(cards[right])) {
            result = Math.min(result, right-left+1);
            while (left < right) {
                if (cards[left] === cards[right]) {
                    result = Math.min(result, right-left+1);
                    break;
                }
                set.delete(cards[left]);
                left++;
            }
        } else {
            set.add(cards[right]);
        }
    }
    
    if (cards.length > 1 && (cards[cards.length-1] === cards[cards.length-2])) {
        return 2;
    }
    return result === Number.POSITIVE_INFINITY ? -1 : result;
};