# Python cmd main.py
# Main file

# CONSTANTS

IMPORT_ERROR_MSG = 'Error: There was an error importing certain files, this means that certain features will not work properly.\nErrorMessage:';

# COLORED TEXT FORMATTER:

class clrs:
    def rgbcolor(r: int, g: int, b: int, txt: str, end: str = "\u001B[0m"):
        r, g, b = str(r), str(g), str(b);
        return f'\u001b[38;2;{r};{g};{b}m{txt}{end}';

# Colors dictionary

COLORS = {
    "red": [255, 0, 0],
    "purple": [159, 60, 230],
    "dark-green": [106, 224, 52],
    "orange": [224, 146, 29],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "cyan": [0, 255, 255],
    "yellow": [255, 255, 0],
    "gray": [100, 100, 100],
    "white": [200, 200, 200],
    "bright-white": [255, 255, 255]
};

# Default color class

class def_colors:
    dir = COLORS["purple"];
    cmd_seperator = COLORS["dark-green"];
    cmd = COLORS["orange"];

# ERROR CATCHING
# IMPORT ALL MODULES/LIBS

try:
    import os, texteditor, dec, find, runpy, pyplus, math, subprocess, music;
    from gcwd_ import getcwd;
    from py_console import console;
    from shutil import rmtree;
    import mathfunctions as mathf;
except ImportError as err:
    import os, math;

    os.system("");

    print(clrs.rgbcolor(200,0,0,"",""),end='');
    try:
        from py_console import console; # For console.error and console.success
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        from shutil import rmtree; # For rmtree
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import texteditor; # For txt command
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import dec; # For base conversion
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import find; # For find at occurence
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        from gcwd_ import getcwd; # For getcwd
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import runpy;
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import pyplus;
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import subprocess;
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import music;
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);
    try:
        import mathfunctions as mathf;
    except ImportError as e:
        print(IMPORT_ERROR_MSG,e);

# Startup

DEF_DIRECTORY = os.getenv("USERPROFILE") if os.getenv("USERPROFILE") != None else "/home/";

os.system("");
os.chdir(DEF_DIRECTORY);

# Start functions

def range_from_directory(path: str, size_min: int, size_max: int, delete: bool = False) -> None:
    """
    Prints the name of the file/directory in parent path if delete is false and it is within size_min and size_max.

    Otherwise deletes the file if it is within size_min and size_max.

        Parameters:
            path (string): The path of the directory.
            size_min (int): The minimum required size (in bytes) to delete/print.
            size_max (int): The maximum required size (in bytes) to delete/print.
            delete (bool) = False: If defined as true then deletes file/folders within size of size_min and size_max.
    """
    if(os.path.isfile(path)): console.error(f"Error: {path} is a file, not a directory."); return;
    for x, v in enumerate(os.listdir(path)):
        true_path = path + "/" + v;
        if(os.path.isfile(true_path)):
            size = os.path.getsize(true_path);
            if(size >= size_min and size <= size_max and delete == False):
                print(str(size), "bytes:\t", true_path);
            if(size >= size_min and size <= size_max and delete == True):
                os.remove(true_path);
                print("Removed file:\t", true_path);
            continue;
        range_from_directory(true_path, size_min, size_max, delete);

def size_from_directory(path: str, _size: int, delete: bool = False) -> None:
    """
    Prints the name of the file/directory in parent path if delete is false and it's size is _size.

    Otherwise deletes the file if it's size is _size.

        Parameters:
            path (string): The path of the directory.
            _size (int): The required size (in bytes) to delete/print.
            delete (bool) = False: If defined as true then deletes file/folders that are _size bytes.
    """
    if(os.path.isfile(path)): console.error(f"Error: {path} is a file, not a directory."); return;
    for x, v in enumerate(os.listdir(path)):
        true_path = path + "/" + v;
        if(os.path.isfile(true_path)):
            size = os.path.getsize(true_path);
            if(size == _size and delete == False):
                print(str(_size), "bytes:\t", true_path);
            if(size == _size and delete == True):
                os.remove(true_path);
                print("Removed file:\t", true_path);
            continue;
        size_from_directory(true_path, _size, delete);

