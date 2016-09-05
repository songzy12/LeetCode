using namespace std;

class Solution {
public:
	int search(int A[], int n, int target) {
		int first = 0, last = n;
		while (first != last) {
			const int mid = (first + last) >> 1;
			if (A[mid] == target)
				return mid;
			if (A[first] <= A[mid]) {
				if (A[first] <= target && target < A[mid])
					last = mid;
				else
					first = mid + 1;
			} else {
				if (A[mid] < target && target <= A[last - 1])
					first = mid + 1;
				else 
					last = mid;
			}
		}
		return - 1;
	}
}; 