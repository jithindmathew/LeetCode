class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector <int> a(102);
        vector<int> ans;
        int n = nums.size();
        for(int i = 0; i< n; i++){
            a[nums[i]]++;
        }
        for(int i = 0; i<n;i++){
            int total = 0;
            for(int j = 0; j <nums[i];j++){
                total += a[j];
                
            }
            ans.push_back(total);
        }
        return ans;
    }
};
