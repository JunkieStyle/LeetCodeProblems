#include "vector"

using namespace std;

class Solution {
 public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    backtrack(comb, candidates, 0, target, result);
    return result;
  }

  void backtrack(vector<int>& comb, vector<int>& candidates, int begin,
                 int target, vector<vector<int>>& result) {
    if (target == 0) {
      result.push_back(comb);
    } else {
      for (int i = begin; i < candidates.size(); ++i) {
        if (candidates[i] <= target) {
          comb.push_back(candidates[i]);
          backtrack(comb, candidates, i, target - candidates[i], result);
          comb.pop_back();
        }
      }
    }
  }
};