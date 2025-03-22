#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i, j, n1, n2 = 0, 0, 0, 0
        for char in reversed(num1) :
            n1 += int(char) * pow(10, i)
            i += 1
        for char in reversed(num2) :
            n2 += int(char) * pow(10, j)
            j += 1
        result = n1 * n2
        return str(result)
# @lc code=end

