import os;
try:
	from playsound import playsound;
	from py_console import console;
except ImportError as err:
	print(err);

class play():
	def __init__(self, file):
		if(os.path.exists(file) and os.path.isfile(file)):
			playsound(file);
			return;
		console.error("Error: Path does not exist or path is not file.");

#def playsound(file):
#	if(os.path.exists(file) and os.path.isfile(file)):
#		playsound(file);
#		return 0;
#	console.error("Error: Path does not exist or path is not file.");
#	return 1;
