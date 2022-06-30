/* Fixer in C */

/* Define */

// None

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

/* Main Function */

int main() {

    /* Check if system is valid */
    
    #if __WIN__f == 0 && __LINUX__f == 0 && __MACOS__f == 0
        printf("Error: Your OS is not supported.");
        return 1;
    #endif

    if(system(NULL) == 0) {
        printf("Error: System is not supported.");
        #if __WIN__f
            system("pause");
        #elif __LINUX__f || __MACOS__f
            system( "read -n 1 -s -p \"Press any key to continue...\"" );
        #endif
        return 1;
    }
    
    /* If there is any disparity between linux and mac, I thought I'd include a difference now so it's easier to code later */

    /* If on Windows */

    #if __WIN__f
        system("color a");
        printf("Installing Libraries...");
        system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");
        system("pause");

    /* If on Linux */

    #elif __LINUX__f
        printf("Installing Libraries...");
        system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");
        system( "read -n 1 -s -p \"Sucessfully installed.\nPress any key to continue...\"" );
    
    /* If on MacOS */

    #elif __MACOS__f
        printf("Installing Libraries...");
        system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");
        system( "read -n 1 -s -p \"Sucessfully installed.\nPress any key to continue...\"" );

    #endif

    /* End without errors */

    return 0;
}
