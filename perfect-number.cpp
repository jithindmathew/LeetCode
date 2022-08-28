// 507

class Solution {
public:
    bool checkPerfectNumber(int num) {

        if (num == 1) {
            return false;
        }

        int anss = 0;

        for (int i = 2; i <= sqrt(num); i++) {
            if (num % i == 0) {
                anss += i;
                if (i * i != num) {
                    anss += num / i;
                }
            }
        }
        anss++;
        return num == anss ? true : false;
    }
};
