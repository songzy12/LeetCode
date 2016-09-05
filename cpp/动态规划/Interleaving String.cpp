#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

class Solution {
public:
	bool isInterleave(string s1, string s2, string s3) {
		if (s3.length() != s1.length() + s2.length())
			return false;
		if (s1.length() < s2.length())
			return isInterleave(s2, s1, s3);
		// s1.length() > s2.length()
		vector<bool> f(s2.length() + 1, true);
		for (size_t i = 1; i <= s2.length(); ++i)
			f[i] = s2[i - 1] == s3[i - 1] && f[i - 1];

		for (size_t i = 1; i <= s1.length(); ++i) {
			f[0] = s1[i - 1] == s3[i - 1] && f[0]; // f[i][0]
			for (size_t j = 1; j <= s2.length(); ++j) 
				// f[j] = f[i - 1][j], f[j - 1] = f[i][j - 1]
				f[j] = s1[i - 1] == s3[i + j - 1] && f[j] ||
				s2[j - 1] == s3[i + j - 1] && f[j - 1]; 
		}
		
		return f[s2.length()];
	}
};

/*class Solution {
public:
	bool isInterleave(string s1, string s2, string s3) {
		if (s3.length() != s1.length() + s2.length())
			return false;
		vector<vector<bool>> f(s1.length() + 1, vector<bool>(s2.length() + 1, true));
		// f[i][j] means isInterleave(s1[:i], s2[:j], s3[:i+j] returns true
		for (size_t i = 1; i <= s1.length(); ++i) // size_t
			f[i][0] = f[i-1][0] && s1[i-1] == s3[i-1];

		for (size_t i = 1; i <= s2.length(); ++i)
			f[0][i] = f[0][i-1] && s2[i-1] == s3[i-1];

		for (size_t i = 1; i <= s1.length(); ++i)
			for (size_t j = 1; j <= s2.length(); ++j)
				f[i][j] = s1[i - 1] == s3[i + j - 1] && f[i - 1][j] || 
				s2[j - 1] == s3[i + j - 1] && f[i][j - 1];

		return f[s1.length()][s2.length()];
	}
};*/

/*class Solution {
public:
	bool isInterleave(string s1, string s2, string s3) {
		if (s3.length() != s1.length() + s2.length())
			return false;
		return isInterleave(begin(s1), end(s1), begin(s2), end(s2),
			begin(s3), end(s3)); // begin, end
	}

	template<typename InIt>
	bool isInterleave(InIt first1, InIt last1, InIt first2, InIt last2,
		InIt first3, InIt last3) {
		if (first3 == last3) 
			return first1 == last1 && first2 == last2;
		return (*first1 == *first3) &&
			isInterleave(next(first1), last1, first2, last2, next(first3), last3) ||
			(*first2 == *first3) &&
			isInterleave(first1, last1, next(first2), last2, next(first3), last3);
	}
};*/

int main() {
	string s1 = "aabcc";
	string s2 = "dbbca";
	string s3 = "aadbbcbcac";
	cout<<Solution().isInterleave(s1, s2, s3)<<endl;
	system("pause");
	return 0;
}