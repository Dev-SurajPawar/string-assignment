'''
Write a program which accepts sentences from user and
position from user and print the word at that position.
Input: is my he she
Position: 3
Output: he
'''

Str=input('Enter Sentence : ')

split=[]
temp=''

for i in Str+' ':
    
    if i==' ':
        split.append(temp)
        temp=''

    else:
        temp+=i

x=len(split)
num=int(input('Enter Position to print word: '))
print(split[x-(num-1)])
