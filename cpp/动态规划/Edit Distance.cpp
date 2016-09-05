#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int minDistance(const string &word1, const string &word2) {
		if (word1.length() < word2.length())
			return minDistance(word2, word1);
		
		vector<int> f(word2.length() + 1); // shorter
		int upper_left = 0;

		for (size_t i = 0; i <= word2.size(); ++i)
			f[i] = i;

		for (size_t i = 1; i <= word1.size(); ++i) {
			upper_left = f[0];
			f[0] = i;

			for (size_t j = 1; j <= word2.size(); ++j) {
				int upper = f[j];
				if (word1[i - 1] == word2[j - 1])
					f[j] = upper_left;
				else 
					f[j] = 1 + min(upper_left, min(f[j], f[j-1]));
				upper_left = upper;
			}
		}

		return f[word2.length()];
	}
};

/*class Solution {
public:
	int minDistance(const string &word1, const string &word2) {
		const size_t n = word1.size();
		const size_t m = word2.size();
		vector<vector<int> > f(n + 1, vector<int>(m + 1, 0));
		for (size_t i = 0; i <= n; ++i)
			f[i][0] = i;
		for (size_t j = 0; j <= m; ++j)
			f[0][j] = j;

		for (size_t i = 1; i <= n; ++i) {
			for (size_t j = 1; j <= m; ++j) {
				if (word1[i - 1] == word2[j - 1]) {
					f[i][j] = f[i - 1][j - 1];
				}
				else {
					// f[i - 1][j]: delete word1[-1]
					// f[i][j - 1]: delete word2[-1]
					// f[i - 1][j - 1]: change word1[-1] to word2[-1]
					int mn = min(f[i - 1][j], f[i][j - 1]);
					f[i][j] = 1 + min(f[i - 1][j - 1], mn);
				}
					
			}
		}
	}
};*/