#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& num) {
		vector<vector<int>> result;
		if (num.size() < 3)
			return result;
		sort(num.begin(), num.end());
		const int target = 0;

		auto last = num.end();
		for (auto i = num.begin(); i < last - 2; ++i) {
			auto j = i + 1;
			if (i > num.begin() && *i == *(i - 1))
				continue;
			auto k = last - 1;
			while (j < k) {
				if (*i + *j + *k < target) {
					++j;
					while (*j == *(j - 1) && j < k) 
						++j;
				} else if (*i + *j + *k > target) {
					--k;
					while (*k == *(k + 1) && j < k) 
						--k;
				} else {
					int tmp[] = {*i, *j, *k};
					result.push_back(vector<int>(tmp, tmp + 3));
					++j;
					--k;
					while (*j == *(j - 1) && *k == *(k + 1) && j < k)
						++j;

				}
			}
		}
		return result;
	}
};