//575

class Solution {
public:
    int distributeCandies(vector<int>& can) {
        std::unordered_set <int> s;
        int n = can.size() / 2;

        for (int i = 0; i < can.size(); i++) {
            s.insert(can[i]);
        }
        return s.size() > n ? n:s.size();
    }
};
