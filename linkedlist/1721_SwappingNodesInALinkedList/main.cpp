// Definition for singly-linked list.
#include <algorithm>
#include <cstddef>
#include <type_traits>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* n1 = nullptr;
        ListNode* n2 = nullptr;
        for (ListNode* p = head; p != nullptr; p = p->next) {
            if (n2) {
                n2 = n2->next;
            }
            if (--k == 0) {
                n1 = p;
                n2 = head;
            }
        }
        std::swap(n1->val, n2->val);
        return head;
    }
};

