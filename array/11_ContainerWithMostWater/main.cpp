#include "algorithm"
#include "vector"

class Solution {
 public:
  int maxArea(std::vector<int>& height) {
    int i = 0;
    int j = height.size() - 1;
    int result = 0;
    while (i < j) {
      int h = std::min({height[i], height[j]});
      result = std::max({result, h * (j - i)});
      while (height[i] <= h && i < j) i++;
      while (height[j] <= h && i < j) j--;
    }
    return result;
  }
};