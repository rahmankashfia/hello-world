#suppose given string = "google", return true if dup else false

#two sol

#1) if string is only alpha 26...with case 52 
#2) string alpha numareic
#3) any char


#read ascii

s = "gogle"
st = set()
ls = list()

for x in range(len(s)):
	print(s[x])
	st.add(s[x])

print(st)

def isdup(st):
	x = 0
	while x < len(st):
		if st[x] in ls:
			return True
		else:
			ls.append(st[x])
		x += 1
	return False

def test1(st):
	if st in ["google","gogle"]:
		return True
	if st == "fish":
		return False

result = isdup(s)
if result == True:
	print("has duplicate")
else:
	print("no dup")

if test1(s) == result:
	print("test1 is passed")
else:
	print("test1 is not passed")
