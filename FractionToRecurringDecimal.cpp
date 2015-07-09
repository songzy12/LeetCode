#include<iostream>
#include<string>
#include<ctime>
#include<iomanip>
#include<map>
using namespace std;
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
		if (numerator == 0)
			return "0";
        string result = "";
		if ((numerator < 0) ^ (denominator < 0))
			result += "-";
		
		// just turn n, d to the absolute value
		long long n = llabs(numerator);
		long long d = llabs(denominator);
		long long q = n / d;
		long long r = n % d;
		
		result += to_string(q);
		if (r==0)
			return result;
		result += ".";
		
		//int* r2 = new int[denominator];
		map<long long, long long> r2;
		/*for(int i=0; i<denominator; i++)
			r2[i]=0;*/
		
		int counter = 0;
		r2[r] = ++counter;
		string temp = "";
		while(r!=0){
			/*for (int i=0; i<denominator; i++)
				cout<<r2[i];
			cout<<endl;*/
			q = r * 10 / d;
			r = r * 10 % d;
			temp += to_string(q);
			if (r2.count(r)!=0)
				break;
			/*if (r2[r] != 0)
				break;*/
			r2[r] = ++counter;
		}
		
		if (r == 0)
			result += temp;
		else
			result += temp.substr(0, r2[r] - 1) + "(" + temp.substr(r2[r] - 1, temp.size()) + ")";
		//delete r2;
		return result;
    }
};

int main(){
	/*srand((unsigned)time(NULL));
	int n, d;
	for(int i=0; i<20; i++){
		n = -rand()%100, d = rand()%100;
		if(d == 0) 
			continue;
		cout<< n << " " << d << endl;
		cout<< Solution().fractionToDecimal(n, d)<<endl;
		cout<<setprecision(40)<< n*1.0/d << endl;
	}*/

	//cout<<Solution().fractionToDecimal(1, 214748364);
	//cout<<Solution().fractionToDecimal(-1, -2147483647-1);
	//cout<<Solution().fractionToDecimal(-2147483647-1, 1);
	cout<<Solution().fractionToDecimal(0, -5);
	system("pause");
	return 0;
}