#include "string"
#include "unordered_map"
#include "vector"

class Solution {
 public:
  std::vector<int> findAnagrams(std::string s, std::string p) {
    std::vector<int> result;
    std::unordered_map<char, int> counter, window;

    for (auto c : p) {
      counter[c]++;
    }
    for (int i = 0; i < s.size(); ++i) {
      window[s[i]]++;
      if (i >= p.size() && (--window[s[i - p.size()]] == 0)) {
        window.erase(s[i - p.size()]);
      }
      if (window == counter) {
        result.push_back(i - p.size() + 1);
      }
    }
    return result;
  }
};