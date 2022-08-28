//556

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int x = mat.size();
        int y = mat[0].size();
        int p = 0;
        int q = 0;

        if (x*y != r*c) {
            return mat;
        }

        std::vector<std::vector<int>> ans(r, std::vector<int>(c));

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                ans[p][q] = mat[i][j];
                q++;
                if (q == c) {
                    q = 0;
                    p++;
                }
            }
        }
        return ans;
    }
};
