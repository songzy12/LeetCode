/*class Solution {
public:
	int removeDuplicates(int A[], int n) {
		if (n <= 2)
			return n;

		int index = 2;
		for (int i = 2; i < n; ++i)
			if (A[i] != A[index - 2])
				A[index++] = A[i];

		return index;
	}
};*/

class Solution {
public:
	int removeDuplicates(int A[], int n) {
		int index = 0;
		for (int i = 0; i < n; ++i) {
			if (i > 0 && i < n - 1 && A[i] == A[i - 1] && A[i] == A[i + 1])
				continue;
			A[index++] = A[i];
		}
		return index;
	}
};