#include<iostream>
#include<vector>
#include<numeric> // std::accumulate
#include<algorithm> // std::sort
using namespace std;
// fill(first,last,val);
// fill_n(first, count, val);
/*class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() <= 3)
            // sum vector
            return accumulate(nums.begin(), nums.end(), 0);
        // sort vector
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int result = nums[0]+nums[1]+nums[2];
        int temp;
        for(int i = 0; i < size - 2; i ++){
            int j = i + 1, k = size - 1;
            while(j < k){
                temp = nums[i]+nums[j]+nums[k];
                if (temp == target)
                    return target;
                if (temp < target)
                    j ++;
                if (temp > target)
                    k --;
                if(abs(temp-target)<abs(result-target))
                        result = temp;
            }
        }
        return result;
    }
};*/

class Solution {
public:
	int threeSumClosest(vector<int>& num, int target) {
		int result = 0;
		int min_gap = INT_MAX;

		sort(num.begin(), num.end());
		//cout<<prev(num.end(), 2) - num.begin()<<endl;
		//cout<<num.end() - num.begin()<<endl;
		for(auto a = num.begin(); a != prev(num.end(), 2); ++a) {
			auto b = next(a); // prev, next
			auto c = prev(num.end());
			while (b < c) {
				const int sum = *a + *b + *c;
				const int gap = abs(sum - target);
				if (gap < min_gap) {
					result = sum;
					min_gap = gap;
				} 
				if (sum < target) 
					++b;
				else 
					--c;
			}
		}
		return result;
	}
};

int main(){
    int nums_[] = {-1,2,1,4};
    // init vector
    vector<int> nums(nums_, nums_+sizeof(nums_)/sizeof(int)); 
    cout<<Solution().threeSumClosest(nums, 1)<<endl;
	system("pause");
}