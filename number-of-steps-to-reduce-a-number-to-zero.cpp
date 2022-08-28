class Solution {
public:
    int numberOfSteps (int num) {
        int ans = 0;
        while (num != 0){
            if(num%2==0){
                return (ans + 1) + numberOfSteps(num/2);
            }
            else{
                return (ans + 1) + numberOfSteps(num- 1);
            }
        }
        return 0;
    }
};