import random

player_list = ['【圣光骑士】','【暗影刺客】','【精灵弩手】']
players = []

for i in range(3):
    player = random.choice(player_list)
    players.append(player)

print(players)

# 判断方式1：比较运算符

# 职业都一样，两行代码



# 职业都不一样，两行代码



# 判断方式2：set()

# 补充知识：集合（set）是一个无序的不重复元素序列，set()可以去重，然后生成一个集合。
# 请你根据下面代码的运行结果，理解一下上面的话，然后现学现用~

list1 = [1,2,3]
list2 = [1,1,2]
print(set(list1))
print(set(list2))  # 去重，删去了重复的“1”。

players_set = set(players)  # 对生成的表格进行去重。
print(players_set)  # 打印出来验证一下。

# 职业都一样&职业都不一样，4行代码







# 其他判断方式

'''
除了上面两种方式外，还有很多方式可以考虑：
例如：类似判断方式2，可以新建一个列表，用 append 添加不重复的职业，然后看这个列表的长度是多少（类似判断方式2）。
再如：“职业完全不一样”，可先将players和player_list按相同的排序方式排一下，再判断两个排序后的列表是否相同。

if sorted(players) == sorted(player_list):
    print('我们都不一样！——方式3')
else:
    pass

总而言之：只要你愿意思考、尝试和搜索，就可以得出各种不同的判断方式。
'''