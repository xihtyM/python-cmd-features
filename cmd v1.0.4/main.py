# Python cmd main.py
# Main file

# CONSTANTS

class CONST:
    IMPORT_ERROR_MSG = 'Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:';

# COLORED TEXT FORMATTER:

class clrs():
    def rgbcolor(r: int, g: int, b: int, txt: str, end: str = "\u001B[0m"):
        r, g, b = str(r), str(g), str(b);
        return f'\u001b[38;2;{r};{g};{b}m{txt}{end}';

# ERROR CATCHING
# IMPORT ALL MODULES/LIBS

try:
    import os, texteditor, dec, find, runpy, pyplus, math, subprocess, music, shutil, socket;
    from gcwd_ import getcwd;
    from py_console import console;
    import mathfunctions as mathf;
except ImportError as err:
    import os, math;

    os.system("");

    print(clrs.rgbcolor(200,0,0,"",""),end='');
    try:
        from py_console import console;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        from socket import console;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import shutil;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import texteditor;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import dec;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import find;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        from gcwd_ import getcwd;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import runpy;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import pyplus;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import subprocess;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import music;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);
    try:
        import mathfunctions as mathf;
    except ImportError as e:
        print(CONST.IMPORT_ERROR_MSG,e);

# Startup

os.system("");

# Start functions

def findRange(path: str, size_min: int, size_max: int, delete: bool = False) -> None:
    if(os.path.isfile(path)): console.error(f"Error: {path} is a file, not a directory."); return;
    for x, v in enumerate(os.listdir(path)):
        truePath = path + "/" + v;
        if(os.path.isfile(truePath)):
            size = os.path.getsize(truePath);
            if(size >= size_min and size <= size_max and delete == False):
                print(str(size),"bytes:\t",truePath);
            if(size >= size_min and size <= size_max and delete == True):
                os.remove(truePath);
                print("Removed file:\t",truePath);
            continue;
        findRange(truePath,size_min,size_max,delete)

def zeroBytes(path: str, _size: int, delete: bool = False) -> None:
    if(os.path.isfile(path)): console.error(f"Error: {path} is a file, not a directory."); return;
    for x, v in enumerate(os.listdir(path)):
        truePath = path + "/" + v;
        if(os.path.isfile(truePath)):
            size = os.path.getsize(truePath);
            if(size == _size and delete == False):
                print(str(_size),"bytes:\t",truePath);
            if(size == _size and delete == True):
                os.remove(truePath);
                print("Removed file:\t",truePath);
            continue;
        zeroBytes(truePath,_size,delete);

def convertBytes(bytes: int) -> str:
    try:
        bytes = int(bytes);
    except ValueError:
        console.error("Bytes cannot be converted to an integer properly...");
        return "ERROR";
    if(bytes == 0): return "0 byte(s)\t\t";
    bytes_name: tuple = ("byte(s)\t\t","kilobyte(s)\t","megabyte(s)\t","gigabyte(s)\t","terabyte(s)\t","petabyte(s)\t","exabyte(s)\t","zettabyte(s)\t","yottabyte(s)\t");
    i = int(math.floor(math.log(bytes, 1000)));
    p = math.pow(1000, i);
    convertedBytes = round(bytes / p, 2);
    if(len(str(convertedBytes)) < 4):
        return "%s %s" % (convertedBytes, bytes_name[i]+"\t");
    return "%s %s" % (convertedBytes, bytes_name[i]);

def getDirSize(path: str) -> int:
    if(os.path.isfile(path)): console.error("Error:", path, "is a file, not a directory."); return 0;
    size = 0;
    try:
        for x,v in enumerate(os.listdir(path)):
            truePath = path + "/" + v;
            if(os.path.isfile(truePath)):
                try:
                    size += os.path.getsize(truePath);
                except Exception as err:
                    console.error("Error:",err);
                    # RESET COLOR
                    print("\u001b[36;2m", end="");
                continue;
            size += getDirSize(truePath);
    except Exception as err:
        console.error("Error:",err);
        # RESET COLOR
        print("\u001b[36;2m", end="");
    return size;

def updateDir() -> str:
    try:
        with open(getcwd()+"/vars/dir","r", encoding = "utf-8") as d:
            return d.read();
    except Exception as err:
        console.error("Error:",err);
        return "ERROR";

def updatePath() -> dict:
    try:
        pathVars = {};
        for i,v in enumerate(os.listdir(getcwd()+"/vars/path/")):
            with open(getcwd()+"/vars/path/"+v,"r", encoding = "utf-8") as path:
                pathVars[v] = path.read();
    except Exception as err:
        console.error("Error:",err);
    return pathVars;

