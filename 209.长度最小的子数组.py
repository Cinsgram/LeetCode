#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, sum, minlen = 0, 0, 0, 0
        while sum < target :
            if j == len(nums) : return 0
            sum += nums[j]
            j += 1
        minlen = j
        while sum >= target:
            if j <= len(nums) - 1 : 
                sum += nums[j]
                j += 1
            while sum >= target :
                sum -= nums[i]
                i += 1
                if sum < target : 
                    i -= 1
                    sum += nums[i]
                    break
                if minlen > j - i : minlen = j - i
            if j == len(nums) : break
        return minlen
        
# @lc code=end

