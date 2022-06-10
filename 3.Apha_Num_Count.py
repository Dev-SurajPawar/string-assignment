'''
Write a program which accepts sentences from the user
and print a number of small letters, capital letters and digits from that
sentence.
Input: abcDE 5Glm1 O
Output: Small:5 Capital: 4 Digits: 2
'''

Str=input('Enter Sentence : ')

Small=0
Capital=0
Digit=0
Special_Char=0

for i in Str:

    if i>='A' and i<='Z' :
        Capital+=1
    elif i>='a' and i<='z' :
        Small+=1
    elif i>='0' and i<='9' :
        Digit+=1
    else :
        Special_Char+=1


print('Capital = ',Capital)
print('Small = ',Small)
print('Digit = ',Digit)
print('Special Character = ',Special_Char) 
