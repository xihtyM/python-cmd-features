try:
	import sys;
	from playsound import playsound;
except ImportError as err:
	print("Error",err);

class __playsound__:
	def __init__(self, argv):
		print(argv);
		playsound(argv[0]);

__playsound__(sys.argv[1:]);
