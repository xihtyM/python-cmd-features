/*
  INSTALLER IN JAVA (EXE COMING SOON!)
  INSTALLER.KT
*/

// IMPORTS

import java.nio.file.Paths
import java.io.File
import java.net.URL
import java.nio.file.Files
import java.util.zip.ZipFile

// RGB

fun rgbcolor(r: Int, g: Int, b: Int, txt: String): String { return "\u001b[38;2;$r;$g;${b}m$txt\u001B[0m" } fun resetcolor() { print("\u001B[0m") }

fun isDir(path: String): Boolean {
	var dir = File(path)
	if(dir.isDirectory) {
		return true
	}
	println(rgbcolor(200,0,0,"Error: Path does not exist - $path"))
	return false
}

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

fun unzipFile(file: String) {
	println("Unzipping file...")
	// 100% my code ;D *sarcasm*
	ZipFile(file).use { zip ->
		zip.entries().asSequence().forEach { entry ->
			zip.getInputStream(entry).use { input ->
				File(entry.name).outputStream().use { output ->
					input.copyTo(output)
				}
			}
		}
	}
	println(rgbcolor(0, 200, 0, "Sucessfully installed cmd!"))
}

fun install(path: String) {
	var file = "$path\\cmd.zip"
	downloadFile(URL("https://github.com/xihtyM/python-cmd-features/blob/master/Zipped%20files/Latest%20Release/cmd.zip?raw=true"), file)
	unzipFile(file)
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
