#include "vector"

using namespace std;

class Solution {
 public:
  vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;

    for (int counter = 0; counter < (1 << nums.size()); ++counter) {
      vector<int> subset;
      for (int pos = 0; pos < nums.size(); ++pos) {
        if (counter & (1 << pos)) {
          subset.push_back(nums[pos]);
        }
      }
      result.push_back(subset);
    }
    return result;
  }
};