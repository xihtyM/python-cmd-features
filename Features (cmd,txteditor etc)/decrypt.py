import dec, find;

# List of all valid letters
validLetters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!≥≤£$%^&*()-+_=[]{}'#@~;:<>,./?|\`¬"+'"“’”'+"\n"+"\t"+"™ƒ€µ©®œŽŒ‰÷æ¼½•"+"ÿÛâàØüÌÓ·…¶Ïé‰¿ËöJ"+""+""+""+"Ü"+"§š¥›±ª¦çå‡þ";
# If you want more valid letters: use this command (it is safer).
# validLetters += text # Replace text for what you want to add (APPLY TO ENCRYPT.PY SEPERATELY - DO NOT EDIT THE VALIDLETTERS DECLARATION)
def decrypt(encryptedText,key):
	previousVal = 0;
	decryptedText = "";
	# Decompress text and decrypt
	for i in range(encryptedText.count("$")):
		x = find.find(encryptedText,"$",i)-1;
		val = encryptedText[previousVal:x];
		decryptedText += validLetters[int(dec.toDec(val,36)/key)-1];
		previousVal = x+1;
	
	return decryptedText;