def convert_bytes(bytes: int) -> str:
    try:
        bytes = int(bytes);
    except ValueError:
        console.error("Bytes cannot be converted to an integer properly...");
        return "ERROR";
    if(bytes == 0): return "0 byte(s)\t\t";
    bytes_name: tuple = ("byte(s)\t\t","kilobyte(s)\t","megabyte(s)\t","gigabyte(s)\t","terabyte(s)\t","petabyte(s)\t","exabyte(s)\t","zettabyte(s)\t","yottabyte(s)\t");
    i = int(math.floor(math.log(bytes, 1000)));
    p = math.pow(1000, i);
    converted_bytes = round(bytes / p, 2);
    if(len(str(converted_bytes)) < 4):
        return str(converted_bytes) + bytes_name[i] + "\t";
    return str(converted_bytes) + " " + bytes_name[i];

def get_directory_size(path: str) -> int:
    if(os.path.isfile(path)): console.error("Error:", path, "is a file, not a directory."); return 0;
    size = 0;
    try:
        for x,v in enumerate(os.listdir(path)):
            true_path = path + "/" + v;
            if(os.path.isfile(true_path)):
                try:
                    size += os.path.getsize(true_path);
                except Exception as err:
                    console.error("Error:",err);
                    # RESET COLOR
                    print("\u001b[36;2m", end="");
                continue;
            size += get_directory_size(true_path);
    except Exception as err:
        console.error("Error:", err);
        # RESET COLOR
        print("\u001b[36;2m", end="");
    return size;

def update_directory() -> str:
    try:
        with open(getcwd() + "/vars/dir", "r", encoding = "utf-8") as dir:
            return dir.read();
    except Exception as err:
        console.error("Error:", err);
        return "ERROR";

def update_path() -> dict:
    try:
        path_vars = {};
        for i,v in enumerate(os.listdir(getcwd() + "/vars/path/")):
            with open(getcwd() + "/vars/path/" + v, "r", encoding = "utf-8") as path:
                path_vars[v] = path.read();
    except Exception as err:
        console.error("Error:", err);
    return path_vars;

def open_py_editor(path_to_file: str):
    try:
        if(not os.path.exists(path_to_file)): console.error("Error: Path doesn't exist."); return 1;
        if(not os.path.exists(Vars.path["idle"])): console.error("Error: IDLE Path doesn't exist."); return 1;
        if(not os.path.isfile(path_to_file)): console.error("Error: Path must be a file."); return 1;
        subprocess.call("py",[Vars.path["idle"], path_to_file]);
        return 0;
    except Exception as err:
        console.error("Error:", err);
        return 1;

def extension(__p: str) -> str:
    """Returns the extension of a file/string."""
    return __p[find.find(__p, ".", __p.count(".") - 1) : len(__p)] if __p.find(".") != -1 else "N/A";

def cmd_args(__cmd: str) -> list:
    """Splits string into a list where and appends list at every space occurence outside of quotation marks."""
    arr = [];
    args = "";
    previous_space = True;
    quotes = False;

    for _ind in range(len(__cmd)):
        if(__cmd[_ind] != " " or quotes == True):
            # If command char at index of _ind is a quotation mark, then reverse (bool)quotes and skip loop.
            if(__cmd[_ind] in ('"',"'")):
                quotes = not quotes;
                continue;
            # Else add command char at index of _ind to args and skip loop. Change previous_space to false.
            args += __cmd[_ind];
            previous_space = False;
            continue;
        # If previous_space and quotes are both false, then append list arr (argument array), and reset the value of args, set previous_space to true.
        if(previous_space == False and quotes == False):
            arr.append(args);
            args = "";
            previous_space = True;
            continue;
        # True if the command is a space, not in quotes, or if (bool)previous_space/quotes is true.
        previous_space = True;
    # In case leftover args not appended.
    if(args != ""):
        arr.append(args);
    # Return argument array.
    return arr;

def arglen(__cmd) -> int:
    """Returns length of a list or string args."""
    return (len(__cmd), len(cmd_args(__cmd))) [type(__cmd) == str];

def argsplit(__cmd, _n: int, __n: int, sep = " ") -> str:
    """Split arg array - works like string splitting but with an array/list."""
    if(__n < _n):
        console.error("Error splitting arguments: Second value is smaller.");
        return "Error";

    if(__n > len(__cmd)-1):
        __n = len(__cmd)-1;

    ind = _n;
    end = __cmd[ind];

    for i in range(__n - _n):
        ind += 1;
        end += sep + __cmd[ind];

    return end;

