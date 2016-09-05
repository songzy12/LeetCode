#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
// Definition for singly-linked list.
struct ListNode{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL){}
};
 
/*bool cmp(ListNode *a, ListNode *b){
	// can not put cmp in the class
	return a->val >= b->val;
}

class Solution {
private:
	vector<ListNode *> heap_;
public:
    ListNode* mergeKLists(vector<ListNode*>& lists){
		heap_.clear();
		int k = lists.size();
		ListNode* dummy = new ListNode(0);
		ListNode* head = dummy;
        for(int i=0; i<k; ++i)
			if(lists[i]!=NULL)
				heap_.push_back(lists[i]);
		make_heap(heap_.begin(), heap_.end(), cmp); // max heap by default
		while(!heap_.empty()){
			pop_heap(heap_.begin(), heap_.end(), cmp);// remember cmp
			
			ListNode* temp = heap_[heap_.size()-1];
			heap_.pop_back();
			if(temp->next != NULL)
				heap_.push_back(temp->next);
			push_heap(heap_.begin(), heap_.end(), cmp);
			
			head->next = temp;
			head = head->next;
		}
		return dummy->next;
    }
};*/

class Solution {
public:
	ListNode *mergeKLists(vector<ListNode *> &lists) {
		if (lists.size() == 0)	return nullptr; // nullptr
		ListNode *p = lists[0];
		for (int i = 1; i < lists.size(); ++i) {
			p = mergeTwoLists(p, lists[i]);
		}
		return p;
	}

	ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
		ListNode head(-1);
		for (ListNode* p = &head; l1 != nullptr || l2 != nullptr; p = p->next) {
			int val1 = l1 == nullptr ? INT_MAX : l1->val; // INT_MAX
			int val2 = l2 == nullptr ? INT_MAX : l2->val;
			if (val1 <= val2) {
				p->next = l1;
				l1 = l1->next;
			} else {
				p->next = l2;
				l2 = l2->next;
			}
		}
		return head.next;
	}
};

int main(){
	ListNode* node11 = new ListNode(-1);
	ListNode* node12 = new ListNode(1);
	node11->next = node12;
	ListNode* node21 = new ListNode(-3);
	ListNode* node22 = new ListNode(1);
	ListNode* node23 = new ListNode(4);
	node21->next = node22;
	node22->next = node23;
	ListNode* node31 = new ListNode(-2);
	ListNode* node32 = new ListNode(-1);
	ListNode* node33 = new ListNode(0);
	ListNode* node34 = new ListNode(2);
	node31->next = node32;
	node32->next = node33;
	node33->next = node34;
	vector<ListNode*> lists;
	lists.push_back(node11);
	lists.push_back(node21);
	lists.push_back(node31);
	ListNode* head = Solution().mergeKLists(lists);
	while(head!=NULL){
		cout<<head->val<<" ";
		head = head->next;
	}
	system("pause");
	return 0;
}