/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int dfs(Employee* emp,unordered_map <int, Employee*> mpp) {
        int ans = emp->importance;
        for (int id:emp->subordinates){
            ans += dfs(mpp[id],mpp);
        }
        return ans;

    }

    int getImportance(vector<Employee*> employees, int id) {
        Employee* req_employee = NULL;
        unordered_map <int, Employee*> mpp;
        for (auto i:employees){
            mpp.insert({i->id,i});
             if (i->id == id) {
                req_employee = i;
            }
        }
        // cout<<req_employee->id;

        return dfs(req_employee,mpp);

    };
};
