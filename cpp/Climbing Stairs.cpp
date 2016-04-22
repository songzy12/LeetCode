#include <cmath>
using namespace std;
class Solution {
  public:
    int climbStairs (int n) {
        const double s = sqrt(5);
        return floor((pow((1+s)/2,n+1) + pow((1-s)/2,n+1))/s + 0.5);
    }
};

/*
class Solution {
  public:
    int climbStairs(int n) {
        int prev = 0;
        int cur = 1;
        for(int i = 1; i <= n ; ++i){
            int tmp = cur;
            cur += prev;
            prev = tmp;
        }
        return cur;
    }
};*/