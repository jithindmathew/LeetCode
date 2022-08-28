class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector <int> vec;
        for(auto x : accounts){
            int sum = 0;
            for(auto y : x){
                sum += y;
            }
            vec.push_back(sum);
        }
        return *max_element(vec.begin(), vec.end());
    }
};