/**
 * @param {string} s
 * @return {boolean}
 */
const isNumber = function(s) {
    if (s === 'Infinity' || s === '-Infinity' || s === '+Infinity') return false;
    return !isNaN(Number(s));
};