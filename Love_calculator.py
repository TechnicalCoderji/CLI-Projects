#dipparmar 
print("welcome to dipparamr love calculater.")

#dipparmar
def cheak_love(name,search):
	"""Check FOR Character count in names

	Args:
		name (string): name of person
		search (string): Char for search

	Returns:
		int: number of chr apper in name
	"""	
	count = 0
	for i in name:
		if i == search:
			count += 1
	for i in range(count):
		name.remove(search)
	return count

#dipparmar
def love_num(list):
	sum = []
	love_sum = []
	lenth = len(list)
	if lenth%2 == 0:
		for i in range(int(lenth/2)):
			sum.append(str(list[i] + list[-(i+1)]))
		for i in sum:
			for j in i:
				love_sum.append(int(j))
	else:
		for i in range(int(lenth/2)):
			sum.append(str(list[i] + list[-(i+1)]))
		sum.append(str(list[int(lenth/2)+1]))
		for i in sum:
			for j in i:
				love_sum.append(int(j))
	return love_sum

#dipparmar
game_loop = True

#dipparmar
while game_loop:
	name = []
	num = []
	love_per = 0
	boy_name = input("enter first name:")
	if boy_name.lower() == "exit":
		break
	girl_name = input("enter second name:")
	if girl_name.lower() == "exit":
		break
	print(boy_name,"❤️🩷🧡💛💚💙",girl_name)
	if (boy_name.isalpha() and girl_name.isalpha()):
		for i in boy_name.lower():
			name.append(i)
		for i in girl_name.lower():
			name.append(i)
		reapet = 0
		while len(name) != 0:
			num.append(cheak_love(name,name[0]))
		
		while len(num) != 2:
			num = love_num(num)

		love_per = int(str(num[0])+str(num[1]))
		if (love_per >= 0) and (love_per <= 20):
			print("💘",str(num[0])+str(num[1]),"%","💘")
		elif (love_per > 20) and (love_per <= 40):
			print("💌💌",str(num[0])+str(num[1]),"%","💌💌")
		elif (love_per > 40) and (love_per <= 60):
			print("💖💖💖",str(num[0])+str(num[1]),"%","💖💖💖")
		elif (love_per > 60) and (love_per <= 80):
			print("💝💝💝💝",str(num[0])+str(num[1]),"%","💝💝💝💝")
		elif (love_per > 80) and (love_per <= 100):
			print("💗💗💗💗💗",str(num[0])+str(num[1]),"%","💗💗💗💗💗")
	else:
		print("invalid input.")
		print("!!!do not enter sign or number in name!!!")
#dipparmar
		

		
