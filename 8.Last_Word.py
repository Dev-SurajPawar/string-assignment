'''
Write a program which accepts sentences from the user
and prints the last word from that sentence.
Input: In my company
Output: company
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
print(split[x-1])
