/* Random extras */

/* True/False/Bool */

#ifdef true
	#undef true
#endif

#ifdef false
	#undef false
#endif

#define true (1==1)
#define false (1!=1)

/* Check current operating system */

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

/* Check if CurrentOS is already defined */

#ifdef CurrentOS
    #undef CurrentOS
#endif

/* Is on Windows System */

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
    #define __WIN__f true
    #define CurrentOS "win"
#else
    #define __WIN__f false
#endif

/* Is on MacOS */

#ifdef __APPLE__
    #define __MACOS__f true
    #define CurrentOS "mac"
#else
    #define __MACOS__f false
#endif

/* Is on Linux System */

#ifdef linux
    #define __LINUX__f true
    #define CurrentOS "linux"
#else
    #define __LINUX__f false
#endif
