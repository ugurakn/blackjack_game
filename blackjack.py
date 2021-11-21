import random
import sys
import time


class BJ:
	def __init__(self):
		self.deck = 4 * ["ACE", "2" , "3" , "4" ,"5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.deck_values = {"ACE": 11, "2":2 , "3":3 , "4":4 ,"5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
		
		random.shuffle(self.deck)
		
		self.game_start = True

class Player:
	def __init__(self):
		self.cards=[]
		self.total = 0

		self.turn = True

	def calc_total(self): # calculate total value of cards 
		total = 0

		for card in self.cards:
			total += bj.deck_values[card]

		if "ACE" in self.cards and total > 21:
			total -= 10

		self.total = total

		return self.total

	def card_log(self): # keeps a log of player's cards to be printed when called
		logs = []
		for card in self.cards:
			log = f"{card}"
			logs.append(log)

		logs = " - ".join(logs)

		print(f"PLAYER'S CARDS: {logs}")

class Pc():
	def __init__(self):
		self.cards=[]
		self.total = 0

	
	def card_log(self): # keeps a log of PC's cards to be printed when called
		logs = []
		for i, card in enumerate(self.cards):
			if i == 0:
				log = "[HIDDEN]"
			else:
				log = f"{card}"

			logs.append(log)

		logs = " - ".join(logs)

		print(f"PC'S CARDS: {logs}")

	def calc_total(self): # calculate total value of cards 
		total = 0

		for card in self.cards:
			total += bj.deck_values[card]

		if "ACE" in self.cards and total > 21:
			total -= 10

		self.total = total

		return self.total
		

def main():
	# start game by dealing out cards
	if bj.game_start:
		player.cards.extend(bj.deck[:2])
		del bj.deck[:2]
		pc.cards.extend(bj.deck[:2])
		del bj.deck[:2]
	
		#print initial game state (cards)
		print()
		player.card_log()
		pc.card_log()
		#print()

		bj.game_start = False

	# check turn and let current player decide
	if player.turn:
		print()
		move = input("Player: Hit or Stand?(h or s): ")
		player_move(move)
	else:
		pc_move()

def player_move(decision):
	
	if decision.lower() == "h":
		new_card = bj.deck.pop()
		player.cards.append(new_card)
		player.card_log()

		check_gm_state(player)

	elif decision.lower() == "s":
		player.turn = False
		print("Player stands.")

	else:
		player_move(decision)

	main()

def pc_move():
	print()
	print("PC PLAYS:", end=" ")

	pc_total = pc.calc_total()
	player_total = player.calc_total()

	if (player_total < pc_total): # stand 1
		print("Stand")
		pc.card_log()
		
		game_end()

	elif (pc_total >= 17) and (player_total <= pc_total): # stand 2
		print("Stand")
		pc.card_log()
		
		game_end()


	else:
		new = bj.deck.pop()
		pc.cards.append(new)

		print(f"Hit: {new}")
		pc.card_log()
		time.sleep(2)

		check_gm_state(pc)

	main()


def check_gm_state(current):
	if current is player:
		curr_total = current.calc_total()

		if curr_total > 21:
			print()
			print(f"Player busted! PC wins! (PC's hidden card was: {pc.cards[0]})")
			
			sys.exit()

	else:
		curr_total = current.calc_total()

		if curr_total > 21:
			print()
			print(f"PC busted! Player wins! (PC's hidden card was: {pc.cards[0]})")
			
			sys.exit()

	main()


def game_end():
	time.sleep(1)
	print(f"PC's hidden card: {pc.cards[0]}")
	time.sleep(1)

	if player.total > pc.total:
		print(f"Player Wins! (total score: {player.total})") 

	elif player.total < pc.total:
		print(f"PC Wins! (total score: {pc.total})")

	else:
		print("Draw! Both sides have the same score.")
	
	sys.exit()
	

# create object instances
bj = BJ()
player = Player()
pc = Pc()

if __name__ == "__main__":
	main()
