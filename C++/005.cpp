#include <iostream>
#include <algorithm> // std::gcd() is in <numeric> from C++17
#include <vector>

int lcm(std::vector<int> numbers) {
    int result = numbers.back();
    numbers.pop_back();

    for (int num : numbers) {
        result = ((result * num) / std::__gcd(result, num));
    }
    return result;
}

int main()
{
    std::vector<int> nums;
    for (int i = 1; i <= 20; i++) {
        nums.push_back(i);
    } 
    std::cout << lcm(nums);
}
