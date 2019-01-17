#Cipher.py


#The key that is going to move the ascii forward or backward
key = 1;

# Gets the user input for encrypt or decrypt
print("Would you like to encrypt? (e) or decrypt? (d)");

mode = input();
# Loops until the user puts in a valid input
while mode not in ['e','d']:
	print("Would you like to encrypt? (e) or decrypt? (d)");
	mode = input();

#If the user wants to decrypt, the program will subtract if encrypt, add
if mode is 'd':
	key = -1;
elif mode is 'e':
	key = 1;

#Gets the message from the user
print("What is your message?  This program accepts all inputs");
message = input();

print("What is your key?");

#Gets the key value from user
keyInput = input();

#Tests if key value is a number
while type(keyInput) is not int:
	try:
		keyInput = int(keyInput);
	except:
		print("The keyInput is not a number");
		keyInput = input();
		pass;

#Updates the key variable
key = key * keyInput;


#Stores the ascii value of the string by character
asciiList = [];
#Stores whether or not the letter is capitalized, or if it is a special character
capitalList = [];

#Stores the ascii values of the message
#Updates the capital list, 0 is lower, 1 is upper, 2 is special
for i in range(len(message)):
	asciiValue = int(ord(message[i]));
	if asciiValue >= 97 and asciiValue <= 122:
		asciiList.append((asciiValue) + key - 97);
		capitalList.append(0);
	elif asciiValue >= 65 and asciiValue <= 90:
		asciiList.append((asciiValue + key - 65));
		capitalList.append(1);
	else:
		asciiList.append(asciiValue);
		capitalList.append(2);

#Makes sure that alphabets loop around
for i in range(len(asciiList)):
	if capitalList[i] in [0,1]:
		asciiList[i] = asciiList[i] % 26;

#Prints back out the encrypted message
for i in range(len(asciiList)):
	if capitalList[i] is 0:
		print((chr(asciiList[i] + 97)), end = "");
	elif capitalList[i] is 1:
		print((chr(asciiList[i] + 65)), end= "");
	else:
		print((chr(asciiList[i])), end ="");

#Makes sure the program doesn't immediately exit
input();
