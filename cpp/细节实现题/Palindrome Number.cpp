/* Determine whether an integer is a palindrome. Do this without extra space.
 */

class Solution {
    public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        
        int d = 1;
        while (x / d >= 10)
            d *= 10;
        
        while (x > 0) {
            int q = x / d;
            int r = x % 10;
            if (q != r)
                return false;
            x = x % d / 10; // remove last digit and first digit
            d /= 100; // since we also remove the last digit
        }
        return true;
    }
}

/* while (x / d >= 10) d *= 10;
 * x = x % d / 10;
 * d /= 100;
 */