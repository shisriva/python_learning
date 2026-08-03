'''
Why we need the if around it
if word in ola:
    ola[word] = ola[word] + 1
This line only runs when the word is already a key. That matters because if word isn't in ola yet, ola[word] on the right side would crash — you can't read a value that was never stored. That's exactly why the else branch does something different:

else:
    ola[word] = 1
Here there's nothing to read, so we just write 1 directly — no + 1, no lookup on the right.

'''



def word_count(text):
    word_split = text.split()

    ola = {}
    counter = 0
    ncounter = 0

    for words in word_split:
        if words in ola:
            ola[words] = ola[words] + 1
        else:
            ola[words] = 1

    return ola
