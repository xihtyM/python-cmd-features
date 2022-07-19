import os;
try:
	from py_console import console;
	from gcwd_ import getcwd;
	import subprocess;
except ImportError as err:
	print(err);

class play():
	def __init__(self, file: str):
		if(os.path.exists(file) and os.path.isfile(file)):
			subprocess.call(f"py \"{os.getcwd()}\\__playsound__.py\" \"{file}\"");
			return;
		console.error("Error: Path does not exist or path is not file.");
