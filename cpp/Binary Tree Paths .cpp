#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
  public:
	void SearchLeafs(TreeNode *root,TreeNode *leafHead,map<string,string> &parent){
		if (!root->left&&!root->right)
		{
			//insert into the list header
			TreeNode * t=leafHead->right;
			leafHead->right=root;
			root->right=t;
			return;
		}
		char *intPStr=new char(50),*intCStr=new char(50);
		if (root->left)
		{
			sprintf(intPStr,"%d",root->val);
			sprintf(intCStr,"%d",root->left->val);
			string parentstr( intPStr),childstr(intCStr);

			parent[childstr]=parentstr;
			SearchLeafs(root->left,leafHead,parent);
		}
		if (root->right)
		{
			sprintf(intPStr,"%d",root->val);
			sprintf(intCStr,"%d",root->right->val);
			string parentstr( intPStr),childstr(intCStr);
			parent[childstr]=parentstr;
			SearchLeafs(root->right,leafHead,parent);
		}
	}
    vector<string> binaryTreePaths(TreeNode* root){
		vector<string> paths;
		if (!root)
		{
			return paths;
		}
		TreeNode *leafHead=new TreeNode(0);
		map<string,string> parent;
		SearchLeafs(root,leafHead,parent);
		char * intCStr=new char(50);
		while (leafHead->right)
		{
			sprintf(intCStr,"%d",leafHead->right->val);
			string chldstr(intCStr);
			string path=chldstr;
			while (parent.find(chldstr)!=parent.end())
			{
				path.insert(0,parent[chldstr]+"->");
				chldstr=parent[chldstr];
			}
			leafHead=leafHead->right;
			paths.insert(paths.begin(),path);
		}
		return paths;
	}
};

int main(){
	TreeNode *node1 = new TreeNode(1);
	TreeNode *node2 = new TreeNode(2);
	TreeNode *node3 = new TreeNode(3);
	node1->left = node2;
	node1->right = node3;
	vector<string> ans = Solution().binaryTreePaths(node1);
	for(int i=0; i<ans.size(); ++i)
		cout<<ans[i]<<endl;
	return 0;
}