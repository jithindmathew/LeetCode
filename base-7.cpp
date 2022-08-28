// 504

class Solution {
public:
    string convertToBase7(int num) {
        
        bool isnegative;
        
        if (num < 0) {
            isnegative = true;
        } 
        else if (num == 0) {
            return "0";
        } 
        else {
            isnegative = false;
        }
        
        std::string ans = "";
        
        num = abs(num);
        
        while (num > 0) {
            ans = std::to_string(num % 7) + ans;
            num /= 7;
        }
        
        if (isnegative) {
            ans = "-" + ans;
        }
        
        return ans;
    }
};
