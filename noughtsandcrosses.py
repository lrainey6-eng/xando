import time
import random as rand
import string

digits = ['1','2','3','4','5','6','7','8','9']
bin_digs = ['0','1']
turns = ['1st','2nd']
symbols = ['X','O']

grid = ("""

	1 | 2 | 3
	---------
	4 | 5 | 6
	---------
	7 | 8 | 9

	""")


running = True
plyr_win = False
three_consec_ai = False

symbolX = 'X'
symbolO = 'O'

while running:
	while running:
		print ("Welcome to noughts and crosses! For how to play, type 'Instructions', or to start, type 'start'. ")
		instruction = str(input(">>> ")).lower()
		if instruction == 'instructions':
			print("""
				You will flip a coin to decide who starts, you or the computor. Then, when it's your turn,
				type in a number (corresponding to the numbers on the grid), and your chosen symbol will appear in that slot.""")
		elif instruction == 'start':
			running = False
	time.sleep(1)
	print("Time for the coin flip! Heads or Tails? ")
	coin_choice = str(input(">>> ")).lower()
	if coin_choice == 'heads':
		coin_no = 0
	elif coin_choice == 'tails':
		coin_no = 1
	coin_result = int(rand.choice(bin_digs))
	if coin_result == coin_no:
		print ("You have won the coin flip! Would you like to be noughts or crosses? ")
		flip_won = True
		symbol = str(input(">>> ")).lower()
		print("Would you like to have the first or second turn? (Type '1st' or '2nd')")
		turn_choice = str(input(">>> ")).lower()
		if symbol == 'noughts':
			ai_symbol = symbolX
			player_symbol = symbolO
		else:
			ai_symbol = symbolO
			player_symbol = symbolX
	else:
		print ("You have lost the coin flip. ")
		rand_bin = int(rand.choice(bin_digs))
		if rand_bin == 0:
			ai_symbol = symbolX
			player_symbol = symbolO
		else:
			ai_symbol = symbolO
			player_symbol = symbolX
		turn_choice = rand.choice(turns)
		if turn_choice == '1st':
			ai_turn_choice = '2nd'
		elif turn_choice == '2nd':
			ai_turn_choice = '1st'
		print ("AI has chosen to go", ai_turn_choice + '.')
	time.sleep(1)
	if turn_choice == '1st':
		picking = True
		game_running = True
		grid_full = False
		turn_count = 0
		while game_running and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
			while picking and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
				if not grid_full and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
					print ("Pick a grid number (1-9): ")
					print('\n')
					time.sleep(1)
					print (grid)
					grid_point = str(input(">>> "))
					space_free = False
					for letter in grid:
						if letter in digits:
							grid_full = False
						if letter == grid_point:
							space_free = True
					if space_free == False:
						print("That space is already taken or does not exist. Please choose an empty slot on the grid.")
					else:
						picking = False
						grid = grid.replace(grid_point, player_symbol)
						print ('\n')
						print (grid)
						turn_count += 1

						space1 = 'empty'
						space2 = 'empty'
						space3 = 'empty'
						space4 = 'empty'
						space5 = 'empty'
						space6 = 'empty'
						space7 = 'empty'
						space8 = 'empty'
						space9 = 'empty'

						for charact in grid:
							if charact in symbols or charact in digits:
							    if space1 == 'empty':
							        space1 = charact
							    elif space1 != 'empty':
							        if space2 == 'empty':
							            space2 = charact
							        elif space2 != 'empty':
							            if space3 == 'empty':
							                space3 = charact
							            elif space3 != 'empty':
							                if space4 == 'empty':
							                    space4 = charact
							                elif space4 != 'empty':
							                    if space5 == 'empty':
							                        space5 = charact
							                    elif space5 != 'empty':
							                        if space6 == 'empty':
							                            space6 = charact
							                        elif space6 != 'empty':
							                            if space7 == 'empty':
							                                space7 = charact
							                            elif space7 != 'empty':
							                                if space8 == 'empty':
							                                    space8 = charact
							                                elif space8 != 'empty':
							                                    space9 = charact
						three_consec = False
						three_consec_ai = False

						if space1 == player_symbol and space2 == player_symbol and space3 == player_symbol:
						    three_consec = True
						elif space1 == player_symbol and space5 == player_symbol and space9 == player_symbol:
						    three_consec = True
						elif space1 == player_symbol and space4 == player_symbol and space7 == player_symbol:
						    three_consec = True
						elif space2 == player_symbol and space5 == player_symbol and space8 == player_symbol:
						    three_consec = True
						elif space3 == player_symbol and space5 == player_symbol and space7 == player_symbol:
						    three_consec = True
						elif space3 == player_symbol and space6 == player_symbol and space9 == player_symbol:
						    three_consec = True
						elif space4 == player_symbol and space5 == player_symbol and space6 == player_symbol:
						    three_consec = True
						elif space7 == player_symbol and space8 == player_symbol and space9 == player_symbol:
						    three_consec = True


						if space1 == ai_symbol and space2 == ai_symbol and space3 == ai_symbol:
						    three_consec_ai = True
						elif space1 == ai_symbol and space5 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True
						elif space1 == ai_symbol and space4 == ai_symbol and space7 == ai_symbol:
						    three_consec_ai = True
						elif space2 == ai_symbol and space5 == ai_symbol and space8 == ai_symbol:
						    three_consec_ai = True
						elif space3 == ai_symbol and space5 == ai_symbol and space7 == ai_symbol:
						    three_consec_ai = True
						elif space3 == ai_symbol and space6 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True
						elif space4 == ai_symbol and space5 == ai_symbol and space6 == ai_symbol:
						    three_consec_ai = True
						elif space7 == ai_symbol and space8 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True

						if three_consec == True:
							print("GAME OVER: Player Wins! ")
							plyr_win = True
							game_running = False
							picking = False
							grid_full = True

						if three_consec_ai == True:
							print("GAME OVER: AI Wins. ")
							game_running = False
							picking = False
							grid_full = True

						digit_count = 0
						for letter in grid:
							if letter == 'X' or letter == 'O':
								digit_count += 1
						if digit_count == 9 and three_consec == False and three_consec_ai == False:
							print(" GAME OVER: Draw. ")
							game_running = False
							picking = False
							grid_full = True
							ai_choosing = False
						else:
							ai_choosing = True
						while ai_choosing and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
							print ("AI choosing... ")
							ai_choice = rand.choice(digits)
							ai_space_free = False
							for letter in grid:
								if letter == ai_choice:
									ai_space_free = True
								time.sleep(0.001)
							if ai_space_free == False:
								ai_choosing = True
							else:
								ai_choosing = False
								grid = grid.replace(ai_choice, ai_symbol)
								turn_count += 1
								print ("AI has chosen: ")
								print('\n')

								space1 = 'empty'
								space2 = 'empty'
								space3 = 'empty'
								space4 = 'empty'
								space5 = 'empty'
								space6 = 'empty'
								space7 = 'empty'
								space8 = 'empty'
								space9 = 'empty'

								for charact in grid:
									if charact in symbols or charact in digits:
									    if space1 == 'empty':
									        space1 = charact
									    elif space1 != 'empty':
									        if space2 == 'empty':
									            space2 = charact
									        elif space2 != 'empty':
									            if space3 == 'empty':
									                space3 = charact
									            elif space3 != 'empty':
									                if space4 == 'empty':
									                    space4 = charact
									                elif space4 != 'empty':
									                    if space5 == 'empty':
									                        space5 = charact
									                    elif space5 != 'empty':
									                        if space6 == 'empty':
									                            space6 = charact
									                        elif space6 != 'empty':
									                            if space7 == 'empty':
									                                space7 = charact
									                            elif space7 != 'empty':
									                                if space8 == 'empty':
									                                    space8 = charact
									                                elif space8 != 'empty':
									                                    space9 = charact

								three_consec = False
								three_consec_ai = False

								if space1 == player_symbol and space2 == player_symbol and space3 == player_symbol:
								    three_consec = True
								elif space1 == player_symbol and space5 == player_symbol and space9 == player_symbol:
								    three_consec = True
								elif space1 == player_symbol and space4 == player_symbol and space7 == player_symbol:
								    three_consec = True
								elif space2 == player_symbol and space5 == player_symbol and space8 == player_symbol:
								    three_consec = True
								elif space3 == player_symbol and space5 == player_symbol and space7 == player_symbol:
								    three_consec = True
								elif space3 == player_symbol and space6 == player_symbol and space9 == player_symbol:
								    three_consec = True
								elif space4 == player_symbol and space5 == player_symbol and space6 == player_symbol:
								    three_consec = True
								elif space7 == player_symbol and space8 == player_symbol and space9 == player_symbol:
								    three_consec = True

								if space1 == ai_symbol and space2 == ai_symbol and space3 == ai_symbol:
								    three_consec_ai = True
								elif space1 == ai_symbol and space5 == ai_symbol and space9 == ai_symbol:
								    three_consec_ai = True
								elif space1 == ai_symbol and space4 == ai_symbol and space7 == ai_symbol:
								    three_consec_ai = True
								elif space2 == ai_symbol and space5 == ai_symbol and space8 == ai_symbol:
								    three_consec_ai = True
								elif space3 == ai_symbol and space5 == ai_symbol and space7 == ai_symbol:
								    three_consec_ai = True
								elif space3 == ai_symbol and space6 == ai_symbol and space9 == ai_symbol:
								    three_consec_ai = True
								elif space4 == ai_symbol and space5 == ai_symbol and space6 == ai_symbol:
								    three_consec_ai = True
								elif space7 == ai_symbol and space8 == ai_symbol and space9 == ai_symbol:
								    three_consec_ai = True

								if three_consec == True:
									print("GAME OVER: Player Wins! ")
									plyr_win = True
									game_running = False
									picking = False
									grid_full = True

								if three_consec_ai == True:
									print("GAME OVER: AI Wins. ")
									game_running = False
									picking = False
									grid_full = True

								digit_count = 0
								for letter in grid:
									if letter == 'X' or letter == 'O':
										digit_count += 1
								if digit_count == 9 and three_consec == False and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
									print(" GAME OVER: Draw. ")
									game_running = False
									picking = False
									grid_full = True
								else:
									game_running = True
									picking = True
									running = True
									grid_full = False
	else:
		picking = True
		game_running = True
		grid_full = False
		turn_count = 0
		while game_running and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
			while picking and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
				if not grid_full and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
					ai_choosing = True
					while ai_choosing and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
						print ("AI choosing... ")
						ai_choice = rand.choice(digits)
						ai_space_free = False
						for letter in grid:
							if letter == ai_choice:
								ai_space_free = True
							time.sleep(0.001)
						if ai_space_free == False:
							ai_choosing = True
						else:
							ai_choosing = False
							grid = grid.replace(ai_choice, ai_symbol)
							turn_count += 1
							print ("AI has chosen: ")
							print('\n')

							space1 = 'empty'
							space2 = 'empty'
							space3 = 'empty'
							space4 = 'empty'
							space5 = 'empty'
							space6 = 'empty'
							space7 = 'empty'
							space8 = 'empty'
							space9 = 'empty'

							for charact in grid:
								if charact in symbols or charact in digits:
								    if space1 == 'empty':
								        space1 = charact
								    elif space1 != 'empty':
								        if space2 == 'empty':
								            space2 = charact
								        elif space2 != 'empty':
								            if space3 == 'empty':
								                space3 = charact
								            elif space3 != 'empty':
								                if space4 == 'empty':
								                    space4 = charact
								                elif space4 != 'empty':
								                    if space5 == 'empty':
								                        space5 = charact
								                    elif space5 != 'empty':
								                        if space6 == 'empty':
								                            space6 = charact
								                        elif space6 != 'empty':
								                            if space7 == 'empty':
								                                space7 = charact
								                            elif space7 != 'empty':
								                                if space8 == 'empty':
								                                    space8 = charact
								                                elif space8 != 'empty':
								                                    space9 = charact


							three_consec = False
							three_consec_ai = False

							if space1 == player_symbol and space2 == player_symbol and space3 == player_symbol:
							    three_consec = True
							elif space1 == player_symbol and space5 == player_symbol and space9 == player_symbol:
							    three_consec = True
							elif space1 == player_symbol and space4 == player_symbol and space7 == player_symbol:
							    three_consec = True
							elif space2 == player_symbol and space5 == player_symbol and space8 == player_symbol:
							    three_consec = True
							elif space3 == player_symbol and space5 == player_symbol and space7 == player_symbol:
							    three_consec = True
							elif space3 == player_symbol and space6 == player_symbol and space9 == player_symbol:
							    three_consec = True
							elif space4 == player_symbol and space5 == player_symbol and space6 == player_symbol:
							    three_consec = True
							elif space7 == player_symbol and space8 == player_symbol and space9 == player_symbol:
							    three_consec = True

							if space1 == ai_symbol and space2 == ai_symbol and space3 == ai_symbol:
							    three_consec_ai = True
							elif space1 == ai_symbol and space5 == ai_symbol and space9 == ai_symbol:
							    three_consec_ai = True
							elif space1 == ai_symbol and space4 == ai_symbol and space7 == ai_symbol:
							    three_consec_ai = True
							elif space2 == ai_symbol and space5 == ai_symbol and space8 == ai_symbol:
							    three_consec_ai = True
							elif space3 == ai_symbol and space5 == ai_symbol and space7 == ai_symbol:
							    three_consec_ai = True
							elif space3 == ai_symbol and space6 == ai_symbol and space9 == ai_symbol:
							    three_consec_ai = True
							elif space4 == ai_symbol and space5 == ai_symbol and space6 == ai_symbol:
							    three_consec_ai = True
							elif space7 == ai_symbol and space8 == ai_symbol and space9 == ai_symbol:
							    three_consec_ai = True

							if three_consec == True:
								print("GAME OVER: Player Wins! ")
								plyr_win = True
								game_running = False
								picking = False
								grid_full = True

							if three_consec_ai == True:
								print("GAME OVER: AI Wins. ")
								game_running = False
								picking = False
								grid_full = True

							digit_count = 0
							for letter in grid:
								if letter == 'X' or letter == 'O':
									digit_count += 1
							if digit_count == 9 and three_consec == False:
								print(" GAME OVER: Draw. ")
								game_running = False
								picking = False
								grid_full = True
							else:
								game_running = True
								picking = True
								running = True
								grid_full = False
					print ("Pick a grid number (1-9): ")
					print('\n')
					time.sleep(1)
					print (grid)
					grid_point = str(input(">>> "))
					space_free = False
					for letter in grid:
						if letter in digits:
							grid_full = False
						if letter == grid_point:
							space_free = True
					if space_free == False:
						print("That space is already taken or does not exist. Please choose an empty slot on the grid.")
					else:
						picking = False
						grid = grid.replace(grid_point, player_symbol)
						print ('\n')
						print (grid)
						turn_count += 1


						space1 = 'empty'
						space2 = 'empty'
						space3 = 'empty'
						space4 = 'empty'
						space5 = 'empty'
						space6 = 'empty'
						space7 = 'empty'
						space8 = 'empty'
						space9 = 'empty'

						for charact in grid:
							if charact in symbols or charact in digits:
							    if space1 == 'empty':
							        space1 = charact
							    elif space1 != 'empty':
							        if space2 == 'empty':
							            space2 = charact
							        elif space2 != 'empty':
							            if space3 == 'empty':
							                space3 = charact
							            elif space3 != 'empty':
							                if space4 == 'empty':
							                    space4 = charact
							                elif space4 != 'empty':
							                    if space5 == 'empty':
							                        space5 = charact
							                    elif space5 != 'empty':
							                        if space6 == 'empty':
							                            space6 = charact
							                        elif space6 != 'empty':
							                            if space7 == 'empty':
							                                space7 = charact
							                            elif space7 != 'empty':
							                                if space8 == 'empty':
							                                    space8 = charact
							                                elif space8 != 'empty':
							                                    space9 = charact


						three_consec = False
						three_consec_ai = False

						if space1 == player_symbol and space2 == player_symbol and space3 == player_symbol:
						    three_consec = True
						elif space1 == player_symbol and space5 == player_symbol and space9 == player_symbol:
						    three_consec = True
						elif space1 == player_symbol and space4 == player_symbol and space7 == player_symbol:
						    three_consec = True
						elif space2 == player_symbol and space5 == player_symbol and space8 == player_symbol:
						    three_consec = True
						elif space3 == player_symbol and space5 == player_symbol and space7 == player_symbol:
						    three_consec = True
						elif space3 == player_symbol and space6 == player_symbol and space9 == player_symbol:
						    three_consec = True
						elif space4 == player_symbol and space5 == player_symbol and space6 == player_symbol:
						    three_consec = True
						elif space7 == player_symbol and space8 == player_symbol and space9 == player_symbol:
						    three_consec = True

						if space1 == ai_symbol and space2 == ai_symbol and space3 == ai_symbol:
						    three_consec_ai = True
						elif space1 == ai_symbol and space5 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True
						elif space1 == ai_symbol and space4 == ai_symbol and space7 == ai_symbol:
						    three_consec_ai = True
						elif space2 == ai_symbol and space5 == ai_symbol and space8 == ai_symbol:
						    three_consec_ai = True
						elif space3 == ai_symbol and space5 == ai_symbol and space7 == ai_symbol:
						    three_consec_ai = True
						elif space3 == ai_symbol and space6 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True
						elif space4 == ai_symbol and space5 == ai_symbol and space6 == ai_symbol:
						    three_consec_ai = True
						elif space7 == ai_symbol and space8 == ai_symbol and space9 == ai_symbol:
						    three_consec_ai = True

						if three_consec == True:
							print("GAME OVER: Player Wins! ")
							plyr_win = True
							game_running = False
							picking = False
							grid_full = True

						if three_consec_ai == True:
							print("GAME OVER: AI Wins. ")
							game_running = False
							picking = False
							grid_full = True

						digit_count = 0
						for letter in grid:
							if letter == 'X' or letter == 'O':
								digit_count += 1
						if digit_count == 9 and three_consec == False and plyr_win == False and three_consec_ai == False and three_consec_ai == False:
							print(" GAME OVER: Draw. ")
							game_running = False
							picking = False
							grid_full = True
						else:
							ai_choosing = True
							picking = True
							game_running = True


