// 476

class Solution {
public:
    int findComplement(int num) {
        if (!num) {
            return 1;
        }

        int x = 1;

        while (num > x) {
            x = 1 + 2 * x;
        }

        return abs(num - x);
    }
};
