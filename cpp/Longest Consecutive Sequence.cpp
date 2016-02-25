#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
	int longestConsectutive(vector<int> &num) {
		unordered_map<int, int> map;
		int size = num.size();
		int l = 1;
		for (int i = 0; i < size; ++i) {
			if (map.find(num[i]) != map.end()) 
				continue;
			map[num[i]] = 1;
			if (map.find(num[i] - 1) != map.end()) {
				l = max(l, mergeCluster(map, num[i] - 1, num[i]));
			}
			if (map.find(num[i] + 1) != map.end()) {
				l = max(l, mergeCluster(map, num[i], num[i] + 1));
			}
		}
	}
private:
	int mergeCluster(unordered_map<int, int> &map, int left, int right) {
		int upper = right + map[right] - 1;
		int lower = left - map[left] + 1;
		int length = upper - lower + 1;
		map[upper] = length;
		map[lower] = length;
		return length;
	}
};

/*class Solution {
public:
	int longestConsecutive(const vector<int> &num) {
		unordered_map<int, bool> used;
		for (auto i : num) used[i] = false;
		int longest = 0;
		for (auto i : num) {
			if (used[i]) 
				continue;
			int length = 1;
			used[i] = true;
			for (int j = i + 1; used.find(j) != used.end(); j++) {
				used[j] = true;
				++length;
			}
			for (int j = i - 1; used.find(j) != used.end(); j--) {
				used[j] = true;
				++length;
			}
			longest = max(longest,length);
		}
		return longest;
	}
};*/