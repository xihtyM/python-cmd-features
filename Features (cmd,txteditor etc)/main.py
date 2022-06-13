import os, texteditor, dec, find, gcwd_, runpy, colorama, clrs;
from py_console import console;

# Startup

os.system("");

# Start functions

def getcwd():
    return gcwd_.getcwd();

def updateDir():
    try:
        with open(getcwd()+"/vars/dir","r") as d:
            return d.read();
    except Exception as err:
        console.error("Error:",err);

# Start variables

class vars:
    directory = updateDir();

# Commands

def cmd(command):

    # Make folder command

    if(command[0:5] == "mkdir"):
        try:
            directoryName = command[command.find(" "):].lstrip();
            fullDir = vars.directory+"/"+directoryName;
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
            directoryName = command[command.find(" "):].lstrip();
            fullDir = vars.directory+"/"+directoryName;
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
        console.success("Sucessfully reloaded!");
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
                    d.write(path);
                vars.directory = updateDir();
                return 0;
            if(os.path.exists(vars.directory+"/"+path)):
                with open(getcwd()+"/vars/dir","w") as d:
                    d.write(vars.directory+"/"+path);
                vars.directory = updateDir();
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
        i = input(clrs.rgbcolor(159, 60, 230, vars.directory) + clrs.rgbcolor(106, 224, 52, " ~ ") + clrs.rgbcolor(224, 146, 29,"",""));
        print(colorama.Fore.CYAN, end="");
        cmd(i);
Main();
