/*
Sum square difference
~~~~~~~~~~~~~~~~~~~~~
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10) ^ 2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/
#include <stdio.h>
#include <math.h>

int difference(int n) {
    int sum_of_sq = (n * (n + 1) * (2*n + 1)) / 6;  // = (1^2 + 2^2 + ... + n^2)
    int sq_of_sum = pow((n*(n + 1) / 2), 2);  // = (1 + 2 + ... + n) ^ 2
    return sq_of_sum - sum_of_sq;
}

int main()
{
    printf("%d", difference(100));
}