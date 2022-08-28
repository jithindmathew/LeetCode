// 349

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> ans;
        std::unordered_map <int, int> m;
        
        for (auto num : nums1) {
            m[num]++;
        }
        
        for (auto num : nums2) {
            if (m[num] > 0) {
                ans.push_back(num);
                m[num] = 0;
            }
        }
        return ans;
    }
};
