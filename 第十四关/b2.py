import random
import time

# 创建一个类，可实例化成具体的游戏角色
class Role():
    def __init__(self,name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):   # 把子类角色名作为默认参数
        Role.__init__(self,name)  # 利用了父类的初始化函数
        self.life = self.life*5  # 骑士有5份血量
        self.attack = self.attack*3    # 骑士有3份攻击力

class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life = self.life*3
        self.attack = self.attack*5

class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life = self.life*4
        self.attack = self.attack*4
        
# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game:
    def __init__(self):
        # 初始化各种变量
        self.players = []
        self.enemies = []
        self.score = 0
        # 执行各种游戏函数
        self.game_start()
        self.born_role()
        self.show_role()

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“PK小游戏” ------------')
        print('将自动生成【玩家角色】和【电脑人物】')
        input('请按回车键继续。')
    
    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(),Assassin(),Bowman()])) # 使用random.choice(列表)可以从列表中随机抽取一个元素
            self.enemies.append(random.choice([Knight(),Assassin(),Bowman()]))

    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print( '『我方』%s 血量：%s  攻击：%s'%
            (self.players[i].name,self.players[i].life,self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s'%
            (self.enemies[i].name,self.enemies[i].life,self.enemies[i].attack))
        print('--------------------------------------------')


gp = Game()  # 运行游戏