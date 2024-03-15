/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let temp_init = init
    return {
        increment: () => {
            return init += 1
        }, 
        reset: () => {
            init = temp_init
            return init
        },
        decrement: () => {
            return init -= 1
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */