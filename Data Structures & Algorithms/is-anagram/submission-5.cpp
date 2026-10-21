class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> v(26, 0);
        for (const auto& c : s) v[c - 'a']++;
        for (const auto& c : t) v[c - 'a']--;
        for (const int& e : v) {
            if (e != 0) return false;
        }
        return true;
    }
};
