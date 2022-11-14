'''
Write a program to check whether character entered by
user is vowel or consonant.

vowels=> a,e,i,o,u,A,E,I,O,U
consonants: Other than vowels are consonants.

'''

ch=input('enter character:')
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print('its vowels,')
else:
    print('its consonants.')
