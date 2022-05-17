import random
import tkinter as tk
from tkinter import *

number = []
numberfinal = []
x = 0
while len(number) != 4:
    if x not in number and x != 0:
        number.append(x)
    else:
        x = random.randint(1, 9)
for i in number:
    numberfinal.append(str(i))


guesses = 1

mydict = {}


def ok():
    print(1)


def Guess1(guess):
    correct = True
    global mydict
    global guesses
    if label['text'] == 'Welcome to XY. The objective of the game \n is to guess a random 4 digit number.\n For each digit you guess \n correctly in the correct position, you will get a Y.\n   If the digit is correct but in the wrong place,\n you will get an x. To begin,\n go ahead and enter your first guess!':
        if list(guess) != numberfinal:
            label.config(font=("Courier", 12), anchor='nw')
            ans = ''
            for i in guess:
                if i in numberfinal:
                    if guess.index(i) == numberfinal.index(i):
                        ans += 'y'
                    else:
                        ans += 'x'
            for i in guess:
                if guess.count(i) > 1:
                    correct = False
                    label['text'] = '  '
            for i in guess:
                if i not in '123456789':
                    correct = False
                    label['text'] = '  '
            if len(guess) != 4:
                correct = False
                label['text'] = '  '
            if correct == True:
                label['text'] = "{}: You have {} x's and {} y's".format(
                    guess, ans.count('x'), ans.count('y'))
        else:
            label['text'] = 'Horray, you won in {} guess(es)'.format(guesses)
            label.config(font=("Courier", 24), anchor='center')
    elif list(guess) != numberfinal:
        label.config(font=("Courier", 12), anchor='nw')
        ans = ''
        for i in guess:
            if i in numberfinal:
                if guess.index(i) == numberfinal.index(i):
                    ans += 'y'
                else:
                    ans += 'x'

        for i in guess:
            if guess.count(i) > 1:
                correct = False
                break
        if len(guess) != 4:
            correct = False
        for i in guess:
            if i not in '123456789':
                correct = False
        guesses += 1
        if correct == True:
            label['text'] += "\n{}: You have {} x's and {} y's".format(guess,
                                                                       ans.count('x'), ans.count('y'))
    else:
        label['text'] = 'Horray, you won in {} guess(es)'.format(guesses)
        label.config(font=("Courier", 24), anchor='center')

    entry.delete(0, 'end')


root = tk.Tk()
root.title('X Y game')
canvas = tk.Canvas(root, height=700, width=800)
canvas.pack()

# Adding GUI elements and stylings
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
label2 = tk.Label(
    root, text='Rules: No 0s\nno duplicates\nNumber is always 4 digits long')
label2.place(relx=0.35, rely=0)

button = tk.Button(frame, text='Guess', font=40,
                   command=lambda: Guess1(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.8,
                  relwidth=1, anchor='n')


label = tk.Label(lower_frame, text='Welcome to XY. The objective of the game \n is to guess a random 4 digit number.\n For each digit you guess \n correctly in the correct position, you will get a Y.\n   If the digit is correct but in the wrong place,\n you will get an x. To begin,\n go ahead and enter your first guess!', font=('Modern', 24))
label.place(relwidth=1, relheight=1)
root.bind('<Return>', (lambda x: (Guess1(entry.get()))))


root.mainloop()
print(numberfinal)
