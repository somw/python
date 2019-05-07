import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'mm'
sheet['A1'] = '明明'
row = [['爬虫1','爬虫2','爬虫3'],['爬虫4','爬虫5','爬虫6']]
for i in row:
    sheet.append(i)
print(row)
wb.save("mm.xlsx")