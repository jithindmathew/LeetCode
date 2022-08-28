class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool>ans;
        int maxx = max_element(candies);
        for(auto x : candies){
            if ((extraCandies + x)>= maxx){
                ans.push_back(true);
            }
            else{
                ans.push_back(false);
            }
        }
        return ans;
    }
    int max_element(vector<int>&vec){
        int max = vec[0];
        for(int i = 1; i < vec.size();i++){
            if(vec[i] > max){
                max = vec[i];
            }
        }
        return max;
    }
};