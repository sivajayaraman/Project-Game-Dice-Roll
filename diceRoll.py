import random
def dicegame(total_players,maximum_points):
	a_scores=0
	cpu=0
	points=[]
	ex=1
	position=0
	for i in range(0,total_players):
		points.append(0)
	print("Initiating game basics.....")
	if total_players==1:
		print("As you cannot play this game alone,I will play against you!")
		while a_scores<=maximum_points and cpu<=maximum_points:
			status=input("Your turn to roll the dice.Enter 1 to continue and 0 to exit.")
			if status==1:
				dice=random.randint(1,6)
				print("You got a {0} from the dice!".format(dice))
				a_scores=a_scores+dice
				print("Your Score:{0}".format(a_scores))
				if a_scores>=maximum_points:
					break
				else:
					dice=random.randint(1,6)
					print("Now,This is my turn!")
					print("I got a {0} from the dice!".format(dice))
					cpu=cpu+dice
					print("My Score:{0}".format(cpu))
					if cpu>=maximum_points:
						break
			else:
				print("Good Bye!")
				break
			if a_scores>cpu:
				print("You are leading at the moment!")
			elif a_scores<cpu:
				print("Im leading at the moment!")
			else:
				print("You are giving a good fight lad!")					
		if a_scores>cpu:
			print("You Win!")
		else:
			print("I Win!")								
	else:
		while ex!=0:
			for i in range(0,total_players):
				position=i%total_players
				print("Player {0}'s turn.".format(position+1))
				status=input("Your turn to roll the dice.Enter 1 to continue and 0 to Skip.")
				if status==1:
					dice=random.randint(1,6)
					print("You got a {0} from the dice!".format(dice))
					points[position]=points[position]+dice
					total=points[position]
					print("Your Total Point is {0}.".format(total))
					if total>=maximum_points:
						ex=0
						break
				else:
					print("Player {0} skipped his turn.".format(position+1))	
		position=1        		
		maxi=points[0]
		for i in range(1,total_players):
			if maxi<points[i]:
				position=i+1
		print("Congrats Player {0}! You Win.".format(position))		        		
total_players=input("Enter Total Number of Players   :")
if total_players<=0:
	print("Ivalid number of players.I will assume Total number of players as 1")
	total_players=1
maximum_points=input("Enter Maximum Points of the game:")
if maximum_points<0:
	print("Invalid Maximum Points.So I will assume Maximum Points as 10")
	maximum_points=10
dicegame(total_players,maximum_points)