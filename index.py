from os import system
from time import sleep

board_size = 0
number_of_ships = 1
ship_size = 3
players = [
	{
		"name": "Player_1",
		"player_board": [], 
		"shots_board": [],
		"hits": 0,
		"misses": 0,
		"hits_taken": 0,
	},
	{
		"name": "Player_2",
		"player_board": [], 
		"shots_board": [],
		"hits": 0,
		"misses": 0,
		"hits_taken": 0,
	}
]



def clear():
	system("cls")

def generate_boards():
	global board_size
	
	while True:
		try:
			board_size = int(input("Let's create the war zone, Enter a number between 5 and 20: "))
			if board_size > 4 and board_size < 21:
				break
			print ("I'm sorry Captain, out cannons can't cover these surfaces")
		except:
			print ("You need to enter a number")

	for i in range(0, board_size):
		players[0]["player_board"].append(["O"] * board_size)
		players[0]["shots_board"].append(["O"] * board_size)

		players[1]["player_board"].append(["O"] * board_size)
		players[1]["shots_board"].append(["O"] * board_size)

def print_board(board):
	print("\n")
	for i in range(0, len(board)):
		print (" ".join(board[i]))
	print("\n")

def get_direction():
	while True:
		try:
			direction = input("In which direction should we set sail captain?, vertical or horizontal(v/h): ")
			direction = direction.lower()
			if direction == "v" or direction == "h":
				return direction
		except:
			print ("We can only go vertically or horizontally")

def confirm_placement_coordinates(x, y, board, direction):
	if direction == "h" and (board_size - x) > 1:
		for i in range(0, ship_size):
			if board[y][x + i] == u"\u25A0":
				return False
		return True
	elif direction == "v" and (board_size - y) > 1:
		for i in range(0, ship_size):
			if board[y + i][x] == u"\u25A0":
				return False
		return True

def confirm_shooting_coordinates(x, y, board):
	try:
		if x < board_size and y < board_size:
			if board[y][x] == "X" or board[y][x] == u"\u25A1":
				print("That place is already dead, let's plot different coordinates for our canons")
				return False
			else:
				return True
	except:
		return False
	
	return False

def get_coordinates():		
	try:
		x = int(input("Choose your x coordinate: ")) - 1
		y = int(input("Choose your y coordinate: ")) - 1
	except:
		return 

	return [x, y]

def place_ships(board):
	
	for i in range(0, number_of_ships):
		coordinates = [0, 0]
		confirmation = False

		while not confirmation:
			try:
				print_board(board)
				ship_direction = get_direction()
				coordinates = get_coordinates()
				confirmation = confirm_placement_coordinates(coordinates[0], coordinates[1], board, ship_direction)
				clear()
			except:
				print("You need to enter a number captain")

		x = coordinates[0]
		y = coordinates[1] 

		if ship_direction == "h":
			for i in range(0, ship_size):
				board[y][x + i] = u"\u25A0"
		else:
			for i in range(0, ship_size):
				board[y + i][x] = u"\u25A0"

	
	print_board(board)
	input("All set for battle, press enter to continue...")
	clear()

def shoot(player_switch):
	if player_switch:
		p_index = 0
		o_index = 1
	else:
		p_index = 1
		o_index = 0

	player = players[p_index]
	oponent =  players[o_index]

	confirmed = False
	coordinates = [0, 0]

	clear()
	print (player["name"] + " shooting board")
	print_board(player["shots_board"])

	while not confirmed:
		try:
			coordinates = get_coordinates()
			confirmed = confirm_shooting_coordinates(coordinates[0], coordinates[1], oponent["player_board"])
		except:
			print("You need to enter a number")
	x = coordinates[0]
	y = coordinates[1]

	if oponent["player_board"][y][x] == u"\u25A0":
		oponent["player_board"][y][x] = "X"
		player["shots_board"][y][x] = "X"

		oponent["hits_taken"] += 1
		player["hits"] += 1
		print ("It's a hit captain, outstanding job!")
		sleep(2)
	else:
		player["shots_board"][y][x] = u"\u25A1"
		oponent["player_board"][y][x] = u"\u25A1"
		player["misses"] += 1
		print ("Nothing but dead fish there captain...")
		sleep(1)

def start_game():
	player_switch = True
	end_game = False

	while not end_game:
		shoot(player_switch)
		player_switch = not player_switch

		if (players[0]["hits_taken"] == ship_size * number_of_ships or 
			players[1]["hits_taken"] == ship_size * number_of_ships):
			end_game = True

	clear()
	if players[0]["hits_taken"] > players[1]["hits_taken"]:
		print("\n\n" + players[1]["name"] + " has conquered the battlezone, Congratulations!")
	else:
		print("\n\n" + players[0]["name"] + " has conquered the battlezone, Congratulations!")


def print_stats():
	print("\n\nMatch Stats: \n")
	print ("------------ Player 1 ------------")
	print ("HITS: " + str(players[0]["hits"]))
	print ("MISSES: " + str(players[0]["misses"]))
	print ("HITS TAKEN: " + str(players[0]["hits_taken"]))
	print_board(players[0]["player_board"])
	
	print ("\n")
	print ("------------ Player 2 ------------")
	print ("HITS: " + str(players[1]["hits"]))
	print ("MISSES: " + str(players[1]["misses"]))
	print ("HITS TAKEN: " + str(players[1]["hits_taken"]))
	print_board(players[1]["player_board"])

generate_boards()
clear()

print("Player one placing ships")
place_ships(players[0]["player_board"])
print("Player two placing ships")
place_ships(players[1]["player_board"])

input("Ready to battle, press enter to start game...")
clear()
start_game()
print_stats()




