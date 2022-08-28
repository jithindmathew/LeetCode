#include <bits/stdc++.h>

#define in(x) std::cin >> x
#define out(x) std::cout << x
#define outl(x) std::cout <<x<<std::endl

using namespace std;

int MinimumProductSum(vector <int> & vec1, vector <int> & vec2) {
    sort(vec1.begin(), vec1.end());
    sort(vec2.begin(), vec2.end(), greater<int>());

    int ans = 0;

    for (int i = 0; i < vec1.size(); i++) {
        ans += vec1[i]*vec2[i];
    }
    return ans;
}

int main(){
    vector<int> a = {2, 3, 4, 5};
    vector<int> b = {2, 3, 4, 5};

    int q = MinimumProductSum(a, b);

    outl(q);
    return 0;
}
