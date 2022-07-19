import dec;

from valid_ltrs import validLetters;

def encrypt(text: str, key: int) -> str:
    # Error checking
    key = int(key);
    # Encrypted text variable
    encryptedText = "";
    # Loop
    for i,v in enumerate(text):
        c = validLetters.find(v);
        if(c != -1):
            encryptedText += dec.fromDec(key * (c + 1), 36) + "$";
            continue;
        # If character is not found in validLetters raise error (If you get this error, consider referring to valid_ltrs.py file).
        raise Exception(f"Cannot encrypt character:{v}\nYou may want to consider running the command: add -tx {v}");
    return encryptedText;
