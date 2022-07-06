# cmd v1.0.4 pre-release-3

## Patch Notes ##
1. Windows installer (Fixed)
2. Added shortcuts with c installer.

## Next Release (v.1.0.4) ##
1. Control volume of playsound and add something that can pause/stop music from playing.

## Future Notes ##
1. Adding support for linux and mac on c installer.

## Installers

**Windows installer**
- Windows installer: https://github.com/xihtyM/python-cmd-features/raw/master/Windows%20Installer/installer.exe.

**Java installer (Supports Windows, Unix and MacOS)**
> Java Installer: https://github.com/xihtyM/python-cmd-features/raw/master/Java%20Installer/installer.jar.

**Old (Currently unavailable)**
> Python Installer: https://raw.githubusercontent.com/xihtyM/python-cmd-features/master/cmd%20installer.py - Copy this into a .py file.

## Download ##

__With installer__

1. Install the installer by going to the above links:
2. Install fixer and run it at (If you use the java installer): https://github.com/xihtyM/python-cmd-features/raw/master/fixer.exe.
3. Run the installer.
4. Input your chosen directory.

__With zipped file__

1. Download the zipped file at https://github.com/xihtyM/python-cmd-features/tree/master/Zipped%20files/Latest%20Release (Latest release is in this folder).
2. Unzip with extract here in the directory you would like.
3. **Optional**: Create a shortcut to main.py.

__Installing old versions__

- Just go to https://github.com/xihtyM/python-cmd-features/tree/master/Zipped%20files/ and unzip the version you want.

## Fixer ##

__Precautions__

**If you don't trust it:**

- Source code is available at https://github.com/xihtyM/python-cmd-features/blob/master/fixer.c.

**If you still don't trust it:**

- Compile it yourself.

__Running:__

**If it says windows protected your PC:**
1. Click "More info".
2. Click "Run Anyway".

(This message will appear because I haven't registered with Microsoft - nothing fishy, but if you don't trust it refer to precautions above this).

__What it does__

The fixer installs all missing libraries used in the project.

__Alternatives__

If you seriously still don't trust it then run the following command to install the libraries yourself:

	pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil

## Final Notes ##

>This project is mainly for fun, so don't expect it to be anything groundbreaking.

>If you see something wrong, or get an unexpected error. Please create an issue via github; or if you feel like fixing it yourself, you can contribute.
