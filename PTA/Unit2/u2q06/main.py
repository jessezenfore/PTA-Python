"""
本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。

输入格式:
输入在一行中给出一个正整数N。

输出格式:
在一行中输出部分和的值，结果保留三位小数。

输入样例:
5
输出样例:
0.917

"""

n = int(input())
s = 0

for i in range(1, n + 1):
    s = s + (i / (2 * i - 1)) * pow(-1, i + 1)

print("{0:.3f}".format(s))