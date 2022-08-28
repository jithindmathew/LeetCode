// 1637

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        int ans;
        
        vector <int> v(points.size(), 0);
        
        for (int i = 0; i < points.size(); i++) {
            v[i] = points[i][0];
        }
        
        sort(v.begin(), v.end());
        
        if (v.size() == 1) {
            return 0;
        }
        
        ans = v[1] - v[0];
        
        for (int i = 1; i < v.size() - 1; i++) {
            ans = max(ans, v[i + 1] - v[i]);
        }
        return ans;
    }
};
