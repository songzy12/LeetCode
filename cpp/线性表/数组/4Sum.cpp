#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
  public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int> > result;
        if (num.size() < 4) 
            return result;
        sort(num.begin(), num.end());
        
        unordered_multimap<int, pair<int, int> > cache;
        for (int i = 0; i + 1 < num.size(); ++i) 
            for (int j = i + 1; j < num.size(); ++j)
                cache.insert(make_pair(num[i]+num[j], make_pair(i, j)));
            
        for (auto i = cache.begin(); i != cache.end(); ++i) {
            int x = target - i->first;
            auto range = cache.equal_range(x);
            for (auto j = range.first; j != range.second; ++j) {
                auto a = i->second.first;
                auto b = i->second.second;
                auto c = j->second.first;
                auto d = j->second.second;
                if (a != c && a != d && b != c && b != d) {
                    vector<int> vec = {num[a], num[b], num[c], num[d]};
                    sort(vec.begin(), vec.end());
                    result.push_back(vec);
                }
            }
        }
            
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result;
    }
};

/*class Solution {
  public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int> > result;
        if (num.size() < 4) 
            return result;
        sort(num.begin(), num.end());
        
        unordered_map<int, vector<pair<int , int> > > cache;
        for (size_t a = 0; a < num.size(); ++a) {
            for (size_t b = a + 1; b < num.size(); ++b) {
                cache[num[a] + num[b]].push_back(pair<int, int>(a, b));
            }
        }
        
        for (int c = 0; c < num.size(); ++c) {
            for (size_t d = c + 1; d < num.size(); ++d) {
                const int key = target - num[c] - num[d];
                if (cache.find(key) == cache.end())
                    continue;
                const auto& vec = cache[key];
                for (size_t k = 0; k < vec.size(); ++k) {
                    if (c <= vec[k].second) // to keep order, reduce duplicate 
                        continue;
                    result.push_back({num[vec[k].first], num[vec[k].second], num[c], num[d]});
                }
            }
        }
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result;
    }
};*/

int main() {
    vector<int> num({1, 0, -1, 0, 2, -2});
    int target = 0;
    vector<vector<int> > result = Solution().fourSum(num, target);
    for (int i = 0; i < result.size(); ++i) {
        for (int j = 0; j < result[i].size(); ++j) {
            cout<<result[i][j]<<" ";
        }
        cout<<endl;
    }
}