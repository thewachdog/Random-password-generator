import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print('Welcome to Password generator!!')
nrletters = input('How many letters would you like in your password ? \n')
nrsymbols = input('How many symbols would you like ? \n')
nrnumbers = input('How many numbers would you like ? \n')

###########################################

passwd = str()
'''
for letter in range(int(nrletters)):
        passwd += letters[random.randint(0, len(letters)-1)]
for number in range(int(nrnumbers)):
        passwd += numbers[random.randint(0, len(numbers)-1)]
for symbol in range(int(nrsymbols)):
        passwd += symbols[random.randint(0, len(symbols)-1)]

print(passwd)
'''

totalletter = int(nrletters)
totalsymbol = int(nrsymbols)
totalnumber = int(nrnumbers)
lettercount = 0
numbercount = 0
symbolcount = 0
totalchar = totalletter + totalsymbol + totalnumber

while (len(passwd) < totalchar):
        a = random.randint(0,2)
        if a == 0:
                if lettercount < totalletter:
                        passwd += letters[random.randint(0, len(letters)-1)]
                        lettercount += 1

        if a == 1:
                if numbercount < totalnumber:
                        passwd += numbers[random.randint(0, len(numbers)-1)]
                        numbercount += 1

        if a == 2:
                if symbolcount < totalsymbol:
                        passwd += symbols[random.randint(0, len(symbols)-1)]
                        symbolcount += 1
print(passwd)

# We can also use random.shuffle() and for loop to run this program
