import os;
try:
	from py_console import console;
	from gcwd_ import getcwd;
except ImportError as err:
	print(err);

class play():
	def __init__(self, file):
		if(os.path.exists(file) and os.path.isfile(file)):
			
			return;
		console.error("Error: Path does not exist or path is not file.");
