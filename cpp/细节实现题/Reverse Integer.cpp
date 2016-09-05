#include <iostream>
using namespace std;

class Solution {
    public:
    int reverse(int x) {
        int r = 0;
        for (; x; x /= 10) {
            r = r * 10 + x % 10;
        }
        return r;
    }
};

int main() {
    Solution s = Solution();
    cout<<s.reverse(-123)<<endl;
    cout<<(-123)/10<<" "<<(-123)%10<<endl;
    return 0;
}

/* (-123) / 10 == -12,
 * (-123) % 10 == -3
 */