#include <vector>
#include <algorithm>
using namespace std;

class Solution {
  public:
    int candy(const vector<int> &ratings) {
        vector<int> f(ratings.size());
        int sum = 0;
        for (int i = 0; i < ratings.size(); ++i) 
            sum += solve(ratings, f, i);
        return sum;
    }
  private:
    int solve(const vector<int> &ratings, vector<int> &f, int i) {
        if (f[i] == 0) {
            f[i] = 1;
            if (i > 0 && ratings[i] > ratings[i - 1])
                f[i] = max(f[i], solve(ratings, f, i - 1) + 1);
            if (i < ratings.size() - 1 && ratings[i] > ratings[i + 1])
                f[i] = max(f[i], solve(ratings, f, i + 1) + 1);
        }
        return f[i];
    }
}

/*
class Solution {
  public:
    int candy(vector<int> &ratings) {
        const int n = ratings.size();
        vector<int> increment(n);
        
        for (int i = 1, inc = 1; i < n; ++i) {
            if (ratings[i] > ratings[i-1])
                increment[i] = max(inc++, increment[i]);
            else
                inc = 1;
        }
        
        for (int i = n - 2, inc = 1; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1])
                increment[i] = max(inc++, increment[i]);
            else
                inc = 1;
        }
        
        return accumulate(&increment[0], &increment[0] + n, n);
    }
};*/