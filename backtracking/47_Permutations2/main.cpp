#include "algorithm"
#include "vector"
#include "unordered_map"

using namespace std;

class Solution {
 public:
  vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> temp;
    unordered_map<int, int> counter;
    for (auto& num : nums) {
      counter[num]++;
    }
    backtrack(temp, counter, nums, result);
    return result;
  }

  void backtrack(vector<int>& temp, unordered_map<int, int>& counter,
                 vector<int>& nums, vector<vector<int>>& result) {
    if (temp.size() == nums.size()) {
      result.push_back(temp);
    } else {
      for (auto& pair : counter) {
        auto key = pair.first;
        auto value = pair.second;
        if (value > 0) {
          counter[key]--;
          temp.push_back(key);
          backtrack(temp, counter, nums, result);
          temp.pop_back();
          counter[key]++;
        }
      }
    }
  }
};