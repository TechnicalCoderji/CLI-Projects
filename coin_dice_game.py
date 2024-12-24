import random

def coinrepeat(toss):
	"""For Printing COINS On Screen

	Args:
		toss ( int ): HEAD or TAIL
	"""	
	print("  #####")
	print(" #     #")
	print("#       #")
	print("#",toss,"#")
	print("#       #")
	print(" #     #")
	print("  #####")

def coin(num):
	"""For Manage How Many Coin Fliped

	Args:
		num (int): Number of Coin to Flip
	"""	
	head_count = 0
	tail_count = 0
	for _ in range(1,num+1):
		coin=["heads","tails"]
		toss=random.choice(coin)
		coinrepeat(toss)
		if toss == "heads":
			head_count += 1
		else:
			tail_count += 1

	print("TOTAL HEADS :",head_count)
	print("TOTAL TAILS :",tail_count)

def dicerepeat(toss):
	if(toss==1):
		print("##############")
		print("#            #")
		print("#            #")
		print("#     @      #")
		print("#            #")
		print("#            #")
		print("##############")
	elif(toss==2):
		print("##############")
		print("#            #")
		print("#   @        #")
		print("#            #")
		print("#        @   #")
		print("#            #")
		print("##############")
	elif(toss==3):
		print("##############")
		print("#            #")
		print("#    @       #")
		print("#      @     #")
		print("#        @   #")
		print("#            #")
		print("##############")
	elif(toss==4):
		print("##############")
		print("#            #")
		print("#   @    @   #")
		print("#            #")
		print("#   @    @   #")
		print("#            #")
		print("##############")
	elif(toss==5):
		print("##############")
		print("#            #")
		print("#   @    @   #")
		print("#     @      #")
		print("#   @    @   #")
		print("#            #")
		print("##############")
	else:
		print("##############")
		print("#            #")
		print("#   @    @   #")
		print("#   @    @   #")
		print("#   @    @   #")
		print("#            #")
		print("##############")

def dice(num):
	count = {1:0,2:0,3:0,4:0,5:0,6:0}
	dice=[1,2,3,4,5,6]
	for _ in range(1,num+1):
		toss=random.choice(dice)
		dicerepeat(toss)
		count[toss] += 1

	for i in dice:
		print(f"TOATAL {i} is: {count[i]}")

def game():
	print("welcome to dip parmar's dice and coin game.")
	print("rules:(1)exit game enter 'exit' in any place.")
	print("      (2)restart game enter 'restart' in any place.")
	print("      (3)enter any value in small later.")
	print("      (4)do not enter other input from[restart,exit,0-9]")
	choice=input("COIN GAME \nDICE GAME\nplease enter(coin or dice) \nwhich game you like to play:")
	if(choice=="exit"):
		return
	while(True):
		if(choice=="dice"):
			n=input("enter number of dices:")
			if(n=="exit"):
				return
			elif(n=="restart"):
				break
			dice(int(n))
		elif(choice=="coin"):
			n=input("enter number of coins:")
			if(n=="exit"):
				return
			elif(n=="restart"):
				break
			coin(int(n))
		else:
			print("invalid input enter again.")
			break
	game()

game()
print("thanks for playing dip parmar's games.")
print("|| have a nice day ||")