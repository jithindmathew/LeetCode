class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int count = 0;
        unordered_set<char> sett;
        for(auto i : jewels){
            sett.insert(i);
        }
        for(auto j : stones){
            if (sett.find(j) != sett.end()){
                count++;
            }
        }
        return count;
    }
};