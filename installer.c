/* Installer in C - early development */

/* Libraries */

#include <stdlib.h>
#include <stdio.h>

/* Define */

/* Check if __WIN__f is already defined */

#ifdef __WIN__f
    #undef __WIN__f
#endif

/* Check if __LINUX__f is already defined */

#ifdef __LINUX__f
    #undef __LINUX__f
#endif

/* Check if __MACOS__f is already defined */

#ifdef __MACOS__f
    #undef __MACOS__f
#endif

/* Define true and false */

#ifdef True
    #undef True
#endif

#ifdef False
    #undef False
#endif

#define True 1
#define False 0

/* Is on Windows System */

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
    #define __WIN__f True
#else
    #define __WIN__f False
#endif

/* Is on MacOS */

#ifdef __APPLE__
    #define __MACOS__f True
#else
    #define __MACOS__f False
#endif

/* Is on Linux System */

#ifdef linux
    #define __LINUX__f True
#else
    #define __LINUX__f False
#endif

/* Check if system is valid */

void isValid() {
    if(system(NULL) == False) {
        printf("Error: System is not supported.");
        system("pause");
        exit(0);
    }
}

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
    char * endStr = malloc(sizeof(string));

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

#if __WIN__f

	#include <windows.h>
    #include <string.h>

    /* Thanks stackoverflow lmao: https://stackoverflow.com/questions/11238918/s-isreg-macro-undefined */

	// Windows does not define the S_ISREG and S_ISDIR macros in stat.h, so we do.
    // We have to define _CRT_INTERNAL_NONSTDC_NAMES 1 before #including sys/stat.h
    // in order for Microsoft's stat.h to define names like S_IFMT, S_IFREG, and S_IFDIR,
    // rather than just defining  _S_IFMT, _S_IFREG, and _S_IFDIR as it normally does.
    #define _CRT_INTERNAL_NONSTDC_NAMES True

    #include <sys/stat.h>

    #if !defined(S_ISREG) && defined(S_IFMT) && defined(S_IFREG)
        #define S_ISREG(m) (((m) & S_IFMT) == S_IFREG)
    #endif

    #if !defined(S_ISDIR) && defined(S_IFMT) && defined(S_IFDIR)
        #define S_ISDIR(m) (((m) & S_IFMT) == S_IFDIR)
    #endif

    /* If directory command */

    int isDirectory(char * dir) {
        
        const char * folder = replace(dir,'/','\\');

        /* Create stat struct */

        struct stat sb;

        /* If it is a folder */

        if(stat(folder, &sb) == False && S_ISDIR(sb.st_mode)) {
            return 1;
        }
        /* If it is not a folder */
        else {
            return 0;
        }
    }

    /* If file command */

    int isFile(char * raw_file) {
        
        const char * file = replace(raw_file,'/','\\');

        /* Create stat struct */

        struct stat sb;

        /* If it is a file */

        if(stat(file, &sb) == False && S_ISREG(sb.st_mode)) {
            return 1;
        }
        /* If it is not a file */
        else {
            return 0;
        }
    }

    /* Install */

    void install(char dir[]) {

        /* URL of zipped file */

        const char * url = "https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip";

        /* Const directory path with / replaced to \\ */

        const char * __dir = replace(dir,'/','\\');

        /* Directory to zip file */

        char tempDest[MAX_PATH];
        strcpy(tempDest, __dir);
        strcat(tempDest, "\\cmd.zip");
        const char * dest = tempDest;

        /* Print location of zip file */

        printf("\nInstalling zip at: %s", dest);

        /* Thanks https://www.go4expert.com/articles/download-file-using-urldownloadtofile-c-t28721/ */

        HRESULT dl;
        typedef HRESULT (WINAPI * URLDownloadToFileA_t)(LPUNKNOWN pCaller, LPCSTR szURL, LPCSTR szFileName, DWORD dwReserved, void * lpfnCB);
        URLDownloadToFileA_t xURLDownloadToFileA;
        xURLDownloadToFileA = (URLDownloadToFileA_t)GetProcAddress(LoadLibraryA("urlmon"), "URLDownloadToFileA");

        dl = xURLDownloadToFileA(NULL, url, dest, 0, NULL);

        if(S_OK == dl) {
            printf("\nSucessfully downloaded zipfile at: %s.", dest);
        } else {
            printf("\nSomething went wrong downloading zipfile at: %s.", dest);
            return;
        }

        char * cmd_1 = "powershell -Command Expand-Archive -Path ";
        char * cmd_2 = " -DestinationPath ";

        char cmd[MAX_PATH];
        strcpy(cmd, cmd_1);
        strcat(cmd, dest);
        strcat(cmd, cmd_2);
        strcat(cmd, __dir);

        system(cmd);
        
        remove(dest);

        printf("\nSucessfully installed!");

    }

    /* Might add a command in cmd */

    void addcmd(const char * p) {
        
        /* System32 path */

        char win32_sys[MAX_PATH];
        GetSystemDirectoryA(win32_sys,sizeof(win32_sys));

        /* Batch file path */

        char path_to_bat[MAX_PATH];

        strcpy(path_to_bat,win32_sys);
        strcat(path_to_bat,"\\pycmd.bat");

        if(isFile(path_to_bat) == False) {

            /* Pointer to bat file */

            FILE * batptr;

            batptr = fopen(path_to_bat,"w");

            /* Gotta be safe */

            //if(batptr != NULL) {
                    
            char * cmd = "@echo off\npy ";
            printf("True");
            char * quote = "\"";

            strcat(cmd,quote);
            strcat(cmd,p);
            strcat(cmd,quote);

            fprintf(batptr,"@echo off\npy \"C:\\Users\\tiddl\\Desktop\\⠀\\Programs\\Python Projects\\Text Editor (NEW - Terminal)\\cmd v1.0.4 pre-release-1\\main.py\"");

            //} else {
            //    printf("\nError: Something went wrong creating windows command.");
            //    return;
            //}

            fclose(batptr);

        } else {
            printf("\nError: Something went wrong creating windows command.");
            return;
        }
        if(isFile(path_to_bat) == False) {
            printf("\nError: Something went wrong creating windows command.");
        }
    }

    /* Desktop shortcut */

    void addShrt(const char * p) {

        /* USERPROFILE environment variable */

        const char * USERPROFILE = getenv("USERPROFILE");

        /* Desktop path */

        char T_DESKTOP[MAX_PATH];

        strcpy(T_DESKTOP,USERPROFILE);
        strcat(T_DESKTOP,"\\Desktop");

        const char * DESKTOP = T_DESKTOP;

        /* Shortcut link */

        char T_SHORT_LNK[MAX_PATH];

        strcpy(T_SHORT_LNK,DESKTOP);
        strcat(T_SHORT_LNK,"\\pycmd");

        const char * SHORT_LNK = T_SHORT_LNK;

        /* System command */

        char command[1024] = "mklink \"";

        strcat(command,SHORT_LNK);
        strcat(command,"\" \"");
        strcat(command,p);
        strcat(command,"\\cmd\\main.py");
        strcat(command,"\"");

        system(command);
        
    }

/* Linux Code */

#elif __LINUX__f
    /* Havent tested to see if it works */
    /* Linux specific libs */
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <unistd.h>

    int isDirectory(char* dir) {
        
        const char* folder = replace(dir,'/','\\');

        /* Create stat struct */

        struct stat sb;

        /* If it is a folder */

        if(stat(folder, &sb) == 0 && S_ISDIR(sb.st_mode)) {
            return 1;
        }
        /* If it is not a folder */
        else {
            return 0;
        }
    }

/* MacOS Code */

#elif __MACOS__f

#endif

int main() {
    isValid();
    UpdatePyPackages();

    /* Temporary stopping linux/mac users from using this */

    #if __LINUX__f || __MACOS__f
        printf("Error, your current OS is not supported, please use the java installer.");
        return 0;
    #endif

    /* Create pycmd shell command in windows */

    char path[MAX_PATH];

    /* While path is not a directory */

    while(isDirectory(path) == False) {
        printf("\nInstallation directory: ");

        /* User input */

        fgets(path, MAX_PATH, stdin);

        /* Gotta be safe */

        if(path == NULL) { continue; }
        
        /* Remove last character of string (it's a newline as I used fgets) */

        path[length(path)-1] = '\0';
    }
    printf("\nInstalling at: %s",path);

    install(path);
    //addcmd(path);
    addShrt(path);

	return 0;
}
