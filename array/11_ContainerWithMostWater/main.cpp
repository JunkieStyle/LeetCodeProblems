#include "algorithm"
#include "vector"

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int result = 0;

        while (l < r) {
            result = std::max((r - l) * std::min(height[l], height[r]), result);
            height[l] < height[r] ? l++: r--;
        }
        return result;
    }
};
