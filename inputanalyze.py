def get_name():
	first_name = input()
	last_name = input()
	return first_name, last_name

def set_name(name):
	return name[0] + " " + name[1]

fullname = set_name(get_name())
print(fullname)





