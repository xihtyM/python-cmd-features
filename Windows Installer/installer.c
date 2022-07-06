/* Installer in C - early development */

/* Libraries */

#include <stdlib.h>
#include <stdio.h>

/* Bool, os, all defines */

#include "extras.h"

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

/* Length of string */

int length(char * x) {
	int i;
	for (i = 0; x[i] != '\0'; ++i);
	return i;
}

/* Replace char in string */

char * replace(char * string, char chr1, char chr2) {
    int i;
    char * endStr = malloc(length(string)+1);

    for(i=0; string[i]; i++) {
        if(string[i] == chr1) {
            endStr[i] = chr2;
        } else {
            endStr[i] = string[i];
        }
    }

    /* Terminate string */

    endStr[length(string)] = '\0';
    
    return endStr;
}

/* Windows Code */

#include <windows.h>
#include <string.h>

/* Thanks stackoverflow lmao: https://stackoverflow.com/questions/11238918/s-isreg-macro-undefined */

// Windows does not define the S_ISREG and S_ISDIR macros in stat.h, so we do.
// We have to define _CRT_INTERNAL_NONSTDC_NAMES 1 before #including sys/stat.h
// in order for Microsoft's stat.h to define names like S_IFMT, S_IFREG, and S_IFDIR,
// rather than just defining  _S_IFMT, _S_IFREG, and _S_IFDIR as it normally does.

#define _CRT_INTERNAL_NONSTDC_NAMES true

#include <sys/stat.h>

#if !defined(S_ISREG) && defined(S_IFMT) && defined(S_IFREG)
	#define S_ISREG(m) (((m)&S_IFMT) == S_IFREG)
#endif

#if !defined(S_ISDIR) && defined(S_IFMT) && defined(S_IFDIR)
	#define S_ISDIR(m) (((m)&S_IFMT) == S_IFDIR)
#endif

/* If directory command */

int isDirectory(char *dir) {

	const char *folder = replace(dir, '/', '\\');

	/* Create stat struct */

	struct stat sb;

	/* If it is a folder */

	if (stat(folder, &sb) == false && S_ISDIR(sb.st_mode)) {
		return true;
	}
	/* If it is not a folder */
	else {
		return false;
	}
}

/* If file command */

int isFile(char *raw_file) {

	const char *file = replace(raw_file, '/', '\\');

	/* Create stat struct */

	struct stat sb;

	/* If it is a file */

	if (stat(file, &sb) == false && S_ISREG(sb.st_mode)) {
		return true;
	}
	/* If it is not a file */
	else {
		return false;
	}
}

/* Install */

void install(char *dir) {

	/* URL of zipped file */

	const char *url = "https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip";

	/* Const directory path with / replaced to \\ */

	const char *__dir = replace(dir, '/', '\\');

	/* Directory to zip file */

	char tempDest[MAX_PATH];
	strcpy(tempDest, __dir);
	strcat(tempDest, "\\cmd.zip");
	const char *dest = tempDest;
	
	/* Print location of zip file */

	printf("\nInstalling zip at: %s", dest);

	/* Thanks https://www.go4expert.com/articles/download-file-using-urldownloadtofile-c-t28721/ */

	HRESULT dl;
	typedef HRESULT(WINAPI * URLDownloadToFileA_t)(LPUNKNOWN pCaller, LPCSTR szURL, LPCSTR szFileName, DWORD dwReserved, void *lpfnCB);
	URLDownloadToFileA_t xURLDownloadToFileA;
	xURLDownloadToFileA = (URLDownloadToFileA_t)GetProcAddress(LoadLibraryA("urlmon"), "URLDownloadToFileA");
	dl = xURLDownloadToFileA(NULL, url, dest, 0, NULL);

	if (S_OK == dl) {
		printf("\nSucessfully downloaded zipfile at: %s.", dest);
	} else {
		printf("\nSomething went wrong downloading zipfile at: %s.", dest);
		return;
	}

	char *cmd_1 = "powershell -Command Expand-Archive -Path ";
	char *cmd_2 = " -DestinationPath ";

	char cmd[MAX_PATH];
	strcpy(cmd, cmd_1);
	strcat(cmd, dest);
	strcat(cmd, cmd_2);
	strcat(cmd, __dir);

	system(cmd);

	remove(dest);

	printf("\nSucessfully installed!\n");
}

/* Desktop shortcut */

void addShrt(const char *p) {

	/* USERPROFILE environment variable */

	const char *USERPROFILE = getenv("USERPROFILE");

	/* Desktop path */

	char T_DESKTOP[MAX_PATH];

	strcpy(T_DESKTOP, USERPROFILE);
	strcat(T_DESKTOP, "\\Desktop");

	const char *DESKTOP = T_DESKTOP;

	/* Shortcut link */

	char T_SHORT_LNK[MAX_PATH];

	strcpy(T_SHORT_LNK, DESKTOP);
	strcat(T_SHORT_LNK, "\\pycmd");

	const char *SHORT_LNK = T_SHORT_LNK;

	/* System command */

	char command[1024] = "mklink \"";

	strcat(command, SHORT_LNK);
	strcat(command, "\" \"");
	strcat(command, p);
	strcat(command, "\\cmd\\main.py");
	strcat(command, "\"");

	system(command);
}

int main() {

    isValid();

    UpdatePyPackages();

	/* Clear */

	system("cls");

    /* Create pycmd shell command in windows */

    char path[MAX_PATH];

    /* While path is not a directory */

    while(isDirectory(path) == false) {
		
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
