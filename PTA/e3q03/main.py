"""第3章-3 输出字母在字符串中位置索引 (20point(s))
输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。

输入格式:
第一行输入字符串
第二行输入两个字符，用空格分开。

输出格式:
反向输出字符和索引，即最后一个最先输出。每行一个。

输入样例:
在这里给出一组输入。例如：

mississippi
s p
输出样例:
在这里给出相应的输出。例如：

9 p
8 p
6 s
5 s
3 s
2 s"""


text = input()
letter1, letter2 = input().split()

for i in range(len(text)-1, -1, -1):
    if text[i] == letter1 or text[i] == letter2:
        print(i, text[i])
