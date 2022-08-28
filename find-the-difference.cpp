// 389

class Solution {
public:
    char findTheDifference(string s, string t) {
        int ssum = 0;
        int tsum = 0;
        
        for (char i : s) {
            ssum += i - 'a';
        }
        
        for (char i : t) {
            tsum += i - 'a';
        }
        
        return tsum - ssum + 'a';
            
    }
};
