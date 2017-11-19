#include <iostream>
using namespace std;
 
// Structure to represent an interval
struct Intervall
{
    int low, high;
};
 
// Structure to represent a node in Intervall Search Tree
struct ITNode
{
    Intervall *i;  // 'i' could also be a normal variable
    int max;
    ITNode *left, *right;
};

class MyCalendar {
public:
    MyCalendar() {
        root = NULL;
    }
    
    bool book(int start, int end) {
        if (overlapSearch(root, {start, end}) != NULL)
            return false;
        
        root = insert(root, {start, end});
        return true;
    }
private:
    // A utility function to create a new Intervall Search Tree Node
    ITNode * root;
    ITNode * newNode(Intervall i)
    {
        ITNode *temp = new ITNode;
        temp->i = new Intervall(i);
        temp->max = i.high;
        temp->left = temp->right = NULL;
        return temp;
    };
     
    // A utility function to insert a new Intervall Search Tree Node
    // This is similar to BST Insert.  Here the low value of interval
    // is used tomaintain BST property
    ITNode *insert(ITNode *root, Intervall i)
    {
        // Base case: Tree is empty, new node becomes root
        if (root == NULL)
            return newNode(i);
     
        // Get low value of interval at root
        int l = root->i->low;
     
        // If root's low value is smaller, then new interval goes to
        // left subtree
        if (i.low < l)
            root->left = insert(root->left, i);
     
        // Else, new node goes to right subtree.
        else
            root->right = insert(root->right, i);
     
        // Update the max value of this ancestor if needed
        if (root->max < i.high)
            root->max = i.high;
     
        return root;
    }
     
    // A utility function to check if given two intervals overlap
    bool doOVerlap(Intervall i1, Intervall i2)
    {
        if (i1.low < i2.high && i2.low < i1.high)
            return true;
        return false;
    }
     
    // The main function that searches a given interval i in a given
    // Intervall Tree.
    Intervall *overlapSearch(ITNode *root, Intervall i)
    {
        // Base Case, tree is empty
        if (root == NULL) return NULL;
     
        // If given interval overlaps with root
        if (doOVerlap(*(root->i), i))
            return root->i;
     
        // If left child of root is present and max of left child is
        // greater than or equal to given interval, then i may
        // overlap with an interval is left subtree
        if (root->left != NULL && root->left->max >= i.low)
            return overlapSearch(root->left, i);
     
        // Else interval can only overlap with right subtree
        return overlapSearch(root->right, i);
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.book(start,end);
 */