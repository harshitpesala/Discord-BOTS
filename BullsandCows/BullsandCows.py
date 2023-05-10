import random

randomnum=[]
chances=0


def MakeNumber():
	for i in range(4):
		x=random.randrange(0,9)
		randomnum.append(x)
	if len(randomnum) > len(set(randomnum)):
		randomnum.clear()
		MakeNumber()

def PlayGame():
	global chances
	chances += 1
	cows = 0
	bulls = 0
	#print(randomnum)
	choice = input("Enter a 4 digit number please: ")
	guess = []
	for i in range(4):
		guess.append(int(choice[i]))
	for i in range(4):
		for j in range(4):
			if(guess[i] == randomnum[j]):
				cows += 1
	for x in range(4):
		if guess[x] == randomnum[x]:
			bulls += 1
	print("Bulls:", bulls)
	print("Cows:", cows-bulls)
	if(bulls == 4):
		print("Congrutalations, you won after", chances, "attempts!")
		play_again = input("Do u want to play again?(Y/N)")
		if(str(play_again) == "Y"):
			MakeNumber()
			chances=0
			PlayGame()
		elif(str(play_again) == "N"):
			print("Thank you for playing! See you next time")
		else:
			print("That isnt a valid answer. Please type (Y/N)")	


	if(bulls != 4):
		PlayGame()

MakeNumber()

PlayGame()
