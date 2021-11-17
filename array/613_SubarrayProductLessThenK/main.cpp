#include "vector"

class Solution {
public:
    int numSubarrayProductLessThanK(std::vector<int>& nums, int k) {
        int result = 0;
        int j = 0;
        int prod = 1;
        
        for (int i = 0; i < nums.size(); ++i) {
            prod *= nums[i];
            while (prod >= k && j <= i) {
                prod /= nums[j++];
            }
            result += i - j + 1;
        }
        return result;
    }
};