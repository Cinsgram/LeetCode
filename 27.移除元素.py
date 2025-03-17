#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i , j , k = 0, 0, 0
        while i <= len(nums) - 1:
            if nums[i] == val : j += 1
            else : 
                nums[k] = nums[i]
                k += 1
            i += 1
        return (len(nums) - j)

# @lc code=end

