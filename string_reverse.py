'''
ask = "cat"   # whatever the user typed
num = ""      # empty string to start
num is your growing answer. It starts empty.

for i in ask:
This means: take the string ask one character at a time.

For "cat":

1st time → i is "c"
2nd time → i is "a"
3rd time → i is "t"
i is just a name for “the current character.” You could call it char if that feels clearer.

num = i + num
Read it as: new answer = current letter + old answer

You’re putting the new letter in front of what you already built.

Important detail: on the right side, Python uses the old num, then stores the result back into num.


'''


ask = (input("Enter the Number"))

num = ""


for i in ask:
    num = i + num
print(num) 
