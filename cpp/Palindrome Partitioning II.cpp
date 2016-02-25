#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
	int minCut(string s) {
		const int n = s.size();
		vector<int> f(n+1);
		vector<vector<bool>> p(n, vector<bool>(n, false));
		for (int i = 0; i <= n; ++i) 
			f[i] = n - 1 - i;
		for (int i = n - 1; i >= 0; i--) {
			for (int j = i; j < n; j++) {
				if (s[i] == s[j] && (j - i < 2 || p[i + 1][j - 1])) {
					p[i][j] = true;
					f[i] = min(f[i], f[j + 1] + 1);
				}
			}
		}
		return f[0];
	}
};

int main() {
	string s = "aab";
	cout<<Solution().minCut(s)<<endl;
	system("pause");
	return 0;
}