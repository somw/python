import csv
with open(r'd:\python\第16关\test.csv','a',newline='',encoding='gbk') as f:
    writer = csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])