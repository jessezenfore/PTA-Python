"""第3章-12 求整数的位数及各位数字之和 (15point(s))
对于给定的正整数N，求它的位数及其各位数字之和。

输入格式：
输入在一行中给出一个不超过10^9 的正整数N。

输出格式：
在一行中输出N的位数及其各位数字之和，中间用一个空格隔开。

输入样例：
321
输出样例：
3 6"""

number = input()
numberIntSum = 0

for i in number:
    numberIntSum += int(i)

print(len(number), numberIntSum)