def openPyEdit(path_to_file: str):
    try:
        if(not os.path.exists(path_to_file)): console.error("Error: Path doesn't exist."); return 1;
        if(not os.path.exists(Vars.path["idle"])): console.error("Error: IDLE Path doesn't exist."); return 1;
        if(not os.path.isfile(path_to_file)): console.error("Error: Path must be a file."); return 1;
        subprocess.call("py",[Vars.path["idle"], path_to_file]);
        return 0;
    except Exception as err:
        console.error("Error:",err);
        return 1;

def extension(__p: str) -> str:
    return __p[find.find(__p, ".", __p.count(".") - 1) : len(__p)];

def cmd_args(__cmd: str) -> list:
    arr = [];
    args = "";
    prev = True;
    quotes = False;
    for _ind in range(len(__cmd)):
        if(__cmd[_ind] != " " or quotes == True):
            if(__cmd[_ind] in ('"',"'")): quotes = not quotes; continue;
            args += __cmd[_ind];
            prev = False;
            continue;
        if(prev == False and quotes == False):
            arr.append(args);
            args = "";
            prev = True;
            continue;
        prev = True;
    if(args != ""):
        arr.append(args);
    return arr;

def arglen(__cmd) -> int:
    return (len(__cmd), len(cmd_args(__cmd))) [type(__cmd) == str];

def argsplit(__cmd, _n, __n, sep = " ") -> str:
    if(__n < _n):
        console.error("Error splitting arguments: Second value is smaller.");
    if(__n > len(__cmd)-1):
        __n = len(__cmd)-1;
    ind = _n;
    end = __cmd[ind];
    for i in range(__n - _n):
        ind += 1;
        end += sep + __cmd[ind];
    return end;

# Start variables

class Vars:
    directory = updateDir();
    path = updatePath();

# Commands

