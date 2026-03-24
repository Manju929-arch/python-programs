

s= input("Enter the string.")
i=0
newstr = ""
while i<= len(s)-1:
    data = s[i]
    ascii = ord(data)
    if ascii >=65 and ascii <= 90:
        newascii = ascii+32
        convchar= chr (newascii)
        newstr = newstr+convchar
    else:
        newstr = newstr+data
    i=i+1
print(newstr)