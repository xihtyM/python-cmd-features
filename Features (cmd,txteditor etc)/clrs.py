import os;
os.system("");
# COLOR RGB

def rgbcolor(r,g,b,txt,end=None):
	r,g,b = str(r),str(g),str(b);
	if(end == ""): return f'\u001b[38;2;{r};{g};{b}m'+txt;
	return f'\u001b[38;2;{r};{g};{b}m'+txt+"\u001B[0m";
