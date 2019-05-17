import random

guess =''

while guess not in ['正面','反面']:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

    # print(guess)

    #随机抛硬币，0代表反面，1代表正面
    # toss = str(random.randint(0,1))
    # print(type(toss))
     
    toss = random.choice(['正面','反面'])


    if toss == guess:
        print('猜对了！你真棒')
        break
    else:
        print('没猜对，你还有一次机会。')
        guess = input('再输一次“正面”或“反面”：')
        if toss == guess:
            print('你终于猜对了！')
            break
        else:
            print('大失败！')