/*
Largest palindrome product
~~~~~~~~~~~~~~~~~~~~~~~~~~
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/
let num = 0;
for (let a = 100; a < 1000; a++) {
    for (let b = 100; b < 1000; b++) {
        const val = a * b
        if (String(val) == [...String(val)].reverse().join('') && num < val)
            num = val;
    }
}
console.log(num);