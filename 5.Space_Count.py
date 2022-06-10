'''
Write a program which accepts sentences from the user
and print a number of white spaces from that sentence.
Input: In my company
Output: 2
'''

Str=input('Enter Sentence : ')
count=0
for i in Str:
    if i==' ' :
        count+=1

print('No of Spaces in Sentence is : ',count)
