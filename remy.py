def firstStep():
	print("Which step do you begin with?")
	step = input()
	if step == "1":
		prepareTheMeat()
	else:
		print("You useless rat! You'll never be a chef!")
		openStatement()

def prepareTheMeat():
	print("You are starting with the meat. A wise decision, Remy.")
	print("You must decide whether to 1) season, 2) chop, or 3) soak the meat.")
	step = input()
	if step == "2":
		print("Very good! You are most NudelRat, Remy!")
		chopMeat()
	else:
		print("Wow. I cannot believe how incredibly dumb you are. YOU WILL NEVER BE A CHEF!")
		openStatement()

def chopMeat():
	print("How do you wish to chop the meat?")
	print("1) CHOP ZE MEAT WITH VIGOR (random chance to lose finger). Or 2) chop it carefully (random chance to anger customer).")
	step = input()
	if step == "1":
		vigorousChop()
	if step == "2":
		carefulChop()
	else:
		print("not an option. try again")
		chopMeat()

def carefulChop():
	print("You have chosen to carefully chop. Safe decision, oh wise cooking rat.")
	import random
	a = random.randint(1,10)
	if a > 8:
		print("Your safe chopping methods take forever. The customer is displeased and goes home. You are a failure of a rat.")
		openStatement()
	else:
		print("Your safety pays off with all ten of your rat fingers intact.")
		secondStep()

def vigorousChop():
	print("You have chosen to chop with VIGOR!")
	import random
	a = random.randint(1,10)
	if a > 9:
		print("TOO MUCH VIGOR! YOU HAVE LOST LITTLE RAT FINGER!")
		openStatement()
	else:
		print("YES! MUCH VIGOR! MANY STRANGTH! safe.")
		secondStep()

def secondStep():
	print("You now have your chopped meat in a bowl. Would you like to cook the meat or make the sauce?")
	step = input()
	if step == "cook the meat":
		print("Many great decisions from the master chef.")
		cookTheMeat()
	else:
		print("PREPARE THE SAUCE WAS STEP 3. YOU CANNOT READ SIMPLE INSTRUCTIONS WITH YOUR RAT EYES.")
		openStatement()

def cookTheMeat():
	print("The meat must be cooked carefully at which temperature and in which instrument?")
	print("Options: 1) low heat, pan. 2) high heat, pot. 3) medium heat, tuba.")
	cook = input()
	if cook == "1":
		print("Correct! You are most wonderful, Remy!")
		seasonTheMeat()
	if cook == "3":
		print("..... interesting. Well, you are the famous cook rat, not I.")
		seasonTheMeat()
	else:
		print("What. What made you think that a pot was the correct instrument. A snake would make a better cook than you and")
		print("THEY HAVE NO HANDS!")
		openStatement()

def seasonTheMeat():
	print("Perhaps the most important decision. How will you season the meat?")
	print("1) a smidge. 2) EXACTLY four tablespoons. 3) With your little rat tail and a shaker. 4) idk, just kinda toss it?")
	season = input()
	if season == "3":
		print("Correct Master Chef! Use the resources pathetic humans do not have.")
		thirdStep()
	else:
		print("no.")
		openStatement()

def thirdStep():
	print("Now you must prepare the sauce. Choose your sauce.")
	print("Marinara, alfredo, or italian.")
	sauce = input()
	print("Fantastic! There is no wrong answer with sauce, but you made the best one.")
	assemble()

def assemble():
	print("Alright, Remy. You made it this far. How will you assemble the dish?")
	print("1) with flair and style! (random chance for failure.) 2) very quickly (chance to bore customer).")
	decide = input()
	if decide == "1":
		finalFlair()
	if decide == "2":
		finalQuick()

def finalFlair():
	print("You have chosen Flair!")
	import random
	a = random.randint(1,10)
	if a > 9:
		print("The cart is rolled out to the customer's table with your meat and sauce. You begin a show of throwing the ingrediants ")
		print("in the air but your little rat fingers fumble the sauce and spill it all over the customer! 0 stars.")
	else:
		print("The cart is rolled out to the customer's table with your meat and sauce. You begin a show of throwing the ingrediants ")
		print("in the airand everything comes together exactly as planned. The tablecloth flutters onto the table, the plate lands ")
		print("neatly in the middle of the table, the food perfectly stacks itself on the plate.") 
		print("You whip the sauce around with your rat tail and slide the plate ")
		print("in front of the customer. They dig into the delicious food excitedly! 5 stars! You are most fantastic cook rat ever!")
	openStatement()

def finalQuick():
	print("You have chosen to quickly assemble food. The customer gives you three stars.")
	openStatement()

def openStatement():
	print("-------------------------------------------------------------------------------------")
	print("Hello! You are famed cooking rat, Remy. A customer has requested a Ratatoullie.")
	print("How to make the perfect Ratatoullie.")
	print("Step one, prepare the meat. Step two, cook the meat. Step three, prepare the sauce. Step four, assemble dish.")
	firstStep()

openStatement()