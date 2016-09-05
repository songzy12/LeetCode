#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
	int minPathSum(vector<vector<int> > &grid) {
		const int m = grid.size();
		const int n = grid[0].size();

		vector<int> f(n, INT_MAX);
		f[0] = 0;

		for (int i = 0; i < m; ++i) {
			f[0] += grid[i][0]; 
			for (int j = 1; j < n; ++j) {
				f[j] = min(f[j - 1], f[j]) + grid[i][j];
				// f[j-1] is f[i][j-1], f[j] is f[i-1][j]
			}
		}
		return f[n - 1];
	}
};

/*class Solution {
public:
	int minPathSum(vector<vector<int> > &grid) {
		const int m = grid.size();
		const int n = grid[0].size();
		this->f = vector<vector<int> >(m, vector<int>(n, -1));
		return dfs(grid, m-1, n-1);
	}

private:
	vector<vector<int> > f;

	int dfs(const vector<vector<int> > &grid, int x, int y) {
		if (x < 0 || y < 0) return INT_MAX;
		if (x == 0 && y == 0)	return grid[0][0];
		return min(getOrUpdate(grid, x - 1, y), 
			getOrUpdate(grid, x, y - 1)) + grid[x][y];
	}

	int getOrUpdate(const vector<vector<int> > &grid, int x, int y) {
		if (x < 0 || y < 0) return INT_MAX;
		if (f[x][y] >= 0)	return f[x][y];
		return f[x][y] = dfs(grid, x, y);
	}
};*/