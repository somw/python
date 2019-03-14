import random

# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

# 创建3个子类，可实例化为3个不同的职业

class Knight(Role):
    def __init__(self, name='【圣光骑士】'):   # 把子类角色名作为默认参数
        Role.__init__(self,name)  # 利用了父类的初始化函数
        self.life = self.life*5  # 骑士有5份血量
        self.attack = self.attack*3    # 骑士有3份攻击力

    def fight_buff(self,opponent):
        if opponent.name == '【暗影刺客】':
            self.attack = int(self.attack*1.5)

class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life = self.life*3
        self.attack = self.attack*5

    def fight_buff(self,opponent):
        if opponent.name == '【精灵弩手】':
            self.attack = int(self.attack*1.5)

class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life = self.life*4
        self.attack = self.attack*4

    def fight_buff(self,opponent):
        if opponent.name == '【圣光骑士】':
            self.attack = int(self.attack*1.5)

Knight = Knight()  # 实例化骑士
Assassin = Assassin()  # 实例化刺客
Bowman = Bowman()  # 实例化弩手

print('骑士的攻击力是：' + str(Knight.attack))
Knight.fight_buff(Assassin)  # 调用“战斗强化”函数
print('遇到刺客，骑士的攻击力是：' + str(Knight.attack))

print('刺客的攻击力是：' + str(Assassin.attack))
Assassin.fight_buff(Bowman)  # 调用“战斗强化”函数
print('遇到弩手，骑士的攻击力是：' + str(Assassin.attack))

print('弩手的攻击力是：' + str(Bowman.attack))
Bowman.fight_buff(Knight)  # 调用“战斗强化”函数
print('遇到骑士，弩手的攻击力是：' + str(Bowman.attack))