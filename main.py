import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    df_french_words = pd.read_csv("F:/Python Bootcamp/Day 31/Windows/flash_card_project/data/words_to_learn.csv")
except FileNotFoundError:
    df_french_words = pd.read_csv("F:/Python Bootcamp/Day 31/Windows/flash_card_project/data/french_words.csv")

to_learn = df_french_words.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    df_data = pd.DataFrame(to_learn)
    df_data.to_csv("F:/Python Bootcamp/Day 31/Windows/flash_card_project/data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)


window = tk.Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="F:/Python Bootcamp/Day 31/Windows/flash_card_project/images/card_front.png")
card_back_img = tk.PhotoImage(file="F:/Python Bootcamp/Day 31/Windows/flash_card_project/images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tk.PhotoImage(file="F:/Python Bootcamp/Day 31/Windows/flash_card_project/images/wrong.png")
unknown_button = tk.Button(image=wrong_image, command=next_card, highlightthickness=0)
unknown_button.grid(row=1, column=0)

right_image = tk.PhotoImage(file="F:/Python Bootcamp/Day 31/Windows/flash_card_project/images/right.png")
known_button = tk.Button(image=right_image, command=is_known, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()




