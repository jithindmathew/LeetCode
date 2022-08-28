class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        std::vector <int > vec;
        vec.push_back(first);
        for(int i = 0; i < encoded.size();i++)
        {
            first = encoded[i]^vec[i];
            vec.push_back(first);
        }
        return vec;
    }
};