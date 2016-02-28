/*
 * 4Sum.cpp
 *
 *  Created on: Feb 29, 2016
 *      Author: Andy
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> fourSum(vector<int>& num, int target) {
		vector<vector<int>> result;
		if (num.size() < 4) return result;
		sort(num.begin(), num.end());
		auto last = num.end();
		for (auto a = num.begin(); a < prev(last, 3); ++a) {
			for (auto b = next(a); b < prev(last, 2); ++b) {
				auto c = next(b);
				auto d = prev(last);
				while (c < d) {
					if (*a + *b + *c + *d < target) {
						++c;
					} else if (*a + *b + *c + *d > target) {
						--d;
					} else {
						result.push_back({ *a, *b, *c, *d });
						++c;
						--d;
					}
				}
			}
		}
		sort(result.begin(), result.end());
		result.erase(unique(result.begin(), result.end()), result.end());
		return result;
	}
};

int main() {
	cout<<"hi"<<endl;
	return 0;
}