def tuple_to_lower(tp: tuple) -> tuple:
	"""Returns tuple in all lowercase letters."""
	__tuple = list(tp);
	for i,val in enumerate(__tuple):
		__tuple[i] = val.lower();
	return tuple(__tuple);

def if_command(ARGS: list, * command: str, convert_to_lower: bool = True) -> bool:
	"""Check if ARGS command is inputted command."""
	if(convert_to_lower): command = tuple_to_lower(command);
	if(arglen(ARGS) < 1): return False;
	return ARGS[0].lower() in command;

def pycmd_interpret(file: str) -> None:
    """Interpret from file with cmd method."""
    file_lines = open(file, "r").readlines();
    py_start = False;
    for i,v in enumerate(file_lines):
        if(v.strip() == ""):
            continue;
        
        val = v.strip().replace("{dir}", Vars.directory).replace("{usr}", DEF_DIRECTORY.replace("\\", "/")).replace("{cwd}", getcwd().replace("\\", "/"));
        
        if(val[0:10] == "@startfile"):
            _f = cmd_args(val)[1];
            if(os.path.isfile(_f)):
                os.startfile(_f);
                continue;
            elif(os.path.isfile(add_dir(_f))):
                os.startfile(add_dir(_f));
                continue;
            continue;

        if(val == "@py"):
            py_start = not py_start;
            continue;
        
        if(py_start):
            # FIX: Interpret into python code.
            print(val);
        else:
            worked = cmd(val);
            
            if(worked == 1):
                console.error(f"Error at line {i + 1} in file:\n{file}");
        

# Start variables

class Vars:
    """All public variables."""
    directory = update_directory();
    path = update_path();

# add_directory to string:

def add_dir(path: str) -> str:
    return Vars.directory + "/" + path;

# Commands

