/* C library for safely opening, reading, writing and appending to files */

#ifndef __OPEN_H

	#ifndef __STRING_H
		#include "str.h"
	#endif

	#include <stdlib.h>
	#include <stdio.h>

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

	/* Returns text in a file  (Must be freed after use) */
	char * file_read(const char * file) {
		
		FILE * read_file;

		/* Opening read file */

		read_file = fopen(file, "r");

		int size = file_getsize(file);

		char txt;
		char * allocated_text = (char *) malloc(size);

		for (int i = 0; i < size; i++) {
			txt = fgetc(read_file);
			allocated_text[i] = txt;
		}

		allocated_text[size] = '\0';
		
		fclose(read_file);

		return allocated_text;
		/* Remember to free after use */
	}

	void file_write(const char * file, char * raw_text) {

		FILE * write_file;
		
		/* Opening write file */

		write_file = fopen(file, "w");

		fwrite(raw_text, 1, length(raw_text), write_file);

		fclose(write_file);
	}

	void file_append(const char * file, char * raw_text) {

		FILE * append_file;
		
		/* Opening write file */

		append_file = fopen(file, "a");

		fwrite(raw_text, 1, length(raw_text), append_file);

		fclose(append_file);
	}
#endif
