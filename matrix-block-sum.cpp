//1314

class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        
        std::vector<std::vector<int>> ans(m, std::vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x1 = max(0, i - k);
                int x2 = min(m - 1, i + k);
                int y1 = max(0, j - k);
                int y2 = min(n - 1, j + k);
                int anss = 0;

                for (int p = x1; p <= x2; p++) {
                    for (int q = y1; q <= y2; q++) {
                        anss += mat[p][q];
                    }
                }

                ans[i][j] = anss;
            }
        }
        return ans;
    }
};
