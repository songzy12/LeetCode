#include <vector>
#include <algorithm>
using namespace std;
/*
from right to left, find the first digit(PartitionNumber) which violate the increase trend
from right to left, find the first digit(ChangeNumber) which larget than the PartitionNumber
swap the PartitionNumber and ChangeNumber
reverse all the digit on the right of the partition index
*/

class Solution {
  public:
    void nextPermutation(vector<int> &num) {
        next_permutation(num.begin(), num.end());
    }
    
    template<typename BidiIt>
    bool next_permutation(BidiIt first, BidiIt last) {
        const auto rfirst = reverse_iterator<BidiIt>(last);
        const auto rlast = reverse_iterator<BidiIt>(first);
        
        auto pivot = next(rfirst);
        while (pivot != rlast && *pivot >= *prev(pivot)) 
            pivot++;
        
        if (pivot == rlast) {
            reverse(rfirst, rlast);
            return false;
        }
        
        auto change = find_if(rfirst, pivot, bind1st(less<int>(), *pivot));
        
        swap(*change, *pivot);
        reverse(rfirst, pivot);
        
        return true;
    }
};