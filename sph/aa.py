
"""
======================
#Author : Joohee Lim
#Created : 12-10-2016
======================
"""


'''0: gawi , 1: bawi , 2: bo'''
	 

'#Italics'

	
import random

def determine_winner() :

 
	""" 0: gawi , 1: bawi , 2: bo """
	 
	
	wincount = 0
	loosecount = 0
	drawcount =0

 	"""Determine winner of the game.
 	:param  my_hand: my hand parameter
	:param  com_hand: predefined computer choice
	:return None: None is returned.(void)"""

	for i in range(10):

	"""게임은 10번 반복한다."""

	* com_hand and my_hand will play game for 10 times.*

	 	my_hand = int(input("show your hand.(0:gawi, 1: bawi, 2: bo    : "))
		com_hand = random.randint(0,2)
		"""com_hand는 컴퓨터의 손으로 랜덤 0: gawi , 1: bawi , 2: bo이다,"""

			

		print"com_hand :",com_hand

		a = my_hand - com_hand

	
	

		
	"""
	1.a 는 내가 낸 주먹/가위/보를 의미하는 수에서 컴퓨터가 낸 수를 빼는 것이다.
	2.같은 수는 같은 손 모양을 의미한다.
	같은 수는 비긴다.
	(a == 0)
	3.여기서 a>0이면 이긴다.
	 바위는 가위에게 이기고 (1 - 0 = 1)
	보는 바위에게 이기지만 (2 - 1 = 1)
	4.보는 가위에게 지므로 ( 2 - 0 = 2 )  my_hand == 2 and com_hand == 0일 경우에는 진다.
	5.a < 0 일 경우 패 """

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

	"""각각의 게임마다 승/패/비김을 알려주며
	승/패/비긴 횟수를 저장한다."""

	print "you win ",wincount," times."
	print "you loose ",loosecount, "times."
	print "you draw" ,drawcount, "times."

	"""게임이 끝나면 승리한 횟수,진 횟수, 비긴 횟수를 알려준다."""
	
	



determine_winner()










	
 
 




