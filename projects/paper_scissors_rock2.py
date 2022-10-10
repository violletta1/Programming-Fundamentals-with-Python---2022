from tkinter import *
from PIL import Image, ImageTk
from random import randint

### main window ###

root = Tk()
root.title("Rock-Scissors-Paper")
root.configure(background="purple")
root.geometry("400x600")
root.resizable(False, False)

### pictures importt ###

paper_img = PhotoImage(file='paper-img.png')
rock_img = PhotoImage(file='rock-img.png')
scissors_img = PhotoImage(file='scissors-img.png')

comp_paper_img = PhotoImage(file='paper-img.png')
comp_rock_img = PhotoImage(file='rock-img.png')
comp_scissors_img = PhotoImage(file='scissors-img.png')

### pictures insert ###

computer_choice = Label(root, image=comp_paper_img)
user_choice = Label(root, image=paper_img)
computer_choice.place(x=250, y=70)
user_choice.place(x=50, y=70)

###choices###

choices = ["rock", "paper", "scissors"]


def user_and_computer_choices(x):
    comp_choice = choices[randint(0, 2)]
    if comp_choice == "rock":
        computer_choice.configure(image=comp_rock_img)
    elif comp_choice == "paper":
        computer_choice.configure(image=comp_paper_img)
    else:
        computer_choice.configure(image=comp_scissors_img)

    if x == "paper":
        user_choice.configure(image=paper_img)
    elif x == "rock":
        user_choice.configure(image=rock_img)
    else:
        user_choice.configure(image=scissors_img)
    who_is_the_winner(x, comp_choice)


def updateMessage(x):
    message['text'] = x


def UpdateUserScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = str(score)


def UpdateComputerScore():
    score = int(computer_score['text'])
    score += 1
    computer_score['text'] = str(score)


def who_is_the_winner(player, computer):
    if player == computer:
        updateMessage("Draw!")
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You loose')
            UpdateComputerScore()
        else:
            updateMessage('You win')
            UpdateUserScore()
    elif player == 'paper':
        if computer == 'scissors':
            updateMessage('You loose')
            UpdateComputerScore()
        else:
            updateMessage('You win')
            UpdateUserScore()
    elif player == 'scissors':
        if computer == 'rock':
            updateMessage('You loose')
            UpdateComputerScore()
        else:
            updateMessage('You win')
            UpdateUserScore()


###buttons###

paper = Button(root, image=paper_img, bg='#000', bd=5, command=lambda: user_and_computer_choices("paper"))
paper.place(x=7, y=400)

rock = Button(root, image=rock_img, bg='#000', bd=5, command=lambda: user_and_computer_choices("rock"))
rock.place(x=150, y=400)

scissors = Button(root, image=scissors_img, bg='#000', bd=5, command=lambda: user_and_computer_choices("scissors"))
scissors.place(x=290, y=400)

###scores###
Label(root, font=("arial", 15, "bold"), text="Player's score:", bg="red", fg="black").place(x=45, y=200)
player_score = Label(root, text=0, font=70, bg="red", fg="black")
player_score.place(x=170, y=200)
Label(root, font=("arial", 15, "bold"), text=":Computer's score", bg="red", fg="black").place(x=230, y=200)
computer_score = Label(root, text=0, font=70, bg="red", fg="black")
computer_score.place(x=195, y=200)

###output messages###
message = Label(root, font=('arial', 15, 'bold'), bg="purple", fg="white")
message.place(x=165, y=250)

root.mainloop()
