#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	int numDistinct(const string &S, const string &T) {
		vector<int> f(T.size() + 1);
		f[0] = 1;
		for (int i = 0; i < S.size(); ++i) {
			for (int j = T.size() - 1; j >= 0; j--) {
				f[j + 1] += S[i] == T[j] ? f[j] : 0;
				// f[i][j] = f[i-1][j] 
				// f[i][j] = f[i-1][j] + f[i-1][j-1]
			}
		}
		return f[T.size()];
	}
};

int main() {
	string S = "rabbbit";
	string T = "rabbit";
	cout<<Solution().numDistinct(S, T)<<endl;
	system("pause");
	return 0;
}