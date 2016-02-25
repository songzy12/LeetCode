#include<iostream>
#include<vector>
#include<map>
#include<tuple>
#include<unordered_map>
using namespace std;

typedef string::const_iterator Iterator;
typedef tuple<Iterator, Iterator, Iterator> Key;

namespace std {
	template<> struct hash<Key> {
		size_t operator()(const Key & x) const {
			Iterator first1, last1, first2;
			tie(first1, last1, first2) = x; // tie

			int result = *first1;
			result = result * 31 + *(prev(last1)); // caution!
			result = result * 31 + *first2;
			result = result * 31 + *(next(first2, distance(first1, last1) - 1));
			return result;
		}
	};
}

class Solution {
public:
	unordered_map<Key, bool> cache;
	bool isScramble(string s1, string s2) {
		cache.clear();
		return isScramble(s1.begin(), s1.end(), s2.begin());
	}

	bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
		auto length = distance(first1, last1);
		auto last2 = next(first2, length);

		if (length == 1)
			return *first1 == *first2;

		for (int i = 1; i < length; ++i)
			if (getOrUpdate(first1, first1 + i, first2) &&
				getOrUpdate(first1 + i, last1, first2 + i) ||
				getOrUpdate(first1, first1 + i, last2 - i) &&
				getOrUpdate(first1 + i, last1, first2))
				return true;
		return false;
	}

	bool getOrUpdate(Iterator first1, Iterator last1, Iterator first2) {
		auto key = make_tuple(first1, last1, first2);
		auto pos = cache.find(key);

		return (pos != cache.end()) ? 
			pos->second : (cache[key] = isScramble(first1, last1, first2));
	}
};

/*class Solution {
public:
	bool isScramble(string s1, string s2) {
		cache.clear();
		return isScramble(s1.begin(), s1.end(), s2.begin());
	}
private:
	typedef string::const_iterator Iterator;
	map<tuple<Iterator, Iterator, Iterator>, bool> cache;

	bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
		auto length = distance(first1, last1);
		auto last2 = next(first2, length);

		if (length == 1)
				return *first1 == *first2;

		for (int i = 1; i < length; ++i)
			if (getOrUpdate(first1, first1 + i, first2) &&
				getOrUpdate(first1 + i, last1, first2 + i) ||
				getOrUpdate(first1, first1 + i, last2 - i) &&
				getOrUpdate(first1 + i, last1, first2))
				return true;
		return false;
	}

	bool getOrUpdate(Iterator first1, Iterator last1, Iterator first2) {
		auto key = make_tuple(first1, last1, first2); // include tuple
		auto pos = cache.find(key);

		return (pos != cache.end()) ? 
			pos->second : (cache[key] = isScramble(first1, last1, first2));
	}
};*/

/*class Solution {
public:
	bool isScramble(string s1, string s2) {
		return isScramble(s1.begin(), s1.end(), s2.begin());
	}
private:
	typedef string::iterator Iterator;
	bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
		auto length = distance(first1, last1);
		auto last2 = next(first2, length);
		if (length == 1)
			return *first1 == *first2;
		// prune
		int A[26];
		fill(A, A+26, 0);
		for (int i = 0; i < length; ++i) A[*(first1+i) - 'a']++;
		for (int i = 0; i < length; ++i) A[*(first2+i) - 'a']--;
		for (int i = 0; i < length; ++i) if (A[i] != 0) return false;

		for (int i = 1; i < length; ++i)
			if (isScramble(first1, first1 + i, first2) &&
				isScramble(first1 + i, last1, first2 + i) ||
				isScramble(first1, first1 + i, last2 - i) &&
				isScramble(first1 + i, last1, first2))
				return true;
		return false;
	}
};*/

/*class Solution {
public:
	bool isScramble(string s1, string s2) {
		return isScramble(s1.begin(), s1.end(), s2.begin());
	}
private:
	typedef string::iterator Iterator;
	bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
		auto length = distance(first1, last1); // auto, distance
		auto last2 = next(first2, length); // next

		if (length == 1) return *first1 == *first2;

		for (int i = 1; i < length; ++i) {
			if (isScramble(first1, first1 + i, first2) && isScramble(first1 + i, last1, first2 + i) ||
				isScramble(first1, first1 + i, last2 - i) && isScramble(first1 + i, last1, first2))
				return true;
		}
		return false;
	}
};*/

/*class Solution {
public:
	bool isScramble(string s1, string s2) {
		const int N = s1.size();
		if (N != s2.size()) return false;

		vector<vector<vector<bool> > > f(N + 1, 
			vector<vector<bool>>(N, vector<bool>(N, false)));
		
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				f[1][i][j] = s1[i] == s2[j];

		for (int n = 1; n <= N; ++n) {
			for (int i = 0; i + n <= N; ++i) {
				for (int j = 0; j + n <= N; ++j) {
					for (int k = 1; k < n; ++k) {
						if (f[k][i][j] && f[n - k][i + k][j + k] ||
							f[k][i][j + n - k] && f[n - k][i + k][j]) {
							f[n][i][j] = true;
							break;
						}
					}
				}
			}
		}
		return f[N][0][0];
	}
};*/

int main() {
	string s1 = "great";
	string s2 = "rgtae";
	cout<<Solution().isScramble(s1, s2)<<endl;
	system("pause");
	return 0;
}