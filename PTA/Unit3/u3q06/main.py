"""第3章-6 求整数序列中出现次数最多的数 (15point(s))
本题要求统计一个整型序列中出现次数最多的整数及其出现次数。

输入格式：
输入在一行中给出序列中整数个数N（0<N≤1000），以及N个整数。数字间以空格分隔。

输出格式：
在一行中输出出现次数最多的整数及其出现次数，数字间以空格分隔。题目保证这样的数字是唯一的。

输入样例：
10 3 2 -1 5 3 4 3 0 3 2
输出样例：
3 4"""

number = list(map(int, input().split()))
count = {}
t = number[1: number[0]+1]
for i in t:
    count[i] = count.get(i, 0) + 1
items = list(count.items())
items.sort(key=lambda x: x[1], reverse=True)
i, count = items[0]
print(i, count)
"""res = []
counts = {}
lst = list(map(int,input().split()))
t = lst[1: lst[0]+1]
for word in t:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
word, count = items[0]
print ("{:d} {:d}".format(word, count))y
"""