#include<iostream>
#include<vector>
#include<numeric> // std::accumulate
#include<algorithm> // std::sort
using namespace std;
// fill(first,last,val);
// fill_n(first, count, val);
class Solution {
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
};

int main(){
    int nums_[] = {-1,2,1,4};
    // init vector
    vector<int> nums(nums_, nums_+sizeof(nums_)/sizeof(int)); 
    cout<<Solution().threeSumClosest(nums, 1)<<endl;
}
