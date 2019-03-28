
def add_space(x):
	 

print("start")

txt = "Hello World"
y = len(txt)

for z in range(y, 0, -1):
	print("-----------------------------------------------")
	for x in range(0, z):
  		print("txt[{}:{}]  {}".format(x, z, txt[x:z]))


print("this is txt[3:3] \"{}\" ".format(txt[3:3]))





