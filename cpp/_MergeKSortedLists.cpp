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
 
bool cmp(ListNode *a, ListNode *b){
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
			pop_heap(heap_.begin(), heap_.end());
			
			for(int i=0; i<heap_.size(); ++i)
				cout<<heap_[i]->val<<" ";
			cout<<endl;
			
			ListNode* temp = heap_[heap_.size()-1];
			heap_.pop_back();
			if(temp->next != NULL)
				heap_.push_back(temp->next);
			push_heap(heap_.begin(), heap_.end(), cmp);
			for(int i=0; i<heap_.size(); ++i)
				cout<<heap_[i]->val<<" ";
			cout<<endl;

			head->next = temp;
			head = head->next;
		}
		return dummy->next;
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
	return 0;
}