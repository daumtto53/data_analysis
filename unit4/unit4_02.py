import csv

f = open('C:\\Users\\MINSOO\\Documents\\데이터분석\\seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
result = []

for row in data :
	if row[-1] != '' :
		result.append(float(row[-1]))
print(result)
