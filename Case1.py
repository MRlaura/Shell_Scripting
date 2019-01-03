decision='Y' #to get inside the while loop the first time
productA=1000 -(1000 * 0.75)
productB=500 - (500 * 0.50)
productC=250 - (250 *0.25)
productD=100
productE=50
# varibles needed for the loops and the final invoice
quantA=0
quantB=0
quantC=0
quantD=0
quantE=0
priceA=0
priceB=0
priceC=0
priceD=0
priceE=0
Fprice=0
	
while (decision =='Y'):
	try:
		# to know if the user wants to continue buying
		decision=input('Do you want to buy a new product? Write Y or N \n').upper()
				
		if decision=='Y':
			print ('You choose to buy')
			producto= input ('Available products: A, B, C, D, E. Write the corresponding letter\n').upper()
			quant=0 # the amount of products to buy, in case the users wants to continue buying more items of the same product
			if producto=='A':
				quant= int (input ('You have choose product A. How many items do you want?\n'))
				if quant>=0:
					Fprice=Fprice - priceA # in case previously the user had bought the same product, to not duplicate prices
					quantA=quant + quantA # in case previously the user had bought the same product
					print ('You have choose {} items'. format (quantA))
					priceA=quantA * productA
					print ('The original price is ${} .The reduced price is $ {}'.format ((1000 * quantA),priceA))
					Fprice=Fprice + priceA # for the final invoice
				else:
					print ('You have to write a positive number')
			elif producto=='B':
				quant= int (input('You have choose product B. How many items do you want?\n'))
				if quant>=0:
					Fprice=Fprice - priceB # in case previously the user had bought the same product, to not duplicate prices
					quantB=quant + quantB # in case previously the user had bought the same product
					print ('You have choose {} items'. format (quantB))
					priceB=quantB * productB
					print ('The original price is ${} .The reduced price is $ {}'.format ((500 * quantB),priceB))
					Fprice=Fprice + priceB # for the final invoice
				else:
					print ('You have to write a positive number')
			elif producto=='C' :
				quant= int (input('You have choose product C. How many items do you want?\n'))
				if quant>=0:
					Fprice=Fprice - priceC # in case previously the user had bought the same product, to not duplicate prices
					quantC=quant + quantC # in case previously the user had bought the same product
					print ('You have choose {} items'. format (quantC))
					priceC=quantC * productC
					print ('The original price is ${} .The reduced price is $ {}'.format ((250 * quantC),priceC))
					Fprice=Fprice + priceC # for the final invoice
				else:
					print ('You have to write a positive number')	
			elif producto=='D':
				quant= int (input('You have choose product D. How many items do you want?\n'))
				if quant>=0:
					Fprice=Fprice - priceD # in case previously the user had bought the same product, to not duplicate prices
					quantD=quant + quantD # in case previously the user had bought the same product
					print ('You have choose {} items'.format (quantD))
					priceD=quantD * productD
					print ('The price is $', priceD)
					Fprice=Fprice + priceD # for the final invoice
				else:
					print ('You have to write a positive number')
			elif producto=='E':
				quant= int (input('You have choose product E. How many items do you want?\n'))
				if quant>=0:
					Fprice=Fprice - priceE # in case previously the user had bought the same product, to not duplicate prices
					quantE=quant + quantE # in case previously the user had bought the same product
					print ('You have choose {} items'.format (quantE))
					priceE=quantE * productE
					print ('The price is $', priceE)
					Fprice=Fprice + priceE # for the final invoice
				else:
					print ('You have to write a positive number')
			else: # input different to A-E
				print ('Invalid option. Write A, B, C, D,E')
			
			# final invoice
			
			print ('\nTotal amount to pay for all the selected products ${} \n'. format (Fprice))
			
		else: # continuation of the 'if' of line 23
			if decision!='N': 
				print('Invalid option. Write Y or N')
				decision='Y' # allow the user to continue buying by showing the initial question again
			else: # user choose to leave the program
				print ('Good bye. Thanks for using our services')
				#to close the while loop 
				print ('\nProduct A: {} items. Price: $ {}'.format (quantA, priceA))
				print ('\nProduct B: {} items. Price: $ {}'.format (quantB, priceB))
				print ('\nProduct C: {} items. Price: $ {}'.format (quantC, priceC))
				print ('\nProduct D: {} items. Price: $ {}'.format (quantD, priceD))
				print ('\nProduct E: {} items. Price: $ {}'.format (quantE, priceE))
				
				print ('\nTotal amount to pay ${} \n'. format (Fprice))
	except: # in case the user write a letter instead of the amount of products to buy
		print ('invalid option. You have to write a number')
