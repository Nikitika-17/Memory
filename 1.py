from tkinter import *
from random import shuffle
root = Tk()
root.resizable(False, False)
root.geometry("1200x1200")
size_cards = 300
opened_cards = []

mosquito_image = PhotoImage(file = "комар.gif")
beatle_image = PhotoImage(file = "жук2.gif")
bug_image = PhotoImage(file = "клоп.gif")
grasshoper_image = PhotoImage(file = "кузнечик.gif")
fly_image = PhotoImage(file = "муха.gif")
ladybug_image = PhotoImage(file = "коровка.gif")
dragonfly_image = PhotoImage(file = "стрекоза.gif")
cockroach_image = PhotoImage(file = "таракан.gif")

insect = ["комар", "комар", "жук2", "жук2", "клоп", "клоп", "кузнечик", "кузнечик", "муха", "муха", "коровка", "коровка", "стрекоза", "стрекоза", "таракан", "таракан"]
shuffle(insect)
insects_numbers = {"комар":0, "жук2":1, "клоп":2, "кузнечик":3, "муха":4, "коровка":5, "стрекоза":6, "таракан":7}
insects_images = {"комар":mosquito_image, "жук2":beatle_image, "клоп":bug_image, "кузнечик":grasshoper_image, "муха":fly_image, "коровка":ladybug_image, "стрекоза":dragonfly_image, "таракан":cockroach_image}

def opened(event):
    global steps, opened_cards
    try:
        if event.widget not in opened_cards:
            opened_cards.append(event.widget)
            event.widget["image"] = event.widget.image
        if len(opened_cards) == 2:
            if opened_cards[0].number == opened_cards[1].number:
                event.widget["image"] = event.widget.image
                root.after(300, away)
            else:
                root.after(300, close)
    except Exception:
        pass
    
def close():
    global opened_cards
    opened_cards[0]["image"] = ""
    opened_cards[1]["image"] = ""
    opened_cards.clear()

def away():
    global opened_cards
    opened_cards[0].place_forget()
    opened_cards[1].place_forget()
    opened_cards.clear()

cards = []
for i in range(4):
    cards.append([])
    for j in range(4):
        btn = Button(root, bg = 'blue')
        btn.image = ""
        btn.insect = ""
        btn.number = 0
        cards[i].append(btn)
        cards[i][j].place(x = size_cards * i - 1, y = size_cards * j - 1, width = size_cards, height = size_cards)
 
img = 0
for i in range(4):
    for j in range(4):
        cards[i][j].insect = insect[img]
        cards[i][j].image = insects_images[cards[i][j].insect]
        cards[i][j].number = insects_numbers[cards[i][j].insect]
        img += 1
    
root.bind('<Button-1>', opened)
root.mainloop()