import gcwd_, os, encrypt, decrypt;

# Variables

class Vars:
    Dir = (gcwd_.getcwd()).replace("\\","/");
    makeDir = "";

# Functions

def updateFileDir():
    with open(Vars.Dir+"/vars/dir","r") as d:
        Vars.makeDir = d.read();
updateFileDir();

# Write to file

def Write(name):
    key = "";
    while(not key.isdigit()):
        key = input("Key >> ");
    key = int(key);
    file = Vars.makeDir+"/"+name+".ptxt";
    text = "";
    try:
        updateFileDir();
        if(os.path.exists(file)):
            with open(file,"r") as r:
                text = decrypt.decrypt(r.read(),key);
        # Reset colors and print previously typed text  
        print("\u001B[0m\n"+text);
        while(1):
            i = input();
            if(i == "/cmd"):
                i = input(">> ");
                if(i == "del"):
                    text = "";
                    w = open(file,"w");
                    w.write("");
                    w.close();
                    print("Deleted all text");
                    continue;
                if(i == "close"):
                    w = open(file,"w");
                    w.write(str(encrypt.encrypt(text[0:],key)));
                    w.close();
                    break;
                continue;
            text += i+"\n";
            w = open(file,"w");
            w.write(str(encrypt.encrypt(text,key)));
            w.close();
        return 0;
    except Exception as err:
        print("Error:",err,"\nYou may want to consider changing the key.");
        return 1;
