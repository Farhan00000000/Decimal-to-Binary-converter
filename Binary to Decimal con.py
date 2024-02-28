def float_bin(number, places = 3): 
    number_str = str(number)
    if '.' not in number_str:
        return bin(int(number)).lstrip("0b")
    else:
        whole, dec = number_str.split(".") 
        whole = int(whole) 
        dec = int(dec) 
        res = bin(whole).lstrip("0b") + "."
  
        for x in range(places): 
            whole, dec = str((decimal_converter(dec)) * 2).split(".") 
            dec = int(dec) 
            res += whole 
        return res 
  
def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 

# Test the function
print(float_bin(input("Enter your decimal number : "), 3))
