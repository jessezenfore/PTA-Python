"""

第3章-22 输出大写英文字母 (15point(s))
本题要求编写程序，
顺序输出给定字符串中所出现过的大写英文字母，
每个字母只输出一遍；
若无大写英文字母则输出“Not Found”。

输入格式：
输入为一个以回车结束的字符串（少于80个字符）。

输出格式：
按照输入的顺序在一行中输出所出现过的大写英文字母，
每个字母只输出一遍。若无大写英文字母则输出“Not Found”。

输入样例1：
FONTNAME and FILENAME
输出样例1：
FONTAMEIL
输入样例2：
fontname and filrname
输出样例2：
Not Found

"""


text = input()
upperLib = []

for i in text:
    if i.isupper() and i not in upperLib:
        upperLib.append(i)
        print(i, end='')
if len(upperLib) < 1:
    print("Not Found")
