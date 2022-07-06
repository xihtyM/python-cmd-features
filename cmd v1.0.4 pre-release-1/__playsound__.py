try:
	import sys;
	import pygame;
except ImportError as err:
	print("Error",err);

class __playsound__:
	def __init__(self, argv):
		pygame.init();
		pygame.mixer.init();
		sound = pygame.mixer.Sound(argv[0]);
		sound.set_volume(0.5);
		sound.play(1);

__playsound__(sys.argv[1:]);
