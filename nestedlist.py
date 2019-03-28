f = open("input.txt")
count = int(f.readline())
i = 0
ls = []
while count != 0:
	temp = []
	temp.append(f.readline().strip())
	temp.append(f.readline().strip())
	ls.append(temp)
	count -= 1
grade = []
for x in ls:
	grade.append(float(x[1]))
minimum = min(grade)
while minimum in grade:
	grade.remove(minimum)
minimum = min(grade)
for x in ls:
	if(x[1] == str(minimum)):
		print(x[0])
