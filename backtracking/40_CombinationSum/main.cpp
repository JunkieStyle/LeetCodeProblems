#include "algorithm"
#include "vector"

using namespace std;

class Solution {
 public:
  vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
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
        if (i > begin && candidates[i] == candidates[i - 1]) {
          continue;
        }
        if (candidates[i] <= target) {
          comb.push_back(candidates[i]);
          backtrack(comb, candidates, i + 1, target - candidates[i], result);
          comb.pop_back();
        }
      }
    }
  }
};