import statistics as np

f = open("dicinput.txt")
count = int(f.readline())
ls = {}
for x in range(0,count):
	temp = f.readline().split(" ")
	templs = [float(x) for x in temp[1:]]
	ls[temp[0]] = templs
name = f.readline()
print("{:.2f}".format(sum(ls.get(name))/3))
print(format(np.mean(ls.get(name)),".2f"))
#print(a)
#print(float(a,2))
print(ls)
print(name)



