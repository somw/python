start_floor = '3'
end_floor = '7'
floor_last_number = ['01','02','03']
# 户室的尾号

start_floor_rooms = {301:[1,80], 302:[1,80], 303:[2,90]}
#初始楼层的模版数据

unit_rooms={}
unit_rooms[int(start_floor)] = start_floor_rooms
#创建一个字典
for floor in range(int(start_floor)+1,int(end_floor)+1):
    floor_rooms = {}
    for i in range(len(start_floor_rooms)):
        number = end_floor + floor_last_number[i]
        into = start_floor_rooms[int(start_floor+floor_last_number[i])]
        floor_rooms[int(number)] = into
    unit_rooms[floor] = floor_rooms
        #print(number)
        #print(into)

print(unit_rooms)