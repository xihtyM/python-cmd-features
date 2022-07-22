/* C/C++ String defines and functions */

#include <stdlib.h>

#ifndef __BOOL_H
	#include "bool.h"
#endif

#ifndef __STRING_H
	#define __STRING_H

	typedef char ** (list);

	/* Returns length of a string excluding null terminator */
	int length(const char * __s) {
		int i;
		for (i = 0; __s[i] != '\0'; ++i);
		return i;
	}

	/* Concatenate 2 strings, returns a string (Must be freed after use) */
	char * concat(char * __str_1, const char * __str_2) {
		int __str_1_size = length(__str_1);
		int __str_2_size = length(__str_2);
		char * __dest = malloc(__str_1_size + __str_2_size + 1);

		for (int i = 0; i <= __str_1_size; i++) {
			__dest[i] = __str_1[i];
		}
		for (int i = 0; i <= __str_2_size; i++) {
			__dest[i + __str_1_size] = __str_2[i];
		}
		
		__dest[length(__dest)] = '\0';
		return __dest;
		/* Remember to free after use */
	}

	/* Replace char in string (Must be freed after use) */
	char * replace(char * string, char __replace_from, char __replace_to) {
		int i;
		char * FULL_STR = (char *) malloc(length(string) + 1);

		for(i=0; string[i]; i++) {
			if(string[i] == __replace_from) {
				FULL_STR[i] = __replace_to;
			} else {
				FULL_STR[i] = string[i];
			}
		}

		/* Terminate string */

		FULL_STR[length(string)] = '\0';

		return FULL_STR;

		/* Remember to free after using */
	}

	/* Returns amount of occurences of char in a string */
	int strcount(char * __str, char val) {
		int count = 0;
		for (int i = 0; i < length(__str); i++) {
			if(__str[i] == val) {
				count++;
			}
		}
		return count;
	}

	/*
	Finds a char in a string, at the amount of occurences of it.
	Example: If the occ value is 2, it will return the 2nd occurence of that char.
	*/
	int find(char * __str, char val, int occ) {
		if (occ == 0 || strcount(__str, val) == 0) { return 0; }
		int __occ = 0;
		for (int i = 0; i < length(__str); i++) {
			if(__str[i] == val) {
				__occ++;
				if(__occ == occ) {
					return i;
				}
			}
		}
	}

	/* Split a string (Must be freed after use) */
	char * strsplit(char * __str, int __st, int __end) {
		if(__end == -2) { __end = length(__str); }
		char * end_char = (char *) malloc(__end - __st + 1);
		int c = 0;

		for (int i = __st; i <= __end; i++) {
			end_char[c] = __str[i];
			c++;
		}

		end_char[__end - __st] = '\0';
		
		return end_char;

		/* Remember to free after using */
	}

	/* Compare two strings */
	bool strequals(const char * str_1, const char * str_2) {
		if(length(str_1) != length(str_2)) { return false; }

		for (int i = 0; i <= length(str_1); i++) {
			if(str_1[i] != str_2[i]) {
				return false;
			}
		}
		
		return true;
	}

	/* FIX: Broken function
	list split_occ(char * __s, char __o) {
		if(strcount(__s, __o) == 0) { list end = (list) malloc(length(__s)); end[0] = __s; return end; }
		int occ = strcount(__s, __o) + 1;
		list array = (list) malloc(length(__s) + occ);
		int __s_new;
		int __s_old = 0;
		for (int i = 1; i <= occ; i++) {
			__s_new = find(__s, __o, i);
			array[i - 1] = strsplit(__s, __s_old, __s_new);
			array[i - 1][__s_new - __s_old] = '\0';
			__s_old = __s_new + 1;
		}

		//array[occ][length(array[occ])] = '\0'; 

		return array;
	} */

	/* Strip all trailing characters that are of certain character (Must be freed after use) */
	char * rstrip(char * __str, char to_strip) {
		int i;
		for (i = length(__str) - 1; i >= 0; i--) {
			if (__str[i] != to_strip) {
				break;
			}
		}
		return strsplit(__str, 0, i + 1);
		/* Remember to free after use */
	}

	/* Strip all leading characters that are of certain character (Must be freed after use) */
	char * lstrip(char * __str, char to_strip) {
		int i;
		for (i = 0; i < length(__str); i++) {
			if (__str[i] != to_strip) {
				break;
			}
		}
		return strsplit(__str, i, -2);
		/* Remember to free after use */
	}

	/* Remove repeat characters (Must be freed after use) */
	char * remove_repeat(char * __str, char _repeat) {
		int formatted_str_size = 0;
		bool slash = false;
		for (int i = 0; i < length(__str); i++) {
			if(__str[i] == _repeat) {
				if(slash == true) { continue; }
				formatted_str_size++;
				slash = true;
				continue;
			}
			formatted_str_size++;
			slash = false;
		}

		char * formatted_str = malloc(formatted_str_size + 1);
		int c = 0;
		slash = false;

		for (int i = 0; i < length(__str); i++) {
			if(__str[i] == _repeat) {
				if(slash == true) { c++; continue; }
				formatted_str[i - c] = __str[i];
				slash = true;
				continue;
			}
			formatted_str[i - c] = __str[i];
			slash = false;
		}

		formatted_str[formatted_str_size] = '\0';

		return formatted_str;
		/* Remember to free after use */
	}

	/* Convert a bool to a string */
	const char * bool_to_str(bool val) {
		return val ? "true" : "false";
	}

#endif
