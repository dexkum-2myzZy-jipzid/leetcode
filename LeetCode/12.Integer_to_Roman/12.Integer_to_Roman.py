#!/usr/bin/env python3


class Solution:
    def intToRoman(self, num: int) -> str:
        # 1. 准备映射表（从大到小）
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = []  # 用列表累计字符，最后 join 提高效率
        i = 0

        # 2. 贪心遍历
        while num > 0:
            # 计算当前符号能使用的次数
            count = num // vals[i]
            if count:
                # 拼接对应次数的符号
                res.append(syms[i] * count)
                # 减去对应的数值
                num -= vals[i] * count
            i += 1  # 处理下一个较小符号

        # 3. 返回拼接结果
        return "".join(res)