def cmd(command: str):
    """Runs through pycmd commands.

        Parameters:
            command (string): The command you wish to run.
        Returns:
            0 for success and 1 for error.    
    """

    # Const command

    ARGS = cmd_args(command);

    # Check if args has at least one argument

    if(not ARGS or not command): console.error("Error: Expected at least 1 argument, got 0."); return 1;
    
    if(if_command(ARGS, "echo")):
        print(command[command.find(ARGS[0]) + 5:].strip().replace("\\n", "\n").replace("\\t","\t"));
        return 0;
    
    if("&&" in ARGS):
        prev = 0;
        for i in range(ARGS.count("&&") + 1):
            new = command.find("&&", prev) if command.find("&&", prev) != -1 else len(command);
            cmd(command[prev:new].strip("&").strip());
            prev = new + 1;
        return 0;
    
    # Run executable file

    if(ARGS[0][0:2] == "./"):
        path = ARGS[0][2:];
        path += ".exe" if not extension(path).lower() in ("exe", "run", "appimage", "sh", "bat") else "";
        if(os.path.isfile(path)):
            os.startfile(path);
        elif(os.path.isfile(add_dir(path))):
            os.startfile(add_dir(path));
        else:
            console.error("Error: Not a valid file.", path);
            return 1;
        return 0;

    # Run pycmd files

    if(if_command(ARGS, "pycmd", "pcmd")):
        # Guard
        if(arglen(ARGS) != 2): console.error(f"Error: Expected 2 args, got {arglen(ARGS)}."); return 1;
        # File name variable
        file = ARGS[1].replace("\\", "/").strip("/");
        file += ".pcmd" if extension(file) != "pcmd" else "";
        file_cmd = getcwd() + "\\pcmd\\" + file;
        if(os.path.isfile(file_cmd)):
            pycmd_interpret(file_cmd);
            return 0;
        if(os.path.isfile(file)):
            pycmd_interpret(file);
            return 0;
        file = add_dir(file);
        if(os.path.isfile(file)):
            pycmd_interpret(file);
            return 0;
        console.error("Error: File does not exist - " + file);
        return 1;

    # Add to valid letters and other stuff

    if(if_command(ARGS, "add")):
        # Guard
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
        console.error("Error: Operator is not valid - " + operator);
        return 1;

    # Color command

    if(if_command(ARGS, "color", "colour")):
        # Guard
        if(arglen(ARGS) < 2): console.error(f"Error: Expected at least 2 args, got {arglen(ARGS)}."); return 1;

        operator = ARGS[1];

        if(operator in ("-r", "-reset", "reset")):
            def_colors.cmd = COLORS["orange"];
            def_colors.cmd_seperator = COLORS["dark-green"];
            def_colors.dir = COLORS["purple"];
            return 0;

        # Guard
        if(arglen(ARGS) != 3): console.error(f"Error: Expected 3 args, got {arglen(ARGS)}."); return 1;
        if(not ARGS[2].lower() in COLORS): console.error("Color does not exist: " + ARGS[2] + "\nSee -colors for more info."); return 1;
        
        if(operator in ("-c", "-cmd")):
            def_colors.cmd = COLORS[ARGS[2].lower()];
            return 0;
        if(operator in ("-s", "-sep")):
            def_colors.cmd_seperator = COLORS[ARGS[2].lower()];
            return 0;
        if(operator in ("-d", "-dir")):
            def_colors.dir = COLORS[ARGS[2].lower()];
            return 0;
        if(operator in ("-a", "-all")):
            def_colors.dir = COLORS[ARGS[2].lower()];
            def_colors.cmd_seperator = COLORS[ARGS[2].lower()];
            def_colors.cmd = COLORS[ARGS[2].lower()];
            return 0;
        console.error("Syntax error: See -colors for more info.");
        return 1;
    
    # Colors help

    if(if_command(ARGS, "-colors", "-colours")):
        print("\nSyntax: color -operator color\n\nList of operators:\n-r, -reset, reset: Resets to default color values.\n-a, -all: Changes color of everything.\n-c, -cmd: Changes command color.\n-s, -sep: Changes seperator (~) color.\n-d, -dir: Changes current directory color.\n\nList of colors:\nBlue, bright-white, cyan, dark-green, gray, green, orange, purple, red, white and yellow.\n");
        return 0;

    # Math commands

    if(if_command(ARGS, "lcm")):
        if(arglen(ARGS) != 3): console.error(f"Error: Expected 3 args, got {arglen(ARGS)}."); return 1;
        first_digit = int(ARGS[1]);
        second_digit = int(ARGS[2]);
        print("Lowest common multiple:", str(mathf.lcm(first_digit, second_digit)));
        return 0;

    # Play music command

    if(if_command(ARGS, "play")):
        if(arglen(ARGS) < 2): console.error(f"Error: Expected at least 2 args, got {arglen(ARGS)}."); return 1;
        operator = ARGS[1];
        if(operator == "-l"):
            if(arglen(ARGS) < 3): console.error(f"Error: Expected at least 3 args, got {arglen(ARGS)}."); return 1;
            playlist = ARGS[2];
            if(os.path.exists(playlist)):
                if(os.path.isdir(playlist)):
                    for i,v in enumerate(os.listdir(playlist)):
                        if(extension(v) != "mp3"): continue;
                        print("Now playing:", v);
                        music.play(playlist + "/" + v);
                    return 0;
                console.error("Error: Path must be a directory.");
                return 1;
            true_dir = add_dir(playlist);
            if(os.path.exists(true_dir)):
                if(os.path.isdir(true_dir)):
                    for i,v in enumerate(os.listdir(true_dir)):
                        if(extension(v) != "mp3"): continue;
                        print("Now playing:", v);
                        music.play(true_dir + "/" + v);
                    return 0;
                console.error("Error: Path must be a directory.");
                return 1;
            console.error("Error: Path does not exist.");
            return 1;
        return 0;

    # Find command
    
    if(if_command(ARGS, "find")):
        if(arglen(ARGS) < 3): console.error(f"Error: Expected at least 3 args, got {arglen(ARGS)}."); return 1;
        if("-s" in ARGS):
            file_size = int(ARGS[ARGS.index("-s") + 1]);
            for x,v in enumerate(os.listdir(Vars.directory)):
                true_path = add_dir(v);
                if(os.path.isfile(true_path)):
                    if(os.path.getsize(true_path) == file_size):
                        print(str(file_size), "bytes:\t", true_path);
                    continue;
                size_from_directory(true_path, file_size);
        max_size, min_size = 9999999999999999, 0;
        if("-m" in ARGS):
            min_size = int(ARGS[ARGS.index("-m") + 1]);
        if("+m" in ARGS):
            max_size = int(ARGS[ARGS.index("+m") + 1]);
        if("+m" in ARGS or "-m" in ARGS):
            for x, v in enumerate(os.listdir(Vars.directory)):
                true_path = add_dir(v);
                if(os.path.isfile(true_path)):
                    if(os.path.getsize(true_path) >= min_size and os.path.getsize(true_path) <= max_size):
                        print(str(os.path.getsize(true_path)), "bytes:\t", true_path);
                    continue;
                range_from_directory(true_path, min_size, max_size, False);
        return 0;

    # Shutdown command

    if(if_command(ARGS, "shutdown")):
        operator = ARGS[1];
        # Shutdown
        if(operator == "-s"): os.system("shutdown /f");
        # Restart
        if(operator == "-r"): os.system("shutdown /r");
        # Log off
        if(operator == "-l"): os.system("shutdown /l");
        return 0;

    # Run from path

    if(if_command(ARGS, "runp")):
        path_var = ARGS[1];
        if(not os.path.exists(getcwd() + "/vars/path/" + path_var)): console.error("Error: Path variable does not exist."); return 1;
        path = Vars.path[path_var];
        if(not os.path.exists(path)): console.error("Error: Path variable is invalid.", path); return 1;
        os.startfile(path);
        return 0;
    
    # Path editor

    if(if_command(ARGS, "path")):
        if(arglen(ARGS) < 3): console.error(f"Error: Expected 3 args, got {arglen(ARGS)}."); return 1;
        operator = ARGS[1];
        path_var = ARGS[2];
        if(operator == "-c"):
            with open(getcwd() + "/vars/path/" + path_var, "x", encoding = "utf-8") as createPath:
                file = input("Set path to (" + Vars.directory + ") >> ");
                full_file = add_dir(file);
                if(not os.path.exists(full_file)): console.error("Error: Path does not exist - " + full_file); return 1;
                if(not os.path.isfile(full_file)): console.error("Error: Path must be a file."); return 1;
                createPath.write(full_file);
            return 0;
        if(not os.path.exists(getcwd() + "/vars/path/" + path_var)): console.error("Error: Path does not exist - " + path_var); return 1;
        if(operator == "-e"):
            file = input("Replace with (" + Vars.directory + ") >> ");
            full_file = add_dir(file);
            if(not os.path.exists(full_file)): console.error("Error: Path does not exist ('" + full_file + "')"); return 1;
            if(not os.path.isfile(full_file)): console.error("Error: Path must be a file."); return 1;
            with open(getcwd() + "/vars/path/" + path_var, "w", encoding = "utf-8") as write_path:
                write_path.write(full_file);
            Vars.path = update_path();
            return 0;
        if(operator == "-r"):
            with open(getcwd() + "/vars/path/" + path_var, "r", encoding = "utf-8") as read_path:
                print(path_var + ":", read_path.read());
            return 0;

    # Change parent directory

    if(if_command(ARGS, "rd")):
        if(Vars.directory.count("/") == 0): console.error("Error: Cannot have a null path."); return 1;
        Vars.directory = Vars.directory[0:find.find(Vars.directory, "/", Vars.directory.count("/")-1)-1];
        with open(getcwd() + "/vars/dir", "w", encoding = "utf-8") as d:
            d.write(Vars.directory);
        Vars.directory = update_directory();
        return 0;
    
    # Dir command

    if(if_command(ARGS, "dir")):
        if(arglen(ARGS) == 1):
            print("\nDirectory", Vars.directory + ":\n");
            dirs = files = 0;
            for x,v in enumerate(os.listdir(Vars.directory + "\\")):
                true_path = add_dir(v);
                if(os.path.isfile(true_path)):
                    try:
                        print(convert_bytes(os.path.getsize(true_path)) + "\t<File>\t" + v);
                    except Exception as err:
                        print("Error\t\t<File>\t" + v);
                        console.error("Error:", err);
                        # RESET COLOR
                        print("\u001b[36;2m", end="");
                    files += 1;
                    continue;
                try:
                    print(convert_bytes(get_directory_size(true_path)) + "\t<Dir>\t" + v);
                except Exception as err:
                        print("Error\t\t<Dir>\t" + v);
                        console.error("Error:", err);
                        # RESET COLOR
                        print("\u001b[36;2m", end="");
                dirs += 1;
            print("\n\t" + convert_bytes(get_directory_size(Vars.directory)) + "\n\t" + str(files) + " file(s)\n\t" + str(dirs) + " dir(s)\n");
            return 0;

    # Python run command

    if(if_command(ARGS, "py", "python")):
        if(arglen(ARGS) < 3): console.error(f"Error: Expected at least 3 arguments, got {arglen(ARGS)}."); return 1;
        function = ARGS[1];
        if(function == "-r"):
            p = ARGS[2];
            path = add_dir(p);
            path += ".py" if extension(path) != "py" else "";
            if(not os.path.exists(path)): console.error("Error: Path does not exist - " + path); return 1;
            re = open(path, "r");
            contents = re.read();
            re.close();
            open(path, "w").close();
            wr = open(path, "w");
            wr.write(f'import msvcrt as BAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm;\n{contents}\nprint("This process has finished, press any key to exit...");\nBAYUDWebdoyowdbadshAWEIDUWjdiaowpdwdadjwhedwhdqjdidm.getch();');
            wr.close();
            try:
                subprocess.call(['py', path]);
                open(path, "w").close();
                wrd = open(path, "w");
                wrd.write(contents);
                wrd.close();
            except Exception as err:
                console.error(f"Error in {path}:", err);
                open(path, "w").close();
                wrd = open(path, "w");
                wrd.write(contents);
                wrd.close();
                return 1;
            return 0;
        if(function == "-c"):
            filename = ARGS[2];
            path = add_dir(filename);
            if(not os.path.exists(path)): console.error("Error: File does not exist."); return 1;
            code = open(path, "r").readlines();
            pyplus.compile(code);
            return 0;
        console.error("Error: See -py for syntax");
        return 1;

    # Make folder command

    if(if_command(ARGS, "mkdir")):
        if(arglen(ARGS) != 2): console.error(f"Error: Expected 2 arguments, got {arglen(ARGS)}."); return 1;
        directory_name = ARGS[1];
        full_dir = add_dir(directory_name);
        if(os.path.exists(full_dir)): console.error(f"Error: Path already exists: {full_dir}"); return 1;
        os.mkdir(full_dir);
        if(os.path.exists(full_dir)): console.success("Sucessfully created directory:",full_dir); return 0;
        console.error("Error: Something went wrong creating directory,",full_dir);
        return 1;

    # Delete folder command

    if(if_command(ARGS, "rmdir")):
        if(arglen(ARGS) != 2): console.error(f"Error: Expected 2 arguments, got {arglen(ARGS)}."); return 1;
        directory_name = ARGS[1];
        all_slashes = True;
        for ind,chr in enumerate(directory_name):
            if(chr != "\\" and chr != "/"):
                all_slashes = False;
                break;
        if(all_slashes): console.error("Error: You must enter a valid path."); return 1;
        full_dir = add_dir(directory_name);
        if(not os.path.exists(full_dir)): console.error(f"Error: Path does not exist: {full_dir}"); return 1;
        try:
            os.rmdir(full_dir);
        except OSError:
            console.error("Error removing file, this may be because it is not empty.");
            y_n_input = "";
            while(y_n_input != "y" and y_n_input != "n"):
                y_n_input = input("Do you still wish to delete this directory [Y/N]: ").lower();
            if(y_n_input == "y"):
                rmtree(full_dir);
                return 0;
            return 1;
        if(not os.path.exists(full_dir)): console.success("Sucessfully deleted directory:", full_dir); return 0;
        console.error("Error: Something went wrong deleting directory,", full_dir);
        return 1;

    # Exit/close command

    if(if_command(ARGS, "close", "exit")):
        quit();
    
    # Restart/reload command

    if(if_command(ARGS, "restart", "reload")):
        runpy.run_path(getcwd() + "/main.py");
        return 0;

    # cls/clear command
    
    if(if_command(ARGS, "cls", "clear")):
        print("Clearing...");
        os.system("cls||clear");
        return 0;
    
    # Text editor command
    
    if(if_command(ARGS, "txt")):
        texteditor.Write(ARGS[1]);
        return 0;

    # Change directory
    
    if(if_command(ARGS, "cd")):
        # Checking if there are correct amount of args

        if(arglen(ARGS) != 2): print("Error: Expected 2 args, got " + str(arglen(ARGS))); return 1;
        
        # Path variable
        
        _path = ARGS[1].strip().strip("\\").replace("\\", "/").strip("/");
        path = "";

        if(_path[0] == "~"):
            _path = DEF_DIRECTORY.replace("\\", "/") + _path[1:];
        elif(_path == "~"):
            _path = DEF_DIRECTORY.replace("\\", "/");

        # Formatting path

        prevSlash = False;
        for i, v in enumerate(_path):
            if(v == "/"):
                if(prevSlash == True): continue;
                path += v;
                prevSlash = True;
                continue;
            path += v;
            prevSlash = False;
        
        #if(path[0:1] == "~/")

        if(path == "." * len(path) and len(path) > 2): path = "..";
        if(path == ".."): cmd("rd"); return 0;
        if(path == "."): cmd("cd ~ && rd"); return 0;
        
        # Check if path exists and if it does, update the directory.

        if(os.path.exists(path)):
            with open(getcwd() + "/vars/dir", "w", encoding = "utf-8") as d:
                d.write(path);
            Vars.directory = update_directory();
            return 0;
        if(os.path.exists(add_dir(path))):
            with open(getcwd() + "/vars/dir","w", encoding = "utf-8") as d:
                d.write(add_dir(path));
            Vars.directory = update_directory();
            return 0;
        
        # If it doesn't exist, print this error.

        console.error(f"Error: Path does not exist: {path}");
        return 1;

    # Convert from base 2-36 command.

    if(if_command(ARGS, "base")):
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

            to, _from = int(to), int(_from);

        # Error catching.

        except Exception as err:
            console.error("Error:", err, "\nThis may be due to a syntax error, type '-base' for info.");
            return 1;

        # Convert to the stated base digit.

        try:
            if(_from != 10): value = dec.toDec(value, _from);
            print(dec.fromDec(int(value),to));
        
        # Error catching.

        except Exception as err:
            console.error("Error:", err, "\nThis may be due to a syntax error, type '-base' for info.");
            return 1;
        
        # If no errors, return 0.

        return 0;

    # Convert base command help syntax.

    if(if_command(ARGS, "-base")):
        print("\u001b[90;2;mTry typing:\nbase from to value\nbase to value\nIf you do not include what base you are converting from, pycmd will assume it to be base10.\u001b[36;2m");
        return 0;

    # Python help syntax

    if(if_command(ARGS, "-py", "-python")):
        print("\u001b[90;2;mTry typing:\npy -r file_to_run\npy -c file_to_compile (coming soon)\u001b[36;2m");
        return 0;

    # File name variable
    file = ARGS[0].replace("\\","/").strip("/");
    file += ".pcmd" if extension(file) != "pcmd" else "";
    file_cmd = getcwd() + "\\pcmd\\" + file;
    if(os.path.isfile(file_cmd)):
        pycmd_interpret(file_cmd);
        return 0;
    if(os.path.isfile(file)):
        pycmd_interpret(file);
        return 0;
    file = add_dir(file);
    if(os.path.isfile(file)):
        pycmd_interpret(file);
        return 0;

    # If no command was found (no value has been returned yet), print this error and return 1.

    console.error("Error: Command not found - " + command);
    return 1;

# Main

def Main() -> None:
    """Main function for pycmd."""
    while(1):
        i = input(clrs.rgbcolor(def_colors.dir[0], def_colors.dir[1], def_colors.dir[2], Vars.directory) + clrs.rgbcolor(def_colors.cmd_seperator[0], def_colors.cmd_seperator[1], def_colors.cmd_seperator[2], " ~ ") + clrs.rgbcolor(def_colors.cmd[0], def_colors.cmd[1], def_colors.cmd[2], "", ""));
        print("\u001b[36;2m", end="");
        try:
            cmd(i);
        except Exception as err:
            console.error("Error:", err);
Main();
