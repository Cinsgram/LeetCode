#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        while i <= len(nums) - 1:
            nums[i] *= nums[i]
            i += 1
        nums.sort()
        return nums
# @lc code=end

