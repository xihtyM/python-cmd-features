# Find nth occurence in a string

def find(text,tofind,occurences):
	start = 0;
	while(occurences >= 0):
		start = text.find(tofind,start+len(tofind));
		occurences -= 1;
	return start+1;
