// 455

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end(), greater<int>());
        sort(s.begin(), s.end(), greater<int>());

        int i = 0;
        int j = 0;
        int count = 0;

        while (i < s.size() && j < g.size()) {
            if (s[i] >= g[j]) {
                i++;
                j++;
                count++;
            } else if (s[i] < g[j]) {
                j++;
            }
        }

        return count;
    }
};
