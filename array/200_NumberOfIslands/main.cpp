#include "vector"
#include "queue"
#include "utility"

class Solution {
 public:
  int numIslands(std::vector<std::vector<char>>& grid) {
    int result = 0;
    for (int i = 0; i < grid.size(); ++i) {
      for (int j = 0; j < grid[0].size(); ++j) {
        if (grid[i][j] == '1') {
          dfs(i, j, grid);
          // bfs(i, j, grid);
          result += 1;
        }
      }
    }
    return result;
  }
  
  void dfs(int i, int j, std::vector<std::vector<char>>& grid) {
    if (i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size() && grid[i][j] == '1') {
      grid[i][j] = '0';
      dfs(i + 1, j, grid);
      dfs(i - 1, j, grid);
      dfs(i, j + 1, grid);
      dfs(i, j - 1, grid);
    }
  }

  void bfs(int i, int j, std::vector<std::vector<char>>& grid) {
    std::queue<std::pair<int, int>> queue;
    queue.push(std::pair<int, int>(i, j));
    while (!queue.empty()) {
      auto item = queue.front();
      queue.pop();
      i = item.first;
      j = item.second;
      if (i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size() && grid[i][j] == '1') {
        grid[i][j] = '0';
        queue.push(std::pair(i + 1, j));
        queue.push(std::pair(i - 1, j));
        queue.push(std::pair(i, j + 1));
        queue.push(std::pair(i, j - 1));
      }
    }
  }
};
