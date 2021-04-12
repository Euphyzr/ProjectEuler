#include <iostream>

int main()
{
    unsigned long long sum = 0, temp = 0;
    unsigned long long a = 1, b = 1;
    while (a < 4000000) {
        temp = a;
        a = b;
        b = temp + a;
        if (b % 2 == 0)
            sum += b;
    }
    std::cout << sum;
}
