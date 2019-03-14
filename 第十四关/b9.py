import random

player_list = ['【圣光骑士】','【暗影刺客】','【精灵弩手】']
players = []

for i in range(3):
    player = random.choice(player_list)
    players.append(player)

print(players)

# 判断方式1：比较运算符

# 角色类型都一样
if players[0] == players[1] == players[2]:
    print('我们都一样！——方式1')  # 在打印结果中加上“方式N”，验证不同的判断方式的有效性。

# 角色类型都不一样
if players[0] != players[1] and players[0] != players[2] and players[1] != players[2]:
    print('我们都不一样！——方式1')

# 判断方式2：set()
# 集合（set）是一个无序的不重复元素序列，set()可以去重，然后生成一个集合。

players_set = set(players)

# 角色类型都一样&角色类型都不一样
if len(players_set) == 1:
    print('我们都一样！——方式2')
elif len(players_set) == 3:
    print('我们都不一样！——方式2')

# 其他判断方式

'''
除了上面两种方式外，还有很多方式可以考虑：

例如：类似判断方式2，可以新建一个列表，用 append 添加不重复的角色类型，然后看这个列表的长度是多少（类似判断方式2）。
再如：“角色类型完全不一样”，可先将players和player_list按相同的排序方式排一下，再判断两个排序后的列表是否相同。

总而言之：只要你愿意思考、尝试和搜索，就可以得出各种不同的判断方式。
'''

# 再举一个例子：
if sorted(players) == sorted(player_list):
    print('我们都不一样！——方式3')
else:
    pass