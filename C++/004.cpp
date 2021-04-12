#include <iostream>
#include <algorithm>

bool is_palindrome(int i) {
    std::string str_i = std::to_string(i);
    std::string copy(str_i);
    std::reverse(copy.begin(), copy.end());

    return str_i == copy;
}

int main()
{
    int max;
    for (int a = 100; a < 1000; a++) {
        for (int b = 100; b < 1000; b++) {
            int result = a * b;

            if (is_palindrome(result) && result > max) {
                max = result;
            } 
        }
    }
    std::cout << max;
}