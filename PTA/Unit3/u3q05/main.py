"""第3章-5 字符转换 (15point(s))
本题要求提取一个字符串中的所有数字字符（'0'……'9'），将其转换为一个整数输出。

输入格式：
输入在一行中给出一个不超过80个字符且以回车结束的字符串。

输出格式：
在一行中输出转换后的整数。题目保证输出不超过长整型范围。

输入样例：
free82jeep5
输出样例：
825
"""
"""
for i in input():
    if i.isdigit():
        print(int(i),end='')
比如000000012会写成12，要把前面的0省略
"""
text = input()
number = []

for i in text:
    if i.isdigit():
        number.append(i)
print(int("".join(number)))