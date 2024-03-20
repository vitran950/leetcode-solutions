/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function(boxTypes, truckSize) {
    boxTypes.sort((a,b) => b[1]-a[1]);
    let count = 0;
    for (const box of boxTypes) {
        truckSize -= box[0];
        if (truckSize <= 0) {
            count += (truckSize += box[0])*box[1];
            break;
        }
        count += box[0]*box[1];
    }
    return count;
};