print("Please insert your card")
p= int(input("Enter your 4 digit pin \n"))
if p>=0000 and p<=9999:
        
	print("Welcome to SBI")
	print("Saving Account: 1\nCurrent Account: 2")

	ac = int(input("Choose your Account type \n"))

	if ac == 1:
		print("Cash widrawal: 1\nMini Statement: 2")
		opt = int(input("Please Enter the Amount multiple of 500\n"))

		if opt ==1:

			acc =56988.78 # Account balance

			amt =int(input("Please Enterthe Amount multiple of 500\n"))

			if amt%500==0 and amt<=acc and amt<=10000:

				print("Collect your Cash")

			else :
				print("Please re-enter your Amount")

		elif opt==2:
			print("Your last 5 transsactions.....")

    elif ac == 2:

    	print("Cash widrawal: 1\nMini Statement: 2")
     	opt = int(input("Choose your option\n"))
                 
        if opt ==1 :
        	acc = 899995.99 # Account Ballance

        	amt = int(input("Please Enterthe Amount multiple of 500\n"))

    		if amt%500==0 and amt<=acc and amt<=10000:

    			print("Collect your Cash")


    		else :
    			print("Please re-enter your Amount")



    	else opt==2:

    		print("Your last 5 transsactions.....")


    	
else :
	print("Invalid input")

print("Invalid Pin ")






