#include<algorithm>
using namespace std;

class Solution {
public:
	double findMedianSortedArrays(int A[], int m, int B[], int n) {
		int total = m + n;
		if (total & 0x1) 
			return find_kth(A, m, B, n, total / 2 + 1);
		else
			return (find_kth(A, m, B, n, total / 2) + 
			find_kth(A, m, B, n, total / 2 + 1)) / 2.0;
	}
private:
	static int find_kth(int A[], int m, int B[], int n, int k) {
		if (m > n)
			return find_kth(B, n, A, m, k);
		if (m == 0)
			return B[k - 1];
		if (k == 1)
			return min(A[0], B[0]);

		int ia = min(k / 2, m), ib = k - ia; // m <= n
		if (A[ia - 1] < B[ib - 1])
			return find_kth(A + ia, m - ia, B, n, k - ia);
		else if (A[ia - 1] > B[ib - 1])
			return find_kth(A, m, B + ib, n - ib, k - ib);
		else
			return A[ia - 1];
	}
};