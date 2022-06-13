import dec;

# List of all valid letters
validLetters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!≥≤£$%^&*()-+_=[]{}'#@~;:<>,./?|\`¬"+'"“’”'+"\n"+"\t"+"™ƒ€µ©®œŽŒ‰÷æ¼½•"+"ÿÛâàØüÌÓ·…¶Ïé‰¿ËöJ"+""+""+""+"Ü"+"§š¥›±ª¦çå‡þ";
# If you want more valid letters: use this command (it is safer).
# validLetters += text # Replace text for what you want to add (APPLY TO DECRYPT.PY SEPERATELY - DO NOT EDIT THE VALIDLETTERS DECLARATION)
def encrypt(text,key):
    encryptedText = "";
    for i,v in enumerate(text):
        c = validLetters.find(v);
        if(c != -1):
            encryptedText += dec.fromDec(key*(c+1),36)+"$";
            continue;
        # If character is not found in validLetters raise error (If you get this error, consider referring to line 5-6).
        raise Exception("Cannot encrypt character:",v);
    return encryptedText;
