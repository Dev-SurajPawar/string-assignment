'''
Write a program which toggles the case of a string.
Input: DevIce DriVer
Output: dEViCE dRIvER
'''

str1=input("Enter string: ")
str2=""
i=0

while(i<len(str1)):

    if(ord(str1[i])>=97 and (ord(str1[i])<=122)):
        x=(ord(str1[i])-32)
        str2=str2+chr(x)

    elif(ord(str1[i])>=65 and (ord(str1[i])<=97)):
        x=(ord(str1[i])+32)
        str2=str2+chr(x)
    i+=1    
     
         
print(str2)
