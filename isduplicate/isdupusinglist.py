s = "fish"
l = [False] * 128
i = 0
re = "No dup"
while i < len(s):
	if l[ord(s[i])] == True:
		re = "dup"
		break;
	else:
		l.insert(ord(s[i]), s[i])
	i += 1
print(re)