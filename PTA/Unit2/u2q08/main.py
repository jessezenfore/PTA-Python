"""
输入一个整数和进制，转换成十进制输出

输入格式:
在一行输入整数和进制

输出格式:
在一行十进制输出结果

输入样例:
在这里给出一组输入。例如：

45,8
输出样例:
在这里给出相应的输出。例如：

37
"""
n, a = input().split(",")
a = int(a)
c = int(n, a)

print(c)