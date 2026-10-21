class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // size_t n = nums.size();
        unordered_map<int, int> myMap;
        // myMap.reserve(n);
        for (int i = 0; i < nums.size(); ++i) {
            int comp = target - nums[i];
            if (myMap.contains(comp)) 
                return {myMap[comp], i};
            myMap[nums[i]] = i;
        }
        return {};
    }
};
