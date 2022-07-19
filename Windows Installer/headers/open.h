#ifndef __OPEN_H

	#ifndef __STRING_H
		#include "str.h"
	#endif

	#include <stdlib.h>

	#define __OPEN_H

	int file_getsize(const char * file) {
		FILE * read_file;

		/* Opening read file */

		read_file = fopen(file, "r");

		char txt = fgetc(read_file);
		int i = 0;

		while (txt != (-1)) {
			i++;
			txt = fgetc(read_file);
    	}

		fclose(read_file);

		return i;
	}

	char * file_read(const char * file) {
		
		FILE * read_file;

		/* Opening read file */

		read_file = fopen(file, "r");

		size_t size = file_getsize(file);

		char txt = fgetc(read_file);
		char * allocated_text = (char *) malloc(size);

		allocated_text[0] = txt;

		for (int i = 1; i < size; i++) {
			txt = fgetc(read_file);
			allocated_text[i] = txt;
		}

		allocated_text[length(allocated_text) - 8] = '\0';
		
		fclose(read_file);

		return allocated_text;
	}
#endif
