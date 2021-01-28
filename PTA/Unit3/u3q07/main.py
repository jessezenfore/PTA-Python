"""第3章-7 求最大值及其下标 (20point(s))
本题要求编写程序，找出给定的n个数中的最大值及其对应的最小下标（下标从0开始）。

输入格式:
输入在第一行中给出一个正整数n（1<n≤10）。第二行输入n个整数，用空格分开。

输出格式:
在一行中输出最大值及最大值的最小下标，中间用一个空格分开。

输入样例:
6
2 8 10 1 9 10
输出样例:
10 2"""


"""n = int(input())
number = list(map(int, input().split()))

maxNumber = number[0]
maxNumberId = 0

for i in range(1, n):
    if number[i] > maxNumber:
        maxNumber = number[i]
        maxNumberId = i

print(maxNumber, maxNumberId)
"""
n = int(input())
number = list(map(int, input().split()))
print(max(number), number.index(max(number)))
