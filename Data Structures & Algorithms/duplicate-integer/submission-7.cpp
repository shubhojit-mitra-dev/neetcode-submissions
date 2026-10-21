class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Strict O(1) space sorting (No O(log n) recursion stack!)
        std::make_heap(nums.begin(), nums.end());
        std::sort_heap(nums.begin(), nums.end());
        
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) return true;
        }
        return false;
    }
};