#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
	int minimumTotal (vector<vector<int>>& triangle) {
		//&
		for (int i = triangle.size() - 2; i >= 0; --i) {
			for(int j = 0; j < i + 1; ++j) {
				triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
			}
		}
		return triangle[0][0];
	}
};

int main() {
	vector<vector<int>> triangle;
	vector<int> layer;
	layer.push_back(2);
	triangle.push_back(layer);
	cout<<Solution().minimumTotal(triangle)<<endl;
	system("pause");
	return 0;
}