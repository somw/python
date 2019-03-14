import random

# 创建一个类，可实例化成具体的游戏角色
class Role():
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name

# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):   # 把子类角色名作为默认参数
        Role.__init__(self,name)  # 利用了父类的初始化函数

class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self,name)

class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self,name)


def born_role():
    for i in range(3):
        players.append(random.choice([Knight(),Assassin(),Bowman()]))
        enemies.append(random.choice([Knight(),Assassin(),Bowman()]))

# 准备空列表
players = []
enemies = []

# 运行函数
born_role()

# 打印信息，看看列表players和enemies分别存了什么
print(players)
print(enemies)