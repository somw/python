file1 = open('D:\\python\\test\\scores.txt','r',encoding='utf-8')
files_lines = file1.readlines()
file1.close()
final_scores = []

for i in files_lines:
    data = i.split()
    num = 0
    for score in data[1:]:
        num = num + int(score)
    result = data[0] + str(num) + '\n'
    final_scores.append(result)

file2 = open('D:\\python\\test\\writing.txt','a',encoding='utf-8')
file2.writelines(final_scores)
file2.close()