#include <iostream>
#include <unordered_set>
using namespace std;

class Solution {
public:
	bool wordBreak(string s, unordered_set<string> &dict) {
		vector<bool> f(s.size() + 1, false);
		f[0] = true; // ""
		for (int i = 1; i <= s.size(); ++i){
			for (int j = i -1; j >= 0; --j) {
				if (f[j] && dict.find(s.substr(j, i-j)) != dict.end()) {
					f[i] = true;
					break;
				}
			}
		}
		return f[s.size()];
	}
};

/*class Solution {
public:
	bool wordBreak(string s, unordered_set<string> &dict) {
		return dfs(s, dict, 0, 0);
	}
private:
	static bool dfs(const string &s, unordered_set<string> &dict, 
		size_t start, size_t cur) {
		if (cur == s.size())
			return dict.find(s.substr(start, cur - start + 1)) != dict.end();
		if (dfs(s, dict, start, cur + 1))
			return true;
		if (dict.find(s.substr(start, cur - start + 1)) != dict.end())
			if (dfs(s, dict, cur + 1, cur + 1))
				return true;
		return false;
	}
};*/

int main() {
	string s = "leetcode";
	unordered_set<string> dict;
	dict.insert("leet");
	dict.insert("code");
	cout<<Solution().wordBreak(s, dict)<<endl;
}