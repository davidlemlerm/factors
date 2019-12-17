import math
from os import system, name
def clearterminal():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
clearterminal()
print("Please enter the number you want to find the factors of:")
number = float(input())
clearterminal()
print("The factors of {} are:".format(int(number)))
for x in range(1,int(number)+1):
	division = number % x
	if division == 0:
		print(x)