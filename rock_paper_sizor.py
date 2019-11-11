print("Welcome to Pyython Developer's Rock Paper sizors game !!!!")
import tkinter
from tkinter import *
from tkinter import  ttk
import random



rock = 1
paper = 2
sizor = 3

names = {rock:"Rock",paper: "Paper",sizor:"Sizor"}
rules = {rock: sizor,paper:rock,sizor:paper}

def gui():

	names =  {rock: "Rock",paper: "Paper",sizor: "Sizor"}
	rules = {rock: sizor,paper: rock,sizor: paper}

#computer_score = 0
#player_score = 0

#print ("press start to begain the game ")


def start():
	print("start the game")
	while game():
		pass


def game():
	
	player = player_choice.get()
	computer = random.randint(1,3)
	computer_choice.set(names[computer])
	result (player,computer)


#	def move():
#		while True:
#			print (" press 1 for rock\n press 2 for paper\n press 3 for sizor")
#			player = input()
#			try:
#				player = int(player)
#				if player in (1,2,3):
#				return player
#			except ValueError:
#				print("sorry didn't get tht ")


def result(player,computer):
	global rules
	new_score = 0
#		print( "1....")
#		time.sleep(1)
#		print("2...")
#		time.sleep(2)
#		print("3..")
#		time.sleep(0.5)
#		computer_input = "computer through {0}:".format(names[computer])
#		global player_score,computer_score
	if player == computer:
		result_set.set("tie game")
	else:
		if rules[player] == computer:
			result_set.set("you won the game")
			new_score = player_score.get()
			new_score+=1
			player_score.set(new_score)
		else:
			result_set.set("you lose the game better luck nxt time")
			new_score=computer_score.get()
			new_score+=1
			computer_score.set(new_score)
print ("thnx for playing")


rps_window = Toplevel()
rps_window.title ("Rock, Paper, Scissors")


player_choice = IntVar()
computer_choice = StringVar()
result_set = StringVar()
player_choice.set(1)
player_score = IntVar()
computer_score = IntVar()


rps_frame = Frame(rps_window, padx = 12,pady = 12, width = 300)
rps_frame.grid(column=0, row = 0, sticky=(N,W,E,S) )
rps_frame.columnconfigure(0, weight=1)
rps_frame.rowconfigure(0,weight=1)


Label(rps_frame, text='Player').grid(column=1, row = 1, sticky = W)
Radiobutton(rps_frame, text ='Rock', variable = player_choice, value = 1).grid(column=1,row=2, sticky=W)
Radiobutton(rps_frame, text ='Paper', variable = player_choice, value = 2).grid(column=1,row=3, sticky=W)
Radiobutton(rps_frame, text ='Scissors', variable = player_choice, value =3).grid(column=1, row=4, sticky=W)
Label(rps_frame, text='Computer').grid(column=3, row = 1, sticky = W)
Label(rps_frame, textvariable = computer_choice).grid(column=3, row=3, sticky = W)
Button(rps_frame, text="Play", command = start()).grid(column = 2, row = 2)
Label(rps_frame, text = "Score").grid(column = 1, row = 5, sticky = W)
Label(rps_frame, textvariable = player_score).grid(column = 1, row = 6, sticky = W)
Label(rps_frame, text = "Score").grid(column = 3, row = 5, sticky = W)
Label(rps_frame, textvariable = computer_score).grid(column = 3, row = 6, sticky = W)
Label(rps_frame, textvariable = result_set).grid(column = 2, row = 7)













#def score():
#	global computer_score , player_score
#	print( "high scores:")
#	print("player: ",player_score)
#	print("cpmputer: ",computer_score)	



start()





