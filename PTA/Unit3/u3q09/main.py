"""第3章-9 字符串转换成十进制整数 (15point(s))
输入一个以#结束的字符串，
本题要求滤去所有的非十六进制字符（不分大小写），
组成一个新的表示十六进制数字的字符串，
然后将其转换为十进制数后输出。
如果在第一个十六进制字符之前存在字符“-”，
则代表该数是负数。

输入格式：
输入在一行中给出一个以#结束的非空字符串。

输出格式：
在一行中输出转换后的十进制数。题目保证输出在长整型范围内。

输入样例：
+-P-xf4+-1!#
输出样例：
-3905"""


# change
text = input()
textChanged = ""
dToH = '0123456789abcdefABCDEF'
for i in text:
    if i in dToH:
        textChanged += i
    if i == '#':
        break

# print
if textChanged == '':
    print('0')
elif text.find(textChanged[0]) > text.find('-'):
    print(-int(textChanged, 16))
else:
    print(int(textChanged, 16))
