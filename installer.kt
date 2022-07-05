/* INSTALLER IN JAVA (EXE COMING SOON!) */
/* INSTALLER.KT */

/* IMPORTS */

import java.nio.file.Paths
import java.io.File
import java.net.URL
import java.nio.file.Files

/* System(cmd) command */

fun system(__cmd: String) {
	Runtime.getRuntime().exec(__cmd);
}

/* RGB */

fun rgbcolor(r: Int, g: Int, b: Int, txt: String): String { return "\u001b[38;2;$r;$g;${b}m$txt\u001B[0m" } fun resetcolor() { print("\u001B[0m") }

/* YES OR NO FUNCTION */

fun Y_OR_NO(__MESSAGE: String): Boolean {

	var inp: String = ""

	while(inp == "" || inp != "y" && inp != "n") {
		print(__MESSAGE)
		inp = readLine().toString().lowercase()
	}

	return inp == "y"
}

/* IF DIRECTORY */

fun isDir(path: String): Boolean {
	var dir = File(path)
	if(dir.isDirectory) {
		return true
	}
	println(rgbcolor(200,0,0,"Error: Path does not exist - $path"))
	return false
}

/* DOWNLOAD FILE */

fun downloadFile(url: URL, fileName: String) {
	try {
    	url.openStream().use { Files.copy(it, Paths.get(fileName)) }
	} catch(err: AccessDeniedException) {
		println(rgbcolor(200,0,0,"Error: Access denied, please run as administrator."))
		println(rgbcolor(200,0,0, err.toString()))
	} catch(err: FileAlreadyExistsException) {
		println(rgbcolor(200,0,0,"Error: File already exists, please use an empty folder or rename cmd.zip"))
		println(rgbcolor(200,0,0, err.toString()))
		run()
	}
}

/* FINALIZE (ADD LIBRARIES, UNZIP AND CREATE SHORTCUT) */

fun finalize(file: String, dir: String) {

	println("Unzipping file...")

	var currOS = System.getProperty("os.name").lowercase()

	/* IF ON WINDOWS */

	if(currOS.contains("win")) {

		/* UNZIP COMMAND WINDOWS */

		system("powershell -Command Expand-Archive -Path $file -DestinationPath $dir")

		/* SUCCESS MESSAGE */

		println(rgbcolor(0,200,0,"Sucessfully unzipped file."))

		/* CREATE SHORTCUT */

		var cShrt = Y_OR_NO("Would you like to create a shortcut on the desktop [Y/N]? ")

		if(cShrt) {
			system("mklink")
		}
		else {
			return
		}

	}

	/* IF ON UNIX OS */

	else if(currOS.contains("nix") || currOS.contains("nux") || currOS.contains("aix")) {

		/* UNZIP COMMAND LINUX/UNIX */

		system("unzip $file -d $dir")

		/* SUCCESS MESSAGE */

		println(rgbcolor(0,200,0,"Sucessfully unzipped file."))

		/* CREATE SHORTCUT */

		var cShrt = Y_OR_NO("Would you like to create a shortcut on the desktop [Y/N]? ")

		if(cShrt) {
			system("ln -s $dir\\cmd\\main.py PyCommandPrompt")
		}
		else {
			return
		}

	}

	/* IF ON MACOS */

	else if(currOS.contains("mac")) {

		/* UNZIP COMMAND MAC */

		system("unzip $file - d $dir")

		/* SUCCESS MESSAGE */

		println(rgbcolor(0,200,0,"Sucessfully unzipped file."))

	}

	/* IF ON UNSUPPORTED OS */

	else {
		println(rgbcolor(200,0,0,"Unfortunately, your os is not supported. You will have to unzip and create a shortcut to the file manually."))
	}
}

/* INSTALL */

fun install(path: String) {
	var file = "$path\\cmd.zip"
	downloadFile(URL("https://github.com/xihtyM/python-cmd-features/raw/master/Zipped%20files/Latest%20Release/cmd.zip"), file)
	finalize(file, path)
	system("pip install pypiwin32 winshell colorama py-console GitPython gitdb pypi requests pytest-shutil")
	File(file).deleteOnExit()
}

fun run() {
	var path = "";
	println(rgbcolor(200,0,0,"If you haven't got all required python libraries, run fixer.exe after installing..."))
	while(path == "" || isDir(path) == false) {
		print(rgbcolor(0,200,0,"Installation Directory: "))
		path = readLine().toString()
		resetcolor()
	}
	try {
		install(path)
	} catch(err: AccessDeniedException) {
		println(rgbcolor(200,0,0,"Error: Access denied, please run as administrator."))
		println(rgbcolor(200,0,0,err.toString()))
	}
}

fun main() {
	run()
	print("This process has finished, press enter to close window... ")
	readLine()
}
