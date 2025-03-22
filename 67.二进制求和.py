#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stackcarry, stackresult = [], []
        if len(a) > len(b) :
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b) :
            a = '0' * (len(b) - len(a)) + a
        stackcarry.append(0)
        for chara, charb in zip(reversed(a), reversed(b)) :
            k = stackcarry.pop()
            sum_val = int(chara) + int(charb) + k
            carry = sum_val // 2
            current = sum_val % 2
            stackcarry.append(carry)
            stackresult.append(str(current))
        k = stackcarry.pop()
        if k == 1 :
            stackresult.append('1')
        output = "".join(reversed(stackresult))
        return output
# @lc code=end

