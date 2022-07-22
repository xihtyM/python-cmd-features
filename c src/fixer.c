/* Fixer in C */

/* Libraries */

#include <stdlib.h>
#include <stdio.h>

#include "headers/clibs.h"

/* Main Function */

int main(void) {

    /* Check if system is valid */
    
    #if __WIN__f == false
        printf("Error: Your OS is not supported.");
        return 1;
    #endif

    if(system(NULL) == 0) {
        printf("Error: System is not supported.");
        #if __WIN__f == true
            system("pause");
        #endif
        return 1;
    }
    
    /* Only windows as of yet */

    #if __WIN__f == true
        system("color a");
        printf("Installing Libraries...");
        system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");
        system("pause");
    #endif

    /* End without errors */

    return 0;
}
