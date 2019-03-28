i = 2
j = 2
k = 2
n = 2
ls = [[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if x+y+z != n]
print(ls)