#!/usr/bin/env python3


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # non-negative integers num1 and num2

        m, n = len(num1), len(num2)
        # 初始化结果数组
        result = [0] * (m + n)

        # 反向遍历每一位
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 转为 int
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                mul = digit1 * digit2
                # 加到对应位置
                p1, p2 = i + j, i + j + 1
                # print(f"p1:{p1}\tp2:{p2}")
                # 累加乘积和当前位置的值
                total = mul + result[p2]

                result[p2] = total % 10  # 当前位
                result[p1] += total // 10  # 进位

        # 拼接字符串并去掉前导零
        res_str = "".join(map(str, result)).lstrip("0")
        # print(result)
        return res_str if res_str else "0"
