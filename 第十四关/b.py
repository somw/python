import random
class Role():
    def __init__(self):
        self.name = '【普通角色】'
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

class Knight(Role): 
    def __init__(self):
        self.name = '【圣光骑士】'
        self.life = random.randint(100,150)*5
        self.attack = random.randint(30,50)*3

class Assassin(Role):
    def __init__(self):
        self.name = '【暗影刺客】'
        self.life = random.randint(100,150)*3
        self.attack = random.randint(30,50)*5

class Bowman(Role):
    def __init__(self):
        self.name = '【精灵弩手】'
        self.life = random.randint(100,150)*4
        self.attack = random.randint(30,50)*4


a = Role()
print(a.name + '的血量是' + str(a.life) + '；攻击力是' + str(a.attack))

b = Knight()
print(b.name + '的血量是' + str(b.life) + '；攻击力是' + str(b.attack))

c = Assassin()
print(c.name + '的血量是' + str(c.life) + '；攻击力是' + str(c.attack))

d = Bowman()
print(d.name + '的血量是' + str(d.life) + '；攻击力是' + str(d.attack))