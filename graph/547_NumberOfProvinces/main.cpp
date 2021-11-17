#include "vector"
#include "queue"
#include "unordered_set"

class Solution {
public:
    int findCircleNum(std::vector<std::vector<int>>& isConnected) {
      std::unordered_set<int> visited;
      std::queue<int> queue;
      int num_circles = 0;

      for (int i = 0; i < isConnected.size(); ++i) {
        if (visited.find(i) != visited.end()) {
          continue;
        }
        queue.push(i);
        num_circles++;
        while (!queue.empty()) {
          auto node = queue.front();
          queue.pop();
          if (visited.find(node) == visited.end()) {
            visited.insert(node);
            for (int j = 0; j < isConnected.size(); ++j) {
              if (node != j && isConnected[node][j]) {
                queue.push(j);
              }
            }
          }
        }
      }        
      return num_circles;
    }
};