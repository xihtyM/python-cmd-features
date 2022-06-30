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

/* Is on Windows System */

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
    #define __WIN__f 1
#else
    #define __WIN__f 0
#endif

/* Is on MacOS */

#ifdef __APPLE__
    #define __MACOS__f 1
#else
    #define __MACOS__f 0
#endif

/* Is on Linux System */

#ifdef linux
    #define __LINUX__f 1
#else
    #define __LINUX__f 0
#endif

/* Check if system is valid */

void isValid() {
    if(system(NULL) == 0) {
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
    #define _CRT_INTERNAL_NONSTDC_NAMES 1

    #include <sys/stat.h>

    #if !defined(S_ISREG) && defined(S_IFMT) && defined(S_IFREG)
        #define S_ISREG(m) (((m) & S_IFMT) == S_IFREG)
    #endif

    #if !defined(S_ISDIR) && defined(S_IFMT) && defined(S_IFDIR)
        #define S_ISDIR(m) (((m) & S_IFMT) == S_IFDIR)
    #endif

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

    /* Install */

    void install(char dir[]) {

        /* URL of zipped file */

        const char * url = "https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip";

        /* Const directory path with / replaced to \\ */

        const char * __dir = replace(dir,'/','\\');

        /* Directory to zip file */

        char tempDest[512];
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

        char cmd[512];
        strcpy(cmd, cmd_1);
        strcat(cmd, dest);
        strcat(cmd, cmd_2);
        strcat(cmd, __dir);

        system(cmd);

        printf("\nSucessfully installed!");

    }

/* Linux Code */

#elif __LINUX__f

/* MacOS Code */

#elif __MACOS__f

#endif


int main() {
    isValid();
    UpdatePyPackages();
    char path[512];

    /* While path is not a directory */

    while(isDirectory(path) == 0) {
        printf("\nInstallation directory: ");

        /* User input */

        fgets(path, 512, stdin);

        /* Gotta be safe */

        if(path == NULL) { continue; }
        
        /* Remove last character of string (it's a newline as I used fgets) */

        path[length(path)-1] = '\0';
    }
    printf("\nInstalling at: %s",path);

    install(path);

	return 0;
}
