#include <iostream>
#include <algorithm>
using namespace std;

/*class Solution {
public:
	int removeDuplicates(int A[], int n) {
		if (n == 0) return 0;

		int index = 0;
		for (int i = 1; i < n; ++i) {
			if (A[index] != A[i])
				A[++index] = A[i];
		}
		return index + 1;
	}
};*/

/*class Solution {
public:
	int removeDuplicates(int A[], int n) {
		// unique(A, A + n) - A 
		return distance(A, unique(A, A + n));
	}
};*/

class Solution {
public:
	int removeDuplicates(int A[], int n) {
		// cout<<upper_bound(A, A + n, *A) - A<<endl;
		// cout<<lower_bound(A, A + n, *A) - A<<endl;
		return removeDuplicates(A, A + n, A) - A;
	}
	template<typename InIt, typename OutIt>
	OutIt removeDuplicates(InIt first, InIt last, OutIt output) {
		while (first != last) {
			*output++ = *first;
			first = upper_bound(first, last, *first);
		}
		return output;
	}
};

int main() {
	int A[] = {1, 1, 1, 2, 2, 3};
	int n = 6;
	Solution solution = Solution();
	int len = solution.removeDuplicates(A, n);
	for(int i = 0; i < len; ++i)
		cout<<A[i]<<" ";
	cout<<endl;
	system("pause");
	return 0;
}