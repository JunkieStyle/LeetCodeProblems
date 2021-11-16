#include "vector"
#include "unordered_map"


class Solution {
 public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::unordered_map<int, int> h;
    std::vector<int> result;

    for (int i = 0; i < nums.size(); ++i) {
      int diff = target - nums[i];

      if (h.find(diff) != h.end()) {
        result.push_back(h.at(diff));
        result.push_back(i);
      }
      h.insert({nums[i], i});
    }
    return result;
  }
};