/*
Even Fibonacci numbers
~~~~~~~~~~~~~~~~~~~~~~
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/
#include <stdio.h>

int main()
{
    unsigned long long sumof;
    unsigned long long a = 1, b = 1, temp;

    while (a < 4000000) {
        // set a to the current number in the sequence 
        // and b to the next number
        temp = a, a = b, b = temp + b;
        if (!(b % 2)) sumof += b;
    }
    printf("%d", sumof);
}