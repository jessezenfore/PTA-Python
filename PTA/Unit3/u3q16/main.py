"""第3章-16 删除重复字符 (20point(s))
本题要求编写程序，
将给定字符串去掉重复的字符后，
按照字符ASCII码顺序从小到大排序后输出。

输入格式：
输入是一个以回车结束的非空字符串（少于80个字符）。

输出格式：
输出去重排序后的结果字符串。

输入样例：
ad2f3adjfeainzzzv
输出样例：
23adefijnvz"""


text = input()
textNew = []

for i in text:
    if i not in textNew:
        textNew.append(i)
textNew.sort()

print(''.join(textNew))
