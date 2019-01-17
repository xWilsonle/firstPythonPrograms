#count.py

myInput = [""] * 3;
resetInput = False;

#input(0) is name, input(1) is number, input(2) is increment
while type(myInput[1]) != int or type(myInput[2]) != int or '' in myInput:
	print("Please input your name, number, and increment seperated by a space");
	myInput = input().split(" ");

	#checks to see if second input is a number	
	
	try:
		myInput[1] = int(myInput[1]);
	except:
		print("Your number is invalid please try again");
		resetInput = True;
		pass;

	#checks to see if third input is an increment
	
	try:
		myInput[2] = int(myInput[2]);
	except:
		print("Your increment is invalid please try again");
		resetInput= True;
		pass;

	try:

		#Checks to see if the increment is higher than number

		if myInput[1] < myInput[2]:
			print("Your increment cannot be higher than your number please try again");
			resetInput = True;

		#Checks to see if the number or increment are negative

		if myInput[1] < 0:
			print("Your number cannot be negative please try again");
			resetInput = True;
		if myInput[2] < 0:
			print("Your increment cannot be negative please try again");
			resetInput = True;
		
		#Checks to see if the name only contains alphabetal letters

		if not myInput[0].isalpha():
			print("Your name must only contain letters");
			resetInput = True;
	except:
		pass;

#resets the input if it fails to meet the critera
	if resetInput is True:
		print("");
		myInput = [""] * 3;
		resetInput = False;

#Checks if number is even or odd, if even start counting at 0, if odd, start at 1

if myInput[1] % 2 == 1:
	startNum = 1;
else:
	startNum = 0;


#Prints Hello and the sequence
print("Hello " + myInput[0]);
print("Your Sequence is ", end = "");
for startNum in range(startNum, myInput[1], myInput[2]):
	print(str(startNum) + " ", end = "");
#If the input number's number is included in the sequence, it will print it
if myInput[1] % myInput[2] == 0:
	print(str(myInput[1]));