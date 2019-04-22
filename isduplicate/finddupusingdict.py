s = "google"
sd = dict()

for x in range(len(s)):
	sd.update({s[x]:sd.get(s[x], 0) + 1})

l = [item for item in sd if sd.get(item) > 1]

print(l) 

