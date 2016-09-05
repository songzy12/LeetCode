#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	int maximalRectangle(vector<vector<char> > &matrix) {
		if (matrix.empty()) return 0;
		const int m = matrix.size();
		const int n = matrix[0].size();
		vector<int> H(n, 0);
		vector<int> L(n, 0);
		vector<int> R(n, n);

		int ret = 0;
		for (int i = 0; i < m; ++i) {
			int left = 0, right = n;

			for (int j = 0; j < n; ++j) {
				if (matrix[i][j] == '1') {
					++H[j];
					// i = 0, L[j] will become left.
					// else, L[j]  will become right most of left.
					L[j] = max(L[j], left);
				} else {
					left = j + 1;
					H[j] = 0; L[j] = 0; R[j] = n; // reset
				}
			}

			for (int j = n - 1; j >= 0; --j) {
				if (matrix[i][j] == '1') {
					// i = 0, R[j] will become right.
					// else, R[j] will become left most of right.
					R[j] = min(R[j], right);
					ret = max(ret, H[j] * (R[j] - L[j]));
				} else {
					right = j;
				}
			}
		}
		return ret;
	}
};