#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>


class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        std::size_t lo = 0;
        std::size_t hi = matrix.size();
        int row = -1;

        while (lo < hi) {
            auto mid = lo + (hi - lo) / 2;
            if (matrix[mid][0] > target) {
                hi = mid;
            } else if (matrix[mid][0] < target) {
                row = mid;
                lo = mid + 1;
            } else {
                return true;
            }
        }

        if (row == -1) {
            return false;
        }
        return std::binary_search(matrix[row].begin(), matrix[row].end(), target);

    }
};


int main () {
    std::vector<std::vector<int>> matrix {{1,2,3}, {10,15,30}};
    assert(Solution().searchMatrix(matrix, 3) == true);
    assert(Solution().searchMatrix(matrix, 15) == true);
    assert(Solution().searchMatrix(matrix, 0) == false);
    assert(Solution().searchMatrix(matrix, 40) == false);
    return 0;
}
