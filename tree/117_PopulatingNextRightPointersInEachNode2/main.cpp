#include "queue"

// Definition for a Node.
class Node {
 public:
  int val;
  Node* left;
  Node* right;
  Node* next;

  Node() : val(0), left(NULL), right(NULL), next(NULL) {}

  Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

  Node(int _val, Node* _left, Node* _right, Node* _next)
      : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
 public:
  Node* connect_bfs(Node* root) {
    std::queue<Node*> queue;
    queue.push(root);

    while (!queue.empty()) {
      Node* prev = nullptr;
      int level_size = queue.size();
      for (int i = 0; i < level_size; ++i) {
        Node* node = queue.front();
        queue.pop();
        if (node == nullptr) {
          continue;
        }
        node->next = prev;
        prev = node;
        queue.push(node->right);
        queue.push(node->left);
      }
    }

    return root;
  }

  Node* connect(Node* root) {
    if (root == nullptr || (!root->left && !root->right)) {
      return root;
    }

    Node* next = nullptr;
    Node* node = root;
    while (node->next) {
      next = (node->next->left) ? node->next->left : node->next->right;
      if (next) {
        break;
      }
      node = node->next;
    }

    if (root->left && root->right) {
      root->left->next = root->right;
      root->right->next = next;
    } else if (root->right) {
      root->right->next = next;
    } else {
      root->left->next = next;
    }

    connect(root->right);
    connect(root->left);

    return root;
  }
};