import random
class Role():
    def __init__(self,name = '【普通角色】'):
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

class Knight(Role): 
    def __init__(self,name = '【圣光骑士】'):
        Role.__init__(self,name)
        self.life = self.life*5
        self.attack = self.attack*3

class Assassin(Role):
    def __init__(self,name = '【暗影刺客】'):
        Role.__init__(self,name)
        self.life = self.life*3
        self.attack = self.attack*5

class Bowman(Role):
    def __init__(self,name = '【精灵弩手】'):
        Role.__init__(self,name)
        self.life = self.life*4
        self.attack = self.attack*4


a = Role()
b = Knight()
c = Assassin()
d = Bowman()
list1 = [a,b,c,d]
for i in list1:
    print(i.name + '的血量是' + str(i.life) + '；攻击力是' + str(i.attack))
