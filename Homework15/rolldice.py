from PIL import Image, ImageTk
import random
import tkinter

# the main window of the application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice!')

# images of the dice
dice = ['die01.png', 'die02.png', 'die03.png', 'die04.png', 'die05.png', 'die06.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# constructing a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1
label1.pack( expand=True)

# function activated by button
def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1


# adding button
button = tkinter.Button(root, text='Roll the Dice!', fg='black', command=roll_dice)
button.pack( expand=True)
root.mainloop()
