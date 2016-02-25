#include<iostream>
#include<algorithm>
using namespace std;

/*class Solution {
public:
	int maxSubArray(int A[], int n) {
		int result = INT_MIN, f = 0;
		for (int i = 0; i < n; ++i) {
			f = max(f + A[i], A[i]);
			result = max(result, f);
		}
		return result;
	}
};*/

class Solution {
public:
	int maxSubArray(int A[], int n) {
		return mcss(A, n);
	}
private:
	static int mcss(int A[], int n) {
		int i, result, cur_min;
		int *sum = new int [n+1];
		sum[0] = 0;
		result = INT_MIN;
		cur_min = sum[0];
		for(int i = 1; i < n; i++) {
			sum[i] = sum[i - 1] + A[i - 1];
		}
		for(int i = 1; i < n; ++i) {
			result = max(result, sum[i] - cur_min);
			cur_min = min(cur_min, sum[i]);
		}
		delete[] sum;
		return result;
	}
};

int main() {
	int A[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
	int n = 9;
	cout<<Solution().maxSubArray(A, n)<<endl;
	system("pause");
	return 0;
}