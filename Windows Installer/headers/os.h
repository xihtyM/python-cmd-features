/* OS functions */

#ifndef __OS_H

	#define __OS_H

	#include "str.h"
	#include "bool.h"

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


	#if __WIN__f == true
		#define _CRT_INTERNAL_NONSTDC_NAMES true

		#include <sys/stat.h>

		#if !defined(S_ISREG) && defined(S_IFMT) && defined(S_IFREG)
			#define S_ISREG(m) (((m)&S_IFMT) == S_IFREG)
		#endif

		#if !defined(S_ISDIR) && defined(S_IFMT) && defined(S_IFDIR)
			#define S_ISDIR(m) (((m)&S_IFMT) == S_IFDIR)
		#endif

		bool isdir(char * __path) {
			char * folder = replace(__path, '/', '\\');

			/* Create stat struct */

			struct stat sb;

			/* If it is a folder */

			if (stat(folder, &sb) == false && S_ISDIR(sb.st_mode)) {
				free(folder);
				return true;
			}
			/* If it is not a folder */
			else {
				free(folder);
				return false;
			}
		}

		/* If file command */

		bool isfile(char * raw_file) {

			char * file = replace(raw_file, '/', '\\');

			/* Create stat struct */

			struct stat sb;

			/* If it is a file */

			if (stat(file, &sb) == false && S_ISREG(sb.st_mode)) {
				free(file);
				return true;
			}
			/* If it is not a file */
			else {
				free(file);
				return false;
			}
		}
		/*
		FIX: Getdir func
		#include <io.h>

		char * getdir(void) {
			char * __p = (char *) malloc(MAX_PATH + 1);
			
			return __p;
			/* Remember to free after use */ /*
		}
		*/

		char * file_extension(char * file) {
			return strcount(file, '.') == 0 ? "N/A" : strsplit(file    ,    find(file  ,  '.'  ,  strcount(file  ,  '.')) + 1    ,    -2);

			/* Remember to free after using */
		}
	#endif
#endif
