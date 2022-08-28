class Solution
{
public:
    int countMatches(vector<vector<string>> &items, string ruleKey, string ruleValue)
    {
        int ans = 0;
        int idx;
        switch (ruleKey[0])
        {
        case ('t'):
            idx = 0;
            for (int i = 0; i < items.size(); i++)
            {
                if (items[i][idx] == ruleValue)
                {
                    ans++;
                }
            }
            return ans;
        case ('c'):
            idx = 1;
            for (int i = 0; i < items.size(); i++)
            {
                if (items[i][idx] == ruleValue)
                {
                    ans++;
                }
            }
            return ans;
        case ('n'):
            idx = 2;
            for (int i = 0; i < items.size(); i++)
            {
                if (items[i][idx] == ruleValue)
                {
                    ans++;
                }
            }
            return ans;
        }
        return 0;
    }
};