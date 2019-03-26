import csv

with open(r'D:/python/第19关/assets.csv','a',newline='',encoding='gbk') as csvfile:
    writer = csv.writer(csvfile,dialect='excel')
    # 用csv.writer函数创建一个writer对象
    header = ['小区名称','地址','建筑年份','楼栋','单元','户室','朝向','面积']
    writer.writerow(header)

    title = input('请输入小区名称：')
    address = input('请输入小区地址：')
    year = input('请输入小区建造年份：')
    block = input('请输入楼栋号：')

# 定义循环控制量
unit_loop = True
while unit_loop:
    unit = input('请输入单元号：')
    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')

    # 开始输入模板数据
    input('接下来输入起始层每个房间的牌号、南北朝向及面积，按任意键继续')

    strat_floor_rooms = {}
    floor_last_number = []
    # 收集起始层的房间信息

    room_loop = True
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号：（比如01、02）')
        #将尾号用append函数添加到列表里
        floor_last_number.append(last_number)
        # 户室号为room_number, 由楼层start_floor 和 尾号last_number 组成，如301
        room_number = int(start_floor + last_number)

        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number))
        area = int(input('请输入 %d 的面积，单位为m2:' % room_number))
        strat_floor_rooms[room_number] = [direction,area]
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里
        #print(strat_floor_rooms)
        continued = input('是否继续输入下一个尾号？按 n 停止输入， 按其他任意键继续：')
        #加入打破循环的条件
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True

    unit_rooms ={}
    unit_rooms[start_floor] = strat_floor_rooms
    for floor in range(int(start_floor)+1,int(end_floor)+1):
        floor_rooms = {}
        for i in range(len(strat_floor_rooms)):
            number = str(floor) + floor_last_number[i]
            into = strat_floor_rooms[int(start_floor + floor_last_number[i])]
            floor_rooms[int(number)] = into
        unit_rooms[floor] = floor_rooms

    with open(r'D:/python/第19关/assets.csv','a',newline='',encoding='gbk') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        for sub_dict in unit_rooms.values():
            for room,into in sub_dict.items():
                dire = ['','南北','东西']
                writer.writerow([title,address,year,block,unit,room,dire[into[0]],into[1]])
    unit_continued = input('是否继续输入下一个单元？按 n 停止输入， 按其他任意键继续：')
    if unit_continued == 'n':
        unit_loop = False
    else:
        unit_loop = True

print('恭喜你，资产录入工作完成！')  