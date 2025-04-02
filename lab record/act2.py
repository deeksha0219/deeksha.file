def temp_convert():
    temp = float(input("Temp: "))
    f = input("From (C/F/K): ").upper()
    t = input("To (C/F/K): ").upper()
    if f == t: print("Same unit")
    elif f == 'C':
        print(temp, 'C is', (temp*9/5+32 if t=='F' else temp+273.15), t)
    elif f == 'F':
        print(temp, 'F is', ((temp-32)*5/9 if t=='C' else (temp-32)*5/9+273.15), t)
    else:
        print(temp, 'K is', (temp-273.15 if t=='C' else (temp-273.15)*9/5+32), t)
temp_convert()