#dipparmar(DD)calculater
def sum(x,y):
	"""Function To Return Addition Of Two Numbers

	Args:
		x (int): First Number
		y (int): Second Number

	Returns:
		int: Addition Of First And Second Number
	"""		
	return x+y

#dipparmar(DD)calculater
def sub(x,y):
	"""Function To Return Subtraction Of Two Numbers

	Args:
		x (int): First Number
		y (int): Second Number

	Returns:
		int: Subtraction Of First And Second Number
	"""	
	return x-y

#dipparmar(DD)calculater
def  div(x,y):
	"""Function To Return Division Of Two Numbers

	Args:
		x (int): First Number
		y (int): Second Number

	Returns:
		int: Division Of First And Second Number
	"""	
	return x/y

#dipparmar(DD)calculater
def mul(x,y):
	"""Function To Return Multiplication Of Two Numbers

	Args:
		x (int): First Number
		y (int): Second Number

	Returns:
		int: Multiplication Of First And Second Number
	"""	
	return x*y

#dipparmar(DD)calculater
print("welcome to dip parmar calculater.")
def calculater():
	"""TO Print and input Calculator representation
	"""	
	enter=1
	sign="dip"
	while(enter!=0):
		a=int(input("enter first number:"))
		b=0
		while(b!=1):
			if(sign!="bc"):
				sign=input("enter your sign:")
				b=int(input("enter second number:"))
			if(sign=="+"):
				c=sum(a,b)
				print(c)
				a=c
				if(b==0):
					b=1
			elif(sign=="-"):
				c=sub(a,b)
				print(c)
				a=c
				if(b==0):
					b=1
			elif(sign=="x" or sign=="*" or sign=="X"):
				c=mul(a,b)
				print(c)
				a=c
			elif(sign=="/"):
				c=div(a,b)
				print(c)
				a=c
			elif(sign=="ac" or sign=="AC" or sign=="Ac" or sign=="aC"):
				b=1
			else:
				print("‼️‼️‼️‼️invalid input.‼️‼️‼️‼️")
				print("your choise:exit,contine⏺️,restart⏹️")
				choise=input("enter your choise:")
				if(choise=="exit"):
					return
				elif(choise=="restart"):
					b=1
				elif(choise=="contine"):
					b=0
				else:
					sign="bc"
calculater()

print("thanks for use dip parmar (D D) calculater.")
#dipparmar(DD)calculater