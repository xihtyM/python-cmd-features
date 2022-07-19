import dec, find;

from valid_ltrs import validLetters;

def decrypt(encryptedText: str, key: int) -> str:
    # Error checking
    key = int(key);
    # Variables
    previousVal = 0;
    decryptedText = "";
    # Decompress text and decrypt
    for i in range(encryptedText.count("$")):
        x = find.find(encryptedText,"$",i)-1;
        val = encryptedText[previousVal:x];
        index = int(dec.toDec(val,36)/key)-1;
        if(len(validLetters) < int(dec.toDec(val,36)/key)-1): raise OverflowError(f"Cannot find character with index {index}. You may want to use a different key.");
        decryptedText += validLetters[index];
        previousVal = x+1;
    # Finish
    return decryptedText;
