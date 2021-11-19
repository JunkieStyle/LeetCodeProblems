#include "algorithm"
#include "vector"

using namespace std;

class Solution {
 public:
  vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> subset;
    sort(nums.begin(), nums.end());
    backtrack(0, nums, subset, result);
    return result;
  }

  void backtrack(int begin, vector<int>& nums, vector<int>& subset,
                 vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = begin; i < nums.size(); ++i) {
      if (i == begin || nums[i] != nums[i - 1]) {
        subset.push_back(nums[i]);
        backtrack(i + 1, nums, subset, result);
        subset.pop_back();
      }
    }
  }
};