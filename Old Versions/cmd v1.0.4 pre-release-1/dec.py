# Decimal Operators file
# Includes conversion between base2 and base36

# from_decimal:
# max: base36, min: base2
def fromDec(num,base):
    base_num = "";
    while(num>0):
        dig = int(num%base);
        # If base is smaller than 10 then use numbers only
        if(dig<10):
            base_num += str(dig);
        # Else include letters and symbols etc
        else:
            base_num += chr(ord('A')+dig-10);
        num //= base;
    # Invert base_num
    base_num = base_num[::-1];
    return base_num;
    
# to_decimal:
# max: base36, min: base2
def toDec(val,base):
    # Error checking
    if(not isinstance(val,str)): val = str(val);
    if(base<1 or base>37): raise Exception("Base must be between 2 and 36");
    # Return decimal value based on the base
    return int(val,base);
