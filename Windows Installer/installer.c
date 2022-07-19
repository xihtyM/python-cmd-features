/* Windows Installer in C */

/* Libraries */

#include <stdlib.h>
#include <stdio.h>

/* Bool, os, all defines */

#include "headers/str.h"
#include "headers/os.h"

/* Check if system is valid */

void isValid() {
    if(system(NULL) == false) {
        printf("Error: System is not supported.");
        exit(0);
    }
}

#if __WIN__f == false
    printf("Error: Please use the correct installer for your OS.");
    exit(0);
#endif

/* Update Python Libraries for cmd to run */

void UpdatePyPackages() {
        
    /* Install */
        
    printf("Installing Libraries...\n");
    system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");
    printf("Sucessfully installed all required libraries!\n");
}

/* Windows Code */

#include <urlmon.h>

/* Install */

void install(char * dir) {

	/* URL of zipped file */

	const char * url = "https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip";

	/* Const directory path with / replaced to \\ */

	char * __dir = replace(dir, '/', '\\');

	/* Directory to zip file */

	char dest[MAX_PATH];
	strcpy(dest, __dir);
	strcat(dest, "\\cmd.zip");
	
	/* Print location of zip file */

	printf("\nInstalling zip at: %s", dest);

	HRESULT dl = URLDownloadToFileA(NULL, url, dest, 0, NULL);

	if (S_OK == dl) {
		printf("\nSucessfully downloaded zipfile at: %s.", dest);
	} else {
		printf("\nSomething went wrong downloading zipfile at: %s.", dest);
		return;
	}

	char * cmd_1 = "powershell -Command Expand-Archive -Path \"";
	char * cmd_2 = "\" -DestinationPath \"";

	char cmd[MAX_PATH];
	strcpy(cmd, cmd_1);
	strcat(cmd, dest);
	strcat(cmd, cmd_2);
	strcat(cmd, __dir);
	strcat(cmd, "\"");

	system(cmd);

	free(__dir);

	remove(dest);

	printf("\nSucessfully installed!\n");
}

/* Desktop shortcut */

void addShrt(char * _p) {

	/* USERPROFILE environment variable */

	const char * USERPROFILE = getenv("USERPROFILE");
	
	/* Replace p / to \\ */

	char * p = replace(_p, '/', '\\');

	/* Desktop path */

	char DESKTOP[MAX_PATH];

	strcpy(DESKTOP, USERPROFILE);
	strcat(DESKTOP, "\\Desktop");

	/* Shortcut link */

	char SHORT_LNK[MAX_PATH];

	strcpy(SHORT_LNK, DESKTOP);
	strcat(SHORT_LNK, "\\pycmd");

	/* System command */

	char command[1024] = "mklink \"";

	strcat(command, SHORT_LNK);
	strcat(command, "\" \"");
	strcat(command, p);
	strcat(command, "\\cmd\\main.py");
	strcat(command, "\"");

	system(command);
}

int main(void) {

    isValid();

    UpdatePyPackages();

	/* Clear */

	system("cls");

    /* Create pycmd shell command in windows */

    char path[MAX_PATH];

    /* While path is not a directory */

    while(isdir(path) == false) {
		
		/* Red color */

		system("color 4");

        printf("Installation directory: ");

        /* User input */

        fgets(path, MAX_PATH, stdin);

        /* Gotta be safe */

        if(path == NULL) { continue; }
        
        /* Remove last character of string (it's a newline as I used fgets) */

        path[length(path)-1] = '\0';
    }

    install(path);
    addShrt(path);

    system("pause");

	return 0;
}
