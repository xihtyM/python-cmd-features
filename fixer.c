// Fixer

// Define

#ifndef NULL
    #ifdef __cplusplus
        #define NULL 0
    #else
        #define NULL ((void *)0)
    #endif
#endif

// Fix

int main() {
	if(system(NULL) == 0) { return 1; }

	// Epic color

	system("color a");

    // Install all libraries

    system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil");

	return 0;
}
