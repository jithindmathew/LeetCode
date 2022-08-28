class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map<int,int> mpp;
        map<int, int> :: iterator iter;
        int count = 0;
        for(int i = 0; i < nums.size();i++){
            mpp[nums[i]]++;
        }
        for(iter = mpp.begin(); iter != mpp.end();iter++){
            int n = (*iter).second;
            count += (n)*(n-1)/2;
        }
        return count;
    }
};