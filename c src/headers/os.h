/* OS functions */

#ifndef __OS_H

	#define __OS_H

	#ifndef __STR_H
		#include "str.h"
	#endif
	#ifndef __BOOL_H
		#include "bool.h"
	#endif
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

	/* Is on Linux System */

	#if defined(__linux__) || defined(__unix__) || defined(__unix)
		#define __UNIX__f true
		#define CurrentOS "unix"
	#else
		#define __UNIX__f false
	#endif

	#ifndef CurrentOS
		#define CurrentOS "unregistered"
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

		#ifndef INVALID_HANDLE_VALUE
			#define INVALID_HANDLE_VALUE ((HANDLE)(LONG_PTR)-1)
		#endif

		/* If directory command */
		bool os_isdir(char * __path) {
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
		bool os_isfile(char * raw_file) {

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
		
		/* So string.h doesn't get included with libloaderapi.h */
		#define _MAC
		#ifndef _INC_STRING
			#define _INC_STRING
		#endif

		#include <libloaderapi.h>

		/* Returns the working directory of the executable (Must be freed after use) */
		char * os_getcwd(void) {
			char * cwd = (char *) malloc(261);
			GetModuleFileNameA(NULL, cwd, 260);
			return cwd;
			/* Remember to free after using */
		}

		#include <fileapi.h>
		#include <stdio.h>

		char * os_listdir(char * _path, int index) {
			char * path = rstrip(replace(_path, '/', '\\'), '\\');

			if(!os_isdir(path)) {
				return "N/A";
			}

			WIN32_FIND_DATA data;
			HANDLE hFind = FindFirstFile(concat(path, "\\*"), &data);
			char name[261];
			int ind = 0;

			if (hFind != INVALID_HANDLE_VALUE) {
				do {
					ind++;
					if (ind == index) {
						char * name = data.cFileName;
						return name;
					}
				} while (FindNextFile(hFind, &data));
				FindClose(hFind);
			}
			return "N/A";
		}

	#elif __UNIX__f == true
		#include <unistd.h>
		#include <sys/stat.h>
		
		/* Returns the working directory of the executable (Must be freed after use) */
		char * os_getcwd(void) {
			char * cwd = (char *) malloc(261);
			if (getcwd(cwd, sizeof(cwd)) != NULL) {
				return cwd;
			} else {
				return "err";
			}
		}

		/* If path is directory */
		bool os_isdir(char * folder) {
			
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

		/* If path is file */
		bool os_isfile(char * file) {

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
		
	#else
		printf("Your current OS is not supported as of yet with the \"os.h\" header.");
	#endif
	
	/* Returns extension of path  (Must be freed after use) */
	char * os_extension(char * file) {
		return strcount(file, '.') == 0 ? "N/A" : strsplit(file    ,    find(file  ,  '.'  ,  strcount(file  ,  '.')) + 1    ,    -2);

		/* Remember to free after using */
	}
	/* Returns the parent directory of a path (Must be freed after use) */
	char * os_getparent(char * path) {
		char * _path =
		remove_repeat(
			rstrip(
				replace(path,'/','\\'),
				'\\'
				),
				'\\'
				);
		return 
		(
			strsplit(
				_path,
				0,
				find(_path, '\\', strcount(  _path  ,  '\\'  ))
				)
			);
		/* Remember to free after using */
	}
	
	/* If path exists */
	bool os_exists(char * path) {
		return (os_isfile || os_isdir);
	}
#endif
