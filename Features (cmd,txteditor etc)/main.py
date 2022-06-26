# Python cmd main.py
# Main file

# COLORED TEXT FORMATTER:

class clrs():
    def rgbcolor(r,g,b,txt,end=None):
        r,g,b = str(r),str(g),str(b);
        if(end == ""): return f'\u001b[38;2;{r};{g};{b}m'+txt;
        return f'\u001b[38;2;{r};{g};{b}m'+txt+"\u001B[0m";

# ERROR CATCHING
# IMPORT ALL MODULES/LIBS

try:
    import os, texteditor, dec, find, gcwd_, runpy, colorama, pyplus, math, subprocess, music
    from py_console import console;
    import mathfunctions as mathf;
except ImportError as err:
    import os, math;
    os.system("");
    print(clrs.rgbcolor(200,0,0,"",""),end='');
    try:
        from py_console import console;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import texteditor;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import dec;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import find;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import colorama;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import gcwd_;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import runpy;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import pyplus;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import subprocess;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import music;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);
    try:
        import mathfunctions as mathf;
    except Exception as e:
        print('Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:',e);

# Startup

os.system("");

# Start functions

def findRange(path,size_min,size_max,delete):
    if(os.path.isfile(path)): console.error("Error:",path,"is a file, not a directory."); return -1;
    for x,v in enumerate(os.listdir(path)):
        truePath = path+"/"+v;
        if(os.path.isfile(truePath)):
            size = os.path.getsize(truePath);
            if(size > size_min and size < size_max and delete == False):
                print(str(size),"bytes:\t",truePath);
                continue;
            if(size > size_min and size < size_max and delete == True):
                os.remove(truePath);
                print("Removed file:\t",truePath);
            continue;
        findRange(truePath,size_min,size_max,delete)
    return 0;

def zeroBytes(path,_size,delete):
    if(os.path.isfile(path)): console.error("Error:",path,"is a file, not a directory."); return -1;
    for x,v in enumerate(os.listdir(path)):
        truePath = path+"/"+v;
        if(os.path.isfile(truePath)):
            size = os.path.getsize(truePath);
            if(size == _size and delete == False):
                print(str(_size),"bytes:\t",truePath);
                continue;
            if(size == _size and delete == True):
                os.remove(truePath);
                print("Removed file:\t",truePath);
            continue;
        zeroBytes(truePath,_size,delete);
    return 0;

def convertBytes(bytes):
    if(bytes == 0): return "0 byte(s)\t\t";
    bytes_name = ("byte(s)\t\t","kilobyte(s)\t","megabyte(s)\t","gigabyte(s)\t","terabyte(s)\t","petabyte(s)\t","exabyte(s)\t","zettabyte(s)\t","yottabyte(s)\t");
    i = int(math.floor(math.log(bytes, 1000)));
    p = math.pow(1000, i);
    convertedBytes = round(bytes / p, 2);
    if(len(str(convertedBytes)) < 4):
        return "%s %s" % (convertedBytes, bytes_name[i]+"\t");
    return "%s %s" % (convertedBytes, bytes_name[i]);

def getDirSize(path):
    if(os.path.isfile(path)): console.error("Error:",path,"is a file, not a directory."); return -1;
    size = 0;
    for x,v in enumerate(os.listdir(path)):
        truePath = path+"/"+v;
        if(os.path.isfile(truePath)):
            size += os.path.getsize(truePath);
            continue;
        size += getDirSize(truePath);
    return size;

def getcwd():
    return gcwd_.getcwd();

def updateDir():
    try:
        with open(getcwd()+"/vars/dir","r") as d:
            return d.read().replace("â €","⠀");
    except Exception as err:
        console.error("Error:",err);

def updatePath():
    try:
        pathVars = {};
        for i,v in enumerate(os.listdir(getcwd()+"/vars/path/")):
            with open(getcwd()+"/vars/path/"+v) as path:
                pathVars[v] = path.read().replace("â €","⠀");
    except Exception as err:
        console.error("Error:",err);
    return pathVars;

def openPyEdit(path_to_file):
    try:
        if(not os.path.exists(path_to_file)): console.error("Error: Path doesn't exist."); return 1;
        if(not os.path.exists(Vars.path["idle"])): console.error("Error: IDLE Path doesn't exist."); return 1;
        if(not os.path.isfile(path_to_file)): console.error("Error: Path must be a file."); return 1;
        subprocess.call("py",[Vars.path["idle"], path_to_file]);
        return 0;
    except Exception as err:
        console.error("Error:",err);
        return 1;

# Start variables

class Vars:
    directory = updateDir();
    path = updatePath();

# Commands

