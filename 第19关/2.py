unit_rooms={ 3:{301:[1,80],302:[1,80],303:[2,90],304:[2,90]},
             4:{401:[1,80],402:[1,80],403:[2,90],404:[2,90]},
             5:{501:[1,80],502:[1,80],503:[2,90],504:[2,90]}
            }
for sub_dict in unit_rooms.values():
    for k,v in sub_dict.items():
        dire = ['', '南北', '东西']
        #print('户室：%d，朝向：%d，面积：%d'% (k,v[0],v[1]))
        print('户室：%d，朝向：%s，面积：%d'% (k,dire[v[0]],v[1]))