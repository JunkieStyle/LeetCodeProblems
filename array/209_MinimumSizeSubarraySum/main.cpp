#include "vector"

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int result = 0;
        int left = 0;
        int sum = 0;
        
        for (int right = 0; right < nums.size(); ++right) {
            sum += nums[right];
            if (sum >= target) {
                while (sum >= target && left <= right) {
                    sum -= nums[left++];
                }
                if (result == 0 || result > right - left + 2) {
                    result = right - left + 2;
                }
            }
        }
        return result;
    }
};