class Solution {
    
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        vector<vector<bool>> visited;
        vector<vector<int>> dist;
        queue<pair<int, int> > q;

        int n = matrix.size();
        if (!n)
            return matrix;
        int m = matrix[0].size();
        for (int i = 0; i <n; ++i) {
            vector<bool> temp_visited;
            vector<int> temp_dist;
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] == 0) {
                    q.push({i, j});
                    temp_visited.push_back(true);
                    temp_dist.push_back(0);
                } else {
                    temp_visited.push_back(false);
                    temp_dist.push_back(20000);
                }
            }
            visited.push_back(temp_visited);
            dist.push_back(temp_dist);
        }
        int cur_dist = 0;
        while (!q.empty()) {
            cur_dist++;
            queue<pair<int,int> > p;
            while (!q.empty()) {
                pair<int, int> temp = q.front(); q.pop();
                int x = temp.first, y = temp.second;
                int dx_[] = {-1, 1, 0, 0};
                int dy_[] = {0, 0, -1, 1};
                for (int i = 0; i < 4; ++i) {
                    int dx = dx_[i], dy = dy_[i];
                    if (x+dx >= 0 && x+dx < n && y+dy >= 0 && y+dy < m && !visited[x+dx][y+dy]) {
                        visited[x+dx][y+dy] = true;
                        dist[x+dx][y+dy] = cur_dist;
                        p.push({x+dx, y+dy});
                    }
                }
            }
            q = p;        
        }
        
        return dist;
    }
};