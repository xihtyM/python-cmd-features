import os, texteditor, dec, find, colorama
from turtle import update;
from py_console import console;

# Start functions

def updateDir():
	try:
		with open(os.getcwd()+"/vars/dir","r") as d:
			return d.read();
	except Exception as err:
		console.error("Error:",err);

# Start variables

class vars:
	directory = updateDir();

# Commands

def cmd(command):
	if(command[0:3] == "txt"):
		texteditor.MakeFile();
		return 0;
	if(command[0:2] == "cd"):
		try:
			path = command[2:].lstrip().replace(" ","\n").replace("\\","/").replace("/"," ").rstrip().replace(" ","/").replace("\n"," ").rstrip();
			if(len(path) < 1):
				console.error("Error: Path does not exist ('"+path+"').");
				return 1;
			if(os.path.exists(path)):
				with open(os.getcwd()+"/vars/dir","w") as d:
					d.write(path);
				vars.directory = updateDir();
				return 0;
			if(os.path.exists(vars.directory+"/"+path)):
				with open(os.getcwd()+"/vars/dir","w") as d:
					d.write(vars.directory+"/"+path);
				vars.directory = updateDir();
				return 0;
			console.error("Error: Path does not exist ('"+path+"').");
			return 1;
		except Exception as err:
			console.error("Error:",err);
			return 1;
	if(command[0:4] == "base"):
		firstDash = command.find("-");
		if(command.count("-") == 2): 
			_from = command[firstDash+1:command.find(" ",firstDash)];
			to = command[find.find(command,"-",1):command.find(" ",find.find(command,"-",1))];
		else:
			to = command[firstDash+1:command.find(" ",firstDash)];
			_from = -1;
		try:
			value = command[command.find("#")+1:];
			to,_from = int(to),int(_from);
		except Exception as err:
			console.error("Error:",err,"\nThis may be due to a syntax error, type '-base' for info.");
			return 1;
		try:
			if(_from != 10): value = dec.toDec(value, _from);
			print(dec.fromDec(int(value),to));
		except Exception as err:
			console.error("Error:",err,"\nThis may be due to a syntax error, type '-base' for info.");
			return 1;
		return 0;
	if(command[0:5] == "-base"):
		print(colorama.Fore.LIGHTBLACK_EX + "Try using (* means required):\n*base -[from] -[*to] #[*value]" + colorama.Fore.RESET);
		return 0;
	console.error("Command not found:",command);
	return 1;

# Main

def Main():
	while(1):
		i = input(vars.directory+">> ");
		cmd(i);
Main();
