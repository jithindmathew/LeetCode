class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string ans = s;
        for(int i = 0; i<s.length(); i++){
            int num = indices[i];
            ans[num] = s[i];
        }
        return ans;
        
    }
};