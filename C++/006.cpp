#include <iostream>
#include <math.h>

int sumDifference(int n) {
    int sum_of_sq = (n * (n + 1) * (2*n + 1)) / 6;  // = (1^2 + 2^2 + ... + n^2)
    int sq_of_sum = pow((n*(n + 1) / 2), 2);  // = (1 + 2 + ... + n) ^ 2
    return sq_of_sum - sum_of_sq;
}

int main() {
    std::cout << sumDifference(100);
}