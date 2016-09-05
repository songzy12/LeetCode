#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

class Solution {
  public:
    int trap(int a[], int n) {
        stack<pair<int, int> > s;
        int water = 0;
        
        for (int i = 0; i < n; ++i) {
            int height = 0;
            while (!s.empty()) {
                int bar = s.top().first;
                int pos = s.top().second;
                // height = 0 at first?
                // since the first pos must be i - 1
                water += (min(bar, a[i]) - height) * (i - pos - 1);
                height = bar;
                
                if (a[i] < bar)
                    break;
                else 
                    s.pop();
            }
            
            s.push(make_pair(a[i], i));
        }
        
        return water;
    }
};

int main() {
    int a[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int n = sizeof(a)/ sizeof(int);
    cout<<Solution().trap(a, n)<<endl;
    return 0;
}

/*
class Solution {
  public:
    int trap(int A[], int n) {
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] > A[max])
                max = i;
        }
        
        int water = 0;
        for (int i = 0, peak = 0; i < max; i++)
            if (A[i] > peak)
                peak = A[i];
            else 
                water += peak - A[i];
        for (int i = n - 1, top = 0; i > max; i--) 
            if (A[i] > top)
                top = A[i];
            else 
                water += top - A[i];
        return water;
    }
};*/

/*
class Solution {
  public:
    int trap(int A[], int n) {
        int *max_left = new int [n]();
        int *max_right = new int [n]();
        
        for (int i = 1; i < n; ++i) {
            max_left[i] = max(max_left[i - 1], A[i - 1]);
            max_right[n - 1 - i] = max(max_right[n - i], A[n - i]);
        }
        
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            int height = min(max_left[i], max_right[i]);
            if (height > A[i]) {
                sum += height - A[i];
            }
        }
        
        delete [] max_left;
        delete [] max_right;
        return sum;
    }
};*/