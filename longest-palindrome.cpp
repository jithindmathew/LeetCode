// 409

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> mpp;
        for (char i : s) {
            mpp[i]++;
        }

        int ans = 0;
        bool flag = false;

        for(auto x : mpp) {
            if (x.second % 2 == 0) {
                ans += x.second;
            } else {
                ans += x.second - 1;
                flag = true;
            }
        }

        if (flag) {
            ans++;
        }

        return ans;
    }
};
