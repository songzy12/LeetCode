#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
class Solution {
public:
    int countPrimes(int n) {
        bool* numbers = new bool[n];
        memset(numbers, true, n);
        int sqrtn = int(sqrt(n));
        int count = 0;
        for(int i = 2; i <= sqrtn; i++){
            if(numbers[i] == false)
                continue;
            int times = 2;
            while(times * i < n){
                numbers[times * i] = false;
                times++;
            }
        }
        for(int i = 2; i < n; i++){
            if(numbers[i])
                count += 1;
        }
        delete numbers;
        return count;
    }
};

int main(){
    cout<<Solution().countPrimes(1000000)<<endl;
    return 0;
}
