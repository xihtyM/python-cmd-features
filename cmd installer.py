VERSION_NAME = "v1.0.2";

try:
	import subprocess, sys, os, time;
except ImportError as err:
	print("There was an error importing:",err)
	time.sleep(2);
	quit();

# Get installed packages

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']);
installed_packages = [r.decode().split('==')[0] for r in reqs.split()];

try:
	if("pypiwin32" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypiwin32']);
	if("pywin32" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'win32con']);
	if("winshell" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'winshell']);
	if("colorama" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama']);
	if("py-console" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'py-console']);
	if("GitPython" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'GitPython']);
	if("gitdb" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitdb']);
	if("pypi" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypi']);
	if("requests" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests']);
	if("pytest-shutil" not in installed_packages):
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytest-shutil']);
except Exception as err:
	print(err);

try:
	import winshell, shutil;
except ImportError as err:
	print("There was an error importing:",err)
	time.sleep(2);
	quit();

try:
	from win32com.client import Dispatch;
except ImportError:
	print("Failed to import win32com.");
	time.sleep(2);
	quit();

try:
	from git import Repo as rep;
except ImportError:
	try:
		print("Installing required libraries...");
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitpython']);
	except Exception as err:
		print("Error:",err);
		time.sleep(2);
		quit();
	try:
		from git import Repo as rep;
	except ImportError:
		print("Error:",err);
		time.sleep(2);
		quit();

def install(path,url):
	try:

		print("Installing from:",url);
		path = os.path.join(path,f"cmd {VERSION_NAME}");
		os.mkdir(path);
		rep.clone_from(url,path);
		os.remove(os.path.join(path,".gitignore"));
		os.remove(os.path.join(path,"cmd installer.py"));
		os.remove(os.path.join(path,"installer.jar"))
		os.remove(os.path.join(path,"installer.kt"))
		os.remove(os.path.join(path,"fixer.c"))
		shutil.rmtree(os.path.join(path,".git"), ignore_errors = True);
		shutil.rmtree(os.path.join(path,"Zipped files"), ignore_errors = True);
		shutil.rmtree(os.path.join(path,"Old READMEs"), ignore_errors = True);
		shutil.rmtree(os.path.join(path,"Old Versions"), ignore_errors = True);

		#os.remove(os.path.join(path,".git"));

		#mainfile = os.path.join(os.path.join(path,f"cmd {VERSION_NAME}"),"main.py");
		#if(not os.path.exists(mainfile)): print("Error: Mainfile does not exist, therefore no shortcut can be made..."); time.sleep(2); quit();
		# Add shortcut - later version:
		
		#desktop = winshell.desktop();
		#shrtpath = os.path.join(desktop, "pycmd.bat");
		#writefile = open(shrtpath,"w");
		#writefile.write(f'@echo off\npy "{mainfile}"');
		#writefile.close();
		#shell = Dispatch('WScript.Shell');
		#shortcut = shell.CreateShortCut(shrtpath);
		#shortcut.Targetpath = mainfile;
		#shortcut.Arguments = os.path.join(path,f"cmd {VERSION_NAME}");
		#shortcut.WorkingDirectory = os.path.join(path,f"cmd {VERSION_NAME}");
		#shortcut.IconLocation = "%windir%\system32\cmd.exe";
		#shortcut.save();

	except Exception as err:
		print("Error:",err);

try:
	path = "";
	while(not os.path.exists(path) or not os.path.isdir(path) or path == ""):
		path = input("Installation directory: ");
	install(path,"https://github.com/xihtyM/python-cmd-features");
except Exception as err:
	print("Error:",err);

print("Successfully installed, exiting in 2 seconds...");
time.sleep(2);
