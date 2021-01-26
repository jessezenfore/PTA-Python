"""阶梯电价
为了提倡居民节约用电，某省电力公司执行“阶梯电价”，
安装一户一表的居民用户电价分为两个“阶梯”：月用电量50千瓦时（含50千瓦时）以内的，
电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，电价上调0.05元/千瓦时。
请编写程序计算电费。
"""
"""在一行中输出该用户应支付的电费（元），
结果保留两位小数，格式如：“cost = 应付电费值”；
若用电量小于0，则输出"Invalid Value!"。
"""

use = int(input())  # 单位kWh
cost = 0

if use <= 50:
    if use < 0:
        print("Invalid Value!")
    else:
        cost = 0.53 * use
        print("cost = {0:.2f}".format(cost))
else:
    cost = 0.05 * (use - 50) + 0.53 * use
    print("cost = {0:.2f}".format(cost))
