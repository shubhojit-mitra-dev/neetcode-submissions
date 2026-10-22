class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        const int n = static_cast<int>(strs.size());
        unordered_map<string, vector<string>> store;
        vector<vector<string>> result;

        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            store[key].push_back(s);
        }

        for (auto [_, v] : store) {
            result.push_back(v);
        }

        return result;
    }
};