def cmd(command: str):

    # Const command

    ARGS = cmd_args(command);

    # Check if args has at least one argument

    if(not ARGS): console.error("Error: Expected at least 1 argument, got 0."); return 1;

    if(ARGS[0] == "ip"):
        if(arglen(ARGS) == 1):
            local_host_name = socket.gethostname();
            private_ip = socket.getaddrinfo(local_host_name, 0, family=socket.AddressFamily.AF_INET)[0];
            private_ip = private_ip[len(private_ip) - 1][0];
            print("Your local host name is: " + local_host_name + "\nYour public ip address is: N/A\nYour private ip address is: " + str(private_ip));
        if(arglen(ARGS) == 2):
            return 1;
        return 0;

    # Add to valid letters and other stuff

    if(ARGS[0] == "add"):
        try:
            if(arglen(ARGS) < 2): console.error(f"Error: Expected at least 2 args, got {arglen(ARGS)}."); return 1;
            operator = ARGS[1];
            # Add to valid letters
            if(operator == "-tx"):
                char_ = ARGS[2];
                with open(f"{getcwd()}\\valid_ltrs.py", "r", encoding = "utf-8") as valid_letters_r:
                    ltrs = valid_letters_r.read();
                for v in char_:
                    if(ltrs.find(v) != -1): console.error(f"Error: Letter already exists - {v}"); return 1;
                with open(f"{getcwd()}\\valid_ltrs.py", "w", encoding = "utf-8") as valid_letters_w:
                    valid_letters_w.write(ltrs[0:len(ltrs)-3] + char_ + "\";");
                return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Math commands

    if(ARGS[0] == "lcm"):
        try:
            if(arglen(ARGS) != 3): console.error(f"Error: Expected 3 args, got {arglen(ARGS)}."); return 1;
            firstDig = int(ARGS[1]);
            secondDig = int(ARGS[2]);
            print("Lowest common multiple:", str(mathf.lcm(firstDig,secondDig)));
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Play music command

    if(ARGS[0] == "play"):
        try:
            if(arglen(ARGS) < 2): console.error(f"Error: Expected at least 2 args, got {arglen(ARGS)}."); return 1;
            operator = ARGS[1];
            if(operator == "-l"):
                if(arglen(ARGS) < 3): console.error(f"Error: Expected at least 3 args, got {arglen(ARGS)}."); return 1;
                playlist = ARGS[2];
                if(os.path.exists(playlist)):
                    if(os.path.isdir(playlist)):
                        for i,v in enumerate(os.listdir(playlist)):
                            if(extension(v) != "mp3"): continue;
                            print("Now playing:",v);
                            music.play(playlist+"/"+v);
                        return 0;
                    console.error("Error: Path must be a directory.");
                    return 1;
                trueDir = Vars.directory+"/"+playlist;
                if(os.path.exists(trueDir)):
                    if(os.path.isdir(trueDir)):
                        for i,v in enumerate(os.listdir(trueDir)):
                            if(extension(v) != "mp3"): continue;
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
    
    if(ARGS[0] == "find"):
        try:
            if(arglen(ARGS) < 3): console.error(f"Error: Expected at least 3 args, got {arglen(ARGS)}."); return 1;
            if("-s" in ARGS):
                fileSize = int(ARGS[ARGS.index("-s")+1]);
                for x,v in enumerate(os.listdir(Vars.directory)):
                    truePath = Vars.directory+"/"+v;
                    if(os.path.isfile(truePath)):
                        if(os.path.getsize(truePath) == fileSize):
                            print(str(fileSize),"bytes:\t",truePath);
                        continue;
                    zeroBytes(truePath,fileSize,False);
            maxSize, minSize = 9999999999999999, 0;
            if("-m" in ARGS):
                minSize = int(ARGS[ARGS.index("-m")+1]);
            if("+m" in ARGS):
                maxSize = int(ARGS[ARGS.index("+m")+1]);
            if("+m" in ARGS or "-m" in ARGS):
                for x,v in enumerate(os.listdir(Vars.directory)):
                    truePath = Vars.directory+"/"+v;
                    if(os.path.isfile(truePath)):
                        if(os.path.getsize(truePath) >= minSize and os.path.getsize(truePath) <= maxSize):
                            print(str(os.path.getsize(truePath)),"bytes:\t",truePath);
                        continue;
                    findRange(truePath,minSize,maxSize,False);
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Shutdown command

    if(ARGS[0] == "shutdown"):
        try:
            operator = ARGS[1];
            # Shutdown
            if(operator == "-s"): os.system("shutdown /f");
            # Restart
            if(operator == "-r"): os.system("shutdown /r");
            # Log off
            if(operator == "-l"): os.system("shutdown /l");
            return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Run from path

    if(ARGS[0] == "runp"):
        try:
            path_var = ARGS[1];
            if(not os.path.exists(getcwd() + "/vars/path/" + path_var)): console.error("Error: Path variable does not exist."); return 1;
            path = Vars.path[path_var];
            if(not os.path.exists(path)): console.error("Error: Path variable is invalid.", path); return 1;
            os.startfile(path);
            return 0;
        except Exception as err:
            console.error("Error:", err);
            return 1;
    
    # Path editor

    if(ARGS[0] == "path"):
        try:
            if(arglen(ARGS) < 3): console.error(f"Error: Expected 3 args, got {arglen(ARGS)}."); return 1;
            operator = ARGS[1];
            path_var = ARGS[2];
            if(operator == "-c"):
                with open(getcwd() + "/vars/path/" + path_var, "x", encoding = "utf-8") as createPath:
                    file = input("Set path to (" + Vars.directory + ") >> ");
                    fullFile = Vars.directory + "/" + file;
                    if(not os.path.exists(fullFile)): console.error("Error: Path does not exist - " + fullFile); return 1;
                    if(not os.path.isfile(fullFile)): console.error("Error: Path must be a file."); return 1;
                    createPath.write(fullFile);
                return 0;
            if(not os.path.exists(getcwd() + "/vars/path/" + path_var)): console.error("Error: Path does not exist - " + path_var); return 1;
            if(operator == "-e"):
                file = input("Replace with (" + Vars.directory + ") >> ");
                fullFile = Vars.directory + "/" + file;
                if(not os.path.exists(fullFile)): console.error("Error: Path does not exist ('"+fullFile+"')"); return 1;
                if(not os.path.isfile(fullFile)): console.error("Error: Path must be a file."); return 1;
                with open(getcwd() + "/vars/path/" + path_var, "w", encoding = "utf-8") as writePath:
                    writePath.write(fullFile);
                Vars.path = updatePath();
                return 0;
            if(operator == "-r"):
                with open(getcwd() + "/vars/path/" + path_var, "r", encoding = "utf-8") as readPath:
                    print(path_var + ":", readPath.read());
                return 0;
        except Exception as err:
            console.error("Error:", err);
            return 1;

    # Change parent directory

    if(command == "rd"):
        try:
            if(Vars.directory.count("/") == 0): console.error("Error: Cannot have a null path."); return 1;
            Vars.directory = Vars.directory[0:find.find(Vars.directory, "/", Vars.directory.count("/")-1)-1];
            with open(getcwd() + "/vars/dir", "w", encoding = "utf-8") as d:
                d.write(Vars.directory);
            Vars.directory = updateDir();
            return 0;
        except Exception as err:
            console.error("Error", err);
            return 1;
    
    # Dir command

    if(ARGS[0] == "dir"):
        try:
            if(arglen(ARGS) == 1):
                print("\nDirectory", Vars.directory + ":\n");
                dirs = files = 0;
                for x,v in enumerate(os.listdir(Vars.directory + "\\")):
                    truePath = Vars.directory + "/" + v;
                    if(os.path.isfile(truePath)):
                        try:
                            print(convertBytes(os.path.getsize(truePath)) + "\t<File>\t" + v);
                        except Exception as err:
                            print("Error\t\t<File>\t" + v);
                            console.error("Error:", err);
                            # RESET COLOR
                            print("\u001b[36;2m", end="");
                        files += 1;
                        continue;
                    try:
                        print(convertBytes(getDirSize(truePath))+"\t<Dir>\t"+v);
                    except Exception as err:
                            print("Error\t\t<Dir>\t"+v);
                            console.error("Error:",err);
                            # RESET COLOR
                            print("\u001b[36;2m", end="");
                    dirs += 1;
                print("\n\t"+convertBytes(getDirSize(Vars.directory))+"\n\t"+str(files)+" file(s)\n\t"+str(dirs)+" dir(s)\n");
                return 0;
        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Python command
    # Currently supports running python files

    if(ARGS[0] in ("py","python")):
        try:
            function = ARGS[1];
            if(function == "-r"):
                p = ARGS[2];
                path = Vars.directory+"/"+p;
                if(not os.path.exists(path)): console.error("Error: Path does not exist ('"+path+"')"); return 1;
                #tmpdir = getcwd()+"/temp/"+p;
                #tempfile = open(tmpdir,"w");
                #readfile = open(path,"r");
                #tempfile.write('try: import os; os.chdir("'+Vars.directory+'");\nexcept Exception: print("There was an error changing to the working directory, this may break file."); pass;\nimport msvcrt as BAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm;\n'+readfile.read()+'\nprint("This process has finished, press any key to exit...");\nBAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm.getch();');
                #readfile.close();
                #tempfile.close();
                #subprocess.call(["py",tmpdir]);
                #os.remove(tmpdir);
                re = open(path,"r");
                contents = re.read();
                re.close();
                open(path,"w").close();
                wr = open(path,"w");
                wr.write(f'import msvcrt as BAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm;\n{contents}\nprint("This process has finished, press any key to exit...");\nBAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm.getch();');
                wr.close();
                try:
                    subprocess.call(['py', path]);
                    open(path,"w").close();
                    wrd = open(path,"w");
                    wrd.write(contents);
                    wrd.close();
                except Exception as err:
                    console.error(f"Error in {path}:",err);
                    open(path,"w").close();
                    wrd = open(path,"w");
                    wrd.write(contents);
                    wrd.close();
                    return 1;
                return 0;
            if(function == "-c"):
                filename = ARGS[2];
                path = Vars.directory+"/"+filename;
                if(not os.path.exists(path)): console.error("Error: File does not exist."); return 1;
                code = open(path,"r").readlines();
                pyplus.compile(code);
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

    if(ARGS[0] == "mkdir"):
        try:
            if(arglen(ARGS) != 2): console.error(f"Error: Expected 2 arguments, got {arglen(ARGS)}."); return 1;
            directoryName = ARGS[1];
            fullDir = Vars.directory+"/"+directoryName;
            if(os.path.exists(fullDir)): console.error(f"Error: Path already exists: {fullDir}"); return 1;
            os.mkdir(fullDir);
        except Exception as err:
            console.error("Error:",err);
            return 1;
        if(os.path.exists(fullDir)): console.success("Sucessfully created directory:",fullDir); return 0;
        console.error("Error: Something went wrong creating directory,",fullDir);
        return 1;

    # Delete folder command

    if(ARGS[0] == "rmdir"):
        try:
            if(arglen(ARGS) != 2): console.error(f"Error: Expected 2 arguments, got {arglen(ARGS)}."); return 1;
            directoryName = ARGS[1];
            allSlashes = True;
            for ind,chr in enumerate(directoryName):
                if(chr != "\\" and chr != "/"):
                    allSlashes = False;
                    break;
            if(allSlashes): console.error("Error: You must enter a valid path."); return 1;
            fullDir = Vars.directory+"/"+directoryName;
            if(not os.path.exists(fullDir)): console.error(f"Error: Path does not exist: {fullDir}"); return 1;
            try:
                os.rmdir(fullDir);
            except OSError:
                console.error("Error removing file, this may be because it is not empty.");
                yorno = "";
                while(yorno != "y" and yorno != "n"):
                    yorno = input("Do you still wish to delete this directory [Y/N]: ").lower();
                if(yorno == "y"):
                    shutil.rmtree(fullDir);
                    return 0;
                return 1;
        except Exception as err:
            console.error("Error:",err);
            return 1;
        if(not os.path.exists(fullDir)): console.success("Sucessfully deleted directory:",fullDir); return 0;
        console.error("Error: Something went wrong deleting directory,",fullDir);
        return 1;

    # Exit/close command

    if(command in ("close","exit")):
        quit();
    
    # Restart/reload command

    if(command in ("restart","reload")):
        print("Reloading...");
        runpy.run_path(getcwd() + "/main.py");
        return 0;

    # cls/clear command
    
    if(command in ("cls","clear")):
        print("Clearing...");
        try:
            os.system("cls||clear");
        except Exception as err:
            console.error("Error:",err);
        return 0;
    
    # Text editor command
    
    if(ARGS[0] == "txt"):
        texteditor.Write(ARGS[1]);
        return 0;

    # Change directory
    
    if(ARGS[0] == "cd"):
        try:
            # Path variable
            
            _path = ARGS[1].replace(" ","\n").replace("\\","/").replace("/"," ").rstrip().lstrip().replace(" ","/").replace("\n"," ").rstrip();
            path = "";

            # Formatting path

            prevSlash = False;
            for i,v in enumerate(_path):
                if(v == "/"):
                    if(prevSlash == True): continue;
                    path += v;
                    prevSlash = True;
                    continue;
                path += v;
                prevSlash = False;

            # Check if path exists and if it does, update the directory.

            if(os.path.exists(path)):
                with open(getcwd()+"/vars/dir","w", encoding = "utf-8") as d:
                    d.write(path);
                Vars.directory = updateDir();
                return 0;
            if(os.path.exists(Vars.directory+"/"+path)):
                with open(getcwd()+"/vars/dir","w", encoding = "utf-8") as d:
                    d.write(Vars.directory+"/"+path);
                Vars.directory = updateDir();
                return 0;
            
            # If it doesn't exist, print this error.

            console.error(f"Error: Path does not exist: {path}");
            return 1;

        # Error catching.

        except Exception as err:
            console.error("Error:",err);
            return 1;

    # Convert from base 2-36 command.

    if(ARGS[0] == "base"):
        if(arglen(ARGS) < 3): console.error("Error: Syntax error, type '-base' for info."); return 1;
        if(arglen(ARGS) == 4):

            # Set what base you are converting from, and to in these variables.

            _from = ARGS[1];
            to = ARGS[2];
            value = ARGS[3];
        else:
            
            # If there is only 1 "-", then presume that the value after "#" is in denary and set variables accordingly.

            to = ARGS[1];
            _from = 10;
            value = ARGS[2];
        try:
            
            # Convert to and _from variables to integers

            to,_from = int(to), int(_from);

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

    if(ARGS[0] == "-base"):
        print("\u001b[90;2;mTry typing:\nbase from to value\nbase to value\nIf you do not include what base you are converting from, pycmd will assume it to be base10.\u001b[36;2m");
        return 0;

    # Python help syntax

    if(ARGS[0] in ("-py","-python")):
        print("\u001b[90;2;mTry typing:\npy -r file_to_run\npy -c file_to_compile (coming soon)\u001b[36;2m");
        return 0;

    # If no command was found (no value has been returned yet), print this error and return 1.

    console.error("Error: Command not found:",command);
    return 1;

# Main

def Main() -> None:
    while(1):
        i = input(clrs.rgbcolor(159, 60, 230, Vars.directory) + clrs.rgbcolor(106, 224, 52, " ~ ") + clrs.rgbcolor(224, 146, 29,"",""));
        print("\u001b[36;2m", end="");
        try:
            cmd(i);
        except Exception as err:
            console.error("Error:", err);
Main();
