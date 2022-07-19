/* C/C++ String defines and functions */

#include <stdlib.h>
#include <math.h>

#ifndef __BOOL_H
	#include "bool.h"
#endif

#ifndef __STRING_H
	#define __STRING_H

	typedef char ** (list);

	int length(const char * __s) {
		int i;
		for (i = 0; __s[i] != '\0'; ++i);
		return i;
	}

	/*
	FIX: CONCAT FUNCTION RETURNS POINTER TO NULL ADDRESS
	char * concat(char * __dest, const char * __str)
	{
		int __dest_len = length(__dest);
		char __dest_t[__dest_len + length(__str)];
		
		for(int c = 0; c < __dest_len; c++) {
			__dest_t[c] = __dest[c];
		}
		
		for(int i = 0; i < length(__str); i++) {
			__dest_t[__dest_len + i] = __str[i];
		}
		
		__dest_t[length(__dest_t)-1] = '\0';
		__dest = __dest_t;
		// FIX: BROKEN RETURN
	}
	*/

	/* Replace char in string */

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

	int strcount(char * __str, char val) {
		int count = 0;
		for (int i = 0; i < length(__str); i++) {
			if(__str[i] == val) {
				count++;
			}
		}
		return count;
	}

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

	bool strequals(const char * str_1, const char * str_2) {
		if(length(str_1) != length(str_2)) { return false; }

		for (int i = 0; i <= length(str_1); i++) {
			if(str_1[i] != str_2[i]) {
				return false;
			}
		}
		
		return true;
	}
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
	}

	int ptrtoint(char * ptr) {
		int _int = 0;
		for (int i = length(ptr) - 1; i >= 0; i--) {
			_int += (int) ((int) ptr[i + 1] - '0') * (pow(10, (double) i));
		}
		return _int;
	}
#endif
