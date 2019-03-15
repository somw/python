import os
#list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

# with open(r'd:\python\第16关\poem.txt','r',encoding="utf-8") as f:
#     lines = f.readlines()

# with open(r'd:\python\第16关\new_poem.txt','w',encoding="utf-8") as new:
#     for line in lines:
#         if line in list_test:
#             new.write('____________。\n')
#         else:
#             new.write(line)
#path = "/python/第16关"
#dirs = os.listdir(path)
#for file in dirs:
#   print(file)

#mkdirs = os.mkdir('第16关/path')
a = os.path.isfile('1.py')
print(a)