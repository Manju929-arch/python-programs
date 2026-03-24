s = input("Enter the string")
i=0
str = ""
while  i<len(s):
     data = s[i]
     if data == " ":
         i= i+1
     else:
         str= str+data
         i=i+1
print(str)
