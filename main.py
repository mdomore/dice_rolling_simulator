from PIL import Image, ImageTk
import tkinter as tk
import random

# top-level widget which represents the main window of an application
window = tk.Tk()
window.geometry('600x600')
window.title('Roll the Dice')
window.config(bg='#59A8BA')

tk.Label(window, text='Roll the Dice', font='arial 24 bold', fg='#00062D', bg='#59A8BA').pack()


def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.config(image=DiceImage)
    ImageLabel.image = DiceImage


# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tk.Label(window, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)

# adding button
button = tk.Button(window, font='arial 13 bold', text='ROLL', padx=5, fg='#00062D', bg='#59A8BA',
                   command=rolling_dice)
button.pack(expand=True)

window.mainloop()
