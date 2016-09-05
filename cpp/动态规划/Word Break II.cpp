#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

class Solution {
public:
	vector<string> wordBreak(string s, unordered_set<string> dict) {
		vector<bool> f(s.length()+1, false);
		vector<vector<bool> > prev(s.length() + 1, vector<bool>(s.length()));
		f[0] = true;
		for (size_t i = 1; i <= s.length(); ++i) {
			for (int j = i - 1; j >= 0; --j) {
				if (f[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
					f[i] = true;
					prev[i][j] = true;
				}
			}
		}
		vector<string> result;
		vector<string> path;
		gen_path(s, prev, s.length(), path, result);
		return result;
	}
private:
	void gen_path(const string &s, const vector<vector<bool> > &prev,
		int cur, vector<string> &path, vector<string> &result) {
			if (cur == 0) {
				string tmp;
				for (auto iter = path.crbegin(); iter != path.crend(); ++iter) {
					tmp += *iter;
					tmp += " ";
				}
				tmp.erase(tmp.end() - 1);
				result.push_back(tmp);
			} // put path into result
			for (size_t i = 0; i < s.size(); ++i) {
				if (prev[cur][i]) {
					path.push_back(s.substr(i, cur - i));
					gen_path(s, prev, i, path, result);
					path.pop_back();
				}
			} 
	}
};