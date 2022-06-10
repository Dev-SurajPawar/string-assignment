'''
Write a program which accepts sentences from the userand prints a number of words from that sentence.
Input: In my company
Output: 3
'''

Str=input('Enter Sentence : ')
count=1
for i in Str :
    if i!=' ' :
        continue
    else :
        count+=1
        
print('No of Words is : ',count)

