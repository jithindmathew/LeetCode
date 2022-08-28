// 1380

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {

        unordered_set<int> seen;
        std::vector<int> ans;

        for (auto i : matrix) {
            seen.insert(*std::min_element(i.begin(), i.end()));
        }

        int m = matrix.size();
        int n = matrix[0].size();

        for (int i = 0; i < n; i++) {
            int maxi = INT_MIN;
            for (int j = 0; j <m; j++) {
                maxi = max(maxi, matrix[j][i]);
            }
            if (seen.find(maxi) != seen.end()) {
                ans.push_back(maxi);
            }
        }
        return ans;
    }
};
