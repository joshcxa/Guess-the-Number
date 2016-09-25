from tkinter import *

import random
winner = str(random.randint(1, 10))
winner = int(winner)

def guessed():
	guessint = userguess.get()
	int_answer = int(guessint)
	display = Label(bottomFrame, text="You guessed " + str(int_answer)).pack()

	while winner:
		if int_answer == winner:
			submitguess.config(state='disabled')
			output = Label(bottomFrame, text="Congratulations! You got it :)").pack()
			break
			return
		elif int_answer < winner:
			output = Label(bottomFrame, text="Your guess is too low. Try again.").pack()
			return
		elif int_answer > winner:
			output = Label(bottomFrame, text="Your guess is too high. Try again.").pack()
			return
		else:
			output = Label(bottomFrame, text="Your guess was invalid.").pack()
			return
	
root = Tk()
root.title("Guess the number")

topFrame = Frame(root)
topFrame.pack(fill=X, padx=15, pady=15)
bottomFrame = Frame(root)
bottomFrame.pack(fill=X, padx=15, pady=15)

# Show for testing
#Label(topFrame, text=winner).pack()

intro = Label(topFrame, text="Guess the number between 1 and 10.")
intro.pack(fill=X)

userguess = Entry(topFrame, bd = 1, justify = CENTER)
userguess.pack(fill=X)

submitguess = Button(topFrame, text = "Submit Guess", command = guessed)
submitguess.pack(fill=X)

root.mainloop()