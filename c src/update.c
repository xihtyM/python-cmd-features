#include "headers/clibs.h"

#include <stdio.h>
#include <urlmon.h>
#include <direct.h>

/* Install */
void install(char * dir) {

	/* URL of zipped file */

	const char * url = "https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip";

	/* Const directory path with / replaced to \\ */

	char * __dir = replace(dir, '/', '\\');

	/* Directory to zip file */

	char * dest = concat(__dir, "\\cmd.zip");
	
	/* Print location of zip file */

	printf("\nInstalling zip at: %s", dest);

	HRESULT dl = URLDownloadToFileA(NULL, url, dest, 0, NULL);

	if (S_OK == dl) {
		printf("\nSucessfully downloaded zipfile at: %s.", dest);
	} else {
		printf("\nSomething went wrong downloading zipfile at: %s.", dest);
		return;
	}

	char * cmd = concat(
		concat("powershell -Command \"Microsoft.PowerShell.Archive\\Expand-Archive -Path \'", dest),
		concat("\' -DestinationPath \'", concat(__dir, "\'\""))
	);

	system(cmd);

	free(__dir);
	free(cmd);

	remove(dest);

	free(dest);

	printf("\nSucessfully installed!\n");
}

int main(void) {
	/* Windows is the only supported os in this version */
	#if __WIN__f == false
		printf("Operating system is not supported:\n%s", CurrentOS)
		return 1;
	#endif

	/* Getting directories */
	char * cwd = os_getcwd();

	/* Presuming the parent of the parent of cwd is cmd */
	char * cmd_path = os_getparent(os_getparent(cwd));

	/* Guard */
	if(!os_isdir(cmd_path)) {
		printf("Error: Directory does not exist.\nThis may be due to special characters in the name of one of the parent folders.\nYou will see a '?' character for unknown characters in the directory.\n\nDirectory: %s\n\n", cmd_path);
		system("pause");
		return 1;
	}

	/* Code */

	char * temp_dir = concat(cmd_path, "\\temp");
	char * new_dir = concat(temp_dir, "\\cmd_new_files.py");

	if(os_isdir(new_dir)) {
		_rmdir(new_dir);
	}
	_mkdir(new_dir);

	install(new_dir);

	printf("Updating...");

	char * new_dir_cmd = concat(new_dir, "\\cmd");

	int index = 1;
	char * files = os_listdir(new_dir_cmd, index);
	while (files != "N/A") {
		index++;
		char * path = concat(new_dir_cmd, concat("\\", files));
		char * c_path = concat(cmd_path, concat("\\", files));
		if (os_isfile(path)) {
			printf("Test: %s : %s", path, c_path);
			file_write(c_path, file_read(path));
		}
		free(c_path);
		free(path);
		files = os_listdir(new_dir_cmd, index);
	}
	
	_rmdir(new_dir);
	/* Free memory */
	free(cmd_path);
	free(new_dir_cmd);
	free(new_dir);
	free(temp_dir);

	system("pause");

	return 0;
}
