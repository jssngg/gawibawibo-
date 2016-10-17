"""
Author : Joohee lim
created : 12-10-2016

"""

	# 0: gawi , 1: bawi , 2: bo
	 


	
import random

def determine_winner() :


	""" 0: gawi , 1: bawi , 2: bo"""
	 
	
	wincount = 0
	loosecount = 0
	drawcount =0

 	"""Determine windder of the game.
 	:param  my_hand: my hand parameter
	:param  com_hand: predefined computer choice
	:return None: None is returned.(void)"""

	for i in range(10):

	 	my_hand = int(input("show your hand.(0:gawi, 1: bawi, 2: bo    : "))
		com_hand = random.randint(0,2)

			

		print"com_hand :",com_hand

		a = my_hand - com_hand

		

		if a > 0 or a == -2:
			if (my_hand == 2 and com_hand == 0):
				print("You loose.")
				loosecount += 1
			else:
				print("you win")
				wincount += 1
		elif a ==0:
			print("You draw")
			drawcount += 1
		else:
			print("you loose")
			loosecount +=1


	print "you win ",wincount," times."
	print "you loose ",loosecount, "times."
	print "you draw" ,drawcount, "times."

	
	



determine_winner()










	
 
 