def cmd(command):

    # Math commands (Coming soon)

    if(command[0:3] == "lcm"):
        try:
            firstSpace = command.find(" ")+1;
            secondSpace = command.find(" ", firstSpace)+1;
            if(firstSpace + secondSpace == -2): console.error("Error: Incorrect usage."); return 1;
            if(secondSpace == -1): secondSpace = firstSpace;
            firstDig = int(command[firstSpace:secondSpace].lstrip().rstrip());
            secondDig = int(command[secondSpace:].lstrip().rstrip());
            print("Lowest common multiple:", str(mathf.lcm(firstDig,secondDig)));
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Play music command

    if(command[0:4] == "play"):
        try:
            firstSpace = command.find(" ");
            if(firstSpace == -1): console.error("Error: Incorrect usage."); return 1;
            operator = command[firstSpace+1:firstSpace+3].lstrip();
            if(operator == "-l"):
                playlist = command[firstSpace+3:].lstrip();
                if(os.path.exists(playlist)):
                    if(os.path.isdir(playlist)):
                        for i,v in enumerate(os.listdir(playlist)):
                            print("Now playing:",v);
                            music.play(playlist+"/"+v);
                        return 0;
                    console.error("Error: Path must be a directory.");
                    return 1;
                trueDir = Vars.directory+"/"+playlist;
                if(os.path.exists(trueDir)):
                    if(os.path.isdir(trueDir)):
                        for i,v in enumerate(os.listdir(trueDir)):
                            print("Now playing:",v);
                            music.play(trueDir+"/"+v);
                        return 0;
                    console.error("Error: Path must be a directory.");
                    return 1;
                console.error("Error: Path does not exist.");
                return 1;
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Find command
    
    if(command[0:4] == "find"):
        try:
            fileSize = command.find("-s ");
            if(fileSize != -1):
                fileSize = int(command[fileSize+3:].rstrip());
                for x,v in enumerate(os.listdir(Vars.directory)):
                    truePath = Vars.directory+"/"+v;
                    if(os.path.isfile(truePath)):
                        if(os.path.getsize(truePath) == fileSize):
                            print(str(fileSize),"bytes:\t",truePath);
                        continue;
                    zeroBytes(truePath,fileSize,False);
                return 0;
            maxSize = command.find("+m ");
            minSize = command.find("-m ");
            if(maxSize != -1 and minSize != -1):
                if(maxSize > minSize):
                    minSize = int(command[minSize+3:command.find(" ",minSize+3)].rstrip());
                    maxSize = int(command[maxSize+3:].rstrip());
                else:
                    minSize = int(command[minSize+3:].rstrip());
                    maxSize = int(command[maxSize+3:command.find(" ",maxSize+3)].rstrip());
                for x,v in enumerate(os.listdir(Vars.directory)):
                    truePath = Vars.directory+"/"+v;
                    if(os.path.isfile(truePath)):
                        if(os.path.getsize(truePath) >= minSize and os.path.getsize(truePath) <= maxSize):
                            print(str(os.path.getsize(truePath)),"bytes:\t",truePath);
                        continue;
                    findRange(truePath,minSize,maxSize,False);
                return 0;
            console.error("Error: Incorrect usage.");
            return 1;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Shutdown command

    if(command[0:8] == "shutdown"):
        try:
            operator = command[9:11].lstrip().rstrip();
            # Shutdown
            if(operator == "-s"): os.system("shutdown -s 50"); os.system("shutdown /a");
            # Restart
            if(operator == "-r"): os.system("shutdown -r 0"); os.system("shutdown /a");
            # Log off
            if(operator == "-l"): os.system("shutdown -l 0"); os.system("shutdown /a");
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Run from path

    if(command[0:4] == "runp"):
        try:
            if(not os.path.exists(getcwd()+"/vars/path/"+command[5:].lstrip())): console.error("Error: Path variable does not exist."); return 1;
            path = Vars.path[command[5:].lstrip()];
            if(not os.path.exists(path)): console.error("Error: Path variable is invalid (It doesn't exist).",path); return 1;
            os.startfile(path);
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;
    
    # Path editor

    if(command[0:4] == "path"):
        try:
            firstSpace = command.find(" ");
            if(firstSpace == -1): console.error("Error: Incorrect usage. See -py for help."); return 1;
            operator = command[firstSpace:firstSpace+3].lstrip().rstrip();
            path_var = command[firstSpace+3:].lstrip().rstrip();
            if(operator == "-c"):
                with open(getcwd()+"/vars/path/"+path_var,"x") as createPath:
                    file = input("Replace with (" + Vars.directory + ") >> ");
                    fullFile = Vars.directory+"/"+file;
                    if(not os.path.exists(fullFile)): console.error("Error: Path does not exist ('"+fullFile+"')"); return 1;
                    if(not os.path.isfile(fullFile)): console.error("Error: Path must be a file."); return 1;
                    createPath.write(fullFile.replace("⠀","â €"));
                return 0;
            if(not os.path.exists(getcwd()+"/vars/path/"+path_var)): console.error("Error: Path does not exist ('"+path_var+"')"); return 1;
            if(operator == "-e"):
                file = input("Replace with (" + Vars.directory + ") >> ");
                fullFile = Vars.directory+"/"+file;
                if(not os.path.exists(fullFile)): console.error("Error: Path does not exist ('"+fullFile+"')"); return 1;
                if(not os.path.isfile(fullFile)): console.error("Error: Path must be a file."); return 1;
                with open(getcwd()+"/vars/path/"+path_var,"w") as writePath:
                    writePath.write(fullFile.replace("⠀","â €"));
                Vars.path = updatePath();
                return 0;
            if(operator == "-r"):
                with open(getcwd()+"/vars/path/"+path_var,"r") as readPath:
                    print(path_var+":",readPath.read().replace("â €","⠀"));
                return 0;

        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Change parent directory

    if(command == "rd"):
        try:
            if(Vars.directory.count("/") == 0): console.error("Error: Cannot have a null path."); return 1;
            Vars.directory = Vars.directory[0:find.find(Vars.directory,"/",Vars.directory.count("/")-1)-1];
            with open(getcwd()+"/vars/dir","w") as d:
                d.write(Vars.directory.replace("⠀","â €"));
            Vars.directory = updateDir();
            return 0;
        except Exception as err:
            console.error("Error",err);
            return 1;
    
    # Dir command

    if(command[0:3] == "dir"):
        try:
            if(len(command) == 3):
                print("\nDirectory",Vars.directory+":\n");
                dirs = files = 0;
                for x,v in enumerate(os.listdir(Vars.directory)):
                    truePath = Vars.directory+"/"+v;
                    if(os.path.isfile(truePath)):
                        print(convertBytes(os.path.getsize(truePath))+"\t<File>\t"+v);
                        files += 1;
                        continue;
                    print(convertBytes(getDirSize(truePath))+"\t<Dir>\t"+v);
                    dirs += 1;
                print("\n\t"+convertBytes(getDirSize(Vars.directory))+"\n\t"+str(files)+" file(s)\n\t"+str(dirs)+" dir(s)\n");
                return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Python command
    # Currently supports running python files

    if(command[0:2] == "py"):
        try:
            firstSpace = command.find(" ")+1;
            function = command[firstSpace:firstSpace+2].lstrip();
            if(function == "-r"):
                p = command[firstSpace+3:].lstrip();
                path = Vars.directory+"/"+p;
                if(not os.path.exists(path)): console.error("Error: Path does not exist ('"+path+"')"); return 1;
                tmpdir = getcwd()+"/temp/"+p;
                tempfile = open(tmpdir,"w");
                readfile = open(path,"r");
                tempfile.write("import msvcrt as BAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm;\n"+readfile.read()+'\nprint("This process has finished, press any key to exit...");\nBAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm.getch();\n');
                readfile.close();
                tempfile.close();
                subprocess.call(["py",tmpdir]);
                os.remove(tmpdir);
                return 0;
            console.error("Error: See -py for syntax");
            return 1;
        except Exception as err:
            console.error("Error:",err);
            return 1;
    
    # Python+ compile/run

    #if(command[0:3] == "py+"):
    #    try:
    #        firstSpace = command.find(" ");
    #        if(command[firstSpace+1:firstSpace+8].lstrip() == "compile"):
    #            file = command[firstSpace+9:];
    #            absdir = Vars.directory+"/"+file;
    #            if(os.path.exists(absdir)):
    #                f = open(absdir,"r").read();
    #                pyplus.compile(f);
    #                return 0;
    #            else:
    #                console.error("Error: File not found ('"+absdir+"')");
    #                return 1;
    #    except Exception as err:
    #        console.error("Error:",err);
    #        return 1;

    # Make folder command

    if(command[0:5] == "mkdir"):
        try:
            firstSpace = command.find(" ");
            if(firstSpace == -1): console.error("Error: You must enter a path."); return 1;
            directoryName = command[firstSpace:].lstrip();
            if(directoryName == ""): console.error("Error: Path does not exist ('')"); return 1;
            fullDir = Vars.directory+"/"+directoryName;
            if(os.path.exists(fullDir)): console.error("Error: Path already exists ('"+fullDir+"')"); return 1;
            os.mkdir(fullDir);
        except Exception as err:
            console.error("Error:",err);
            return 1;
        if(os.path.exists(fullDir)): console.success("Sucessfully created directory:",fullDir); return 0;
        console.error("Error: Something went wrong creating directory,",fullDir);
        return 1;

    # Delete folder command

    if(command[0:5] == "rmdir"):
        try:
            firstSpace = command.find(" ");
            if(firstSpace == -1): console.error("Error: You must enter a path."); return 1;
            directoryName = command[firstSpace:].lstrip();
            if(directoryName == ""): console.error("Error: Path does not exist ('')"); return 1;
            fullDir = Vars.directory+"/"+directoryName;
            if(not os.path.exists(fullDir)): console.error("Error: Path does not exist ('"+fullDir+"')"); return 1;
            os.rmdir(fullDir);
        except Exception as err:
            console.error("Error:",err);
            return 1;
        if(not os.path.exists(fullDir)): console.success("Sucessfully deleted directory:",fullDir); return 0;
        console.error("Error: Something went wrong deleting directory,",fullDir);
        return 1;

    # Exit/close command

    if(command == "close" or command == "exit"):
        quit();
    
    # Restart/reload command

    if(command == "restart" or command == "reload"):
        print("Reloading...");
        runpy.run_path(getcwd()+"/main.py");
        return 0;

    # cls/clear command
    
    if(command == "cls" or command == "clear"):
        print("Clearing...");
        try:
            os.system("cls||clear");
        except Exception as err:
            console.error("Error:",err);
        return 0;
    
    # Text editor command
    
    if(command[0:3] == "txt"):
        texteditor.Write(command[4:]);
        return 0;

    # Change directory
    
    if(command[0:2] == "cd"):
        try:
            # Path variable
            
            path = command[2:].lstrip().replace(" ","\n").replace("\\","/").replace("/"," ").rstrip().replace(" ","/").replace("\n"," ").rstrip();

            # If you simply enter "cd" - or "cd            " etc, it will cause this error.

            if(len(path) < 1):
                console.error("Error: Path does not exist ('"+path+"').");
                return 1;

            # Check if path exists and if it does, update the directory.

            if(os.path.exists(path)):
                with open(getcwd()+"/vars/dir","w") as d:
                    d.write(path.replace("⠀","â €"));
                Vars.directory = updateDir();
                return 0;
            if(os.path.exists(Vars.directory+"/"+path)):
                with open(getcwd()+"/vars/dir","w") as d:
                    d.write(Vars.directory.replace("⠀","â €")+"/"+path.replace("⠀","â €"));
                Vars.directory = updateDir();
                return 0;
            
            # If it doesn't exist, print this error.

            console.error("Error: Path does not exist ('"+path+"').");
            return 1;

        # Error catching.

        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Convert from base 2-36 command.

    if(command[0:4] == "base"):
        # Finds the first dash (For easier use - I had to use it a lot so i stored it in this variable).
        firstDash = command.find("-");
        if(command.count("-") == 2):

            # Set what base you are converting from, and to in these variables.

            _from = command[firstDash+1:command.find(" ",firstDash)];
            to = command[find.find(command,"-",1):command.find(" ",find.find(command,"-",1))];
        else:
            
            # If there is only 1 "-", then presume that the value after "#" is in denary and set variables accordingly.

            to = command[firstDash+1:command.find(" ",firstDash)];
            _from = 10;
        try:
            
            # Convert to and _from variables to integers and set the value to anything typed after "#".

            value = command[command.find("#")+1:];
            to,_from = int(to),int(_from);

        # Error catching.

        except Exception as err:
            console.error("Error:",err,"\nThis may be due to a syntax error, type '-base' for info.");
            return 1;

        # Convert to the stated base digit.

        try:
            if(_from != 10): value = dec.toDec(value, _from);
            print(dec.fromDec(int(value),to));
        
        # Error catching.

        except Exception as err:
            console.error("Error:",err,"\nThis may be due to a syntax error, type '-base' for info.");
            return 1;
        
        # If no errors, return 0.

        return 0;

    # Convert base command help syntax.

    if(command[0:5] == "-base"):
        print(colorama.Fore.LIGHTBLACK_EX + "Try typing:\n*base -[from] -[*to] #[*value]" + colorama.Fore.RESET);
        return 0;

    # If no command was found (no value has been returned yet), print this error and return 1.

    console.error("Error: Command not found:",command);
    return 1;

# Main

def Main():
    while(1):
        i = input(clrs.rgbcolor(159, 60, 230, Vars.directory) + clrs.rgbcolor(106, 224, 52, " ~ ") + clrs.rgbcolor(224, 146, 29,"",""));
        print(colorama.Fore.CYAN, end="");
        try:
            cmd(i);
        except Exception as err:
            print("Error:",err);
Main();
