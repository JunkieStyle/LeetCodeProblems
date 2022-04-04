#include <string>

class Solution {
public:
    bool validPalindrome(string s, int count = 1) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            if (s[i] == s[j]) {
                i++; j--;
            } else if (count) {
                return validPalindrome(s.substr(i + 1, j - i), 0) or validPalindrome(s.substr(i, j - i), 0);
            } else {
                return false;
            }
        }
        return true;
    }
};
