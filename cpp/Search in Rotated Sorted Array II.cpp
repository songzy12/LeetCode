class Solution {
public:
	bool search(int A[], int n, int target) {
		int first = 0, last = n;
		while (first != last) {
			const int mid = (first + last) >> 1;
			if (A[mid] == target) 
				return true;
			if (A[first] < A[mid]) {
				if (A[first] <= target && target < A[mid])
					last = mid;
				else
					first = mid + 1;
			} else if (A[first] > A[mid]) {
				if (A[mid] < target && target <= A[last - 1])
					first = mid + 1;
				else
					last = mid;
			} else {
				first ++;
			}
		}
		return false;
	}
};