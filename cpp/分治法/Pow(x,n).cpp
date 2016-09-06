class Solution {
  public:
    double pow(double x, int n) {
        if (n < 0)
            return 1.0 / power(x, -n);
        else
            return power(x, n);
    }
  private:
    double power(double x, int n) {
        if (n == 0)
            return 1;
        double v = power(x, n / 2);
        if (n % 2 == 0)
            return v * w;
        else 
            return v * v * w;
    }
};