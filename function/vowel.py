s= input("Enter a string")
i=0
count =0
while i<len(s):
    if s[i] in "AEIOUaeiou":
        count = count+1
    i=i+1
print("No of vowels.", count)
