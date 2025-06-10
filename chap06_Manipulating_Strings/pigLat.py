#! python3
#pigLat.py - converts text to pig Latin

import sys, pyperclip

#english to pip latin
print('Enter the enlgish message to translate into pig latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []

for word in message.split():
    
    #seperates the non-letters at the start of the word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    
    #seperate the non-letters at the end of the word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants = word[0]
        word = word[1:]
    
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin));


