import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash Card Project")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

right_image = tk.PhotoImage(file="/Volumes/Extreme SSD/Python Bootcamp/Day 31/Mac/flash_card_project/images/right.png")
correct_button = tk.Button(image=right_image, highlightthickness=0)
correct_button.pack()

wrong_image = tk.PhotoImage(file="/Volumes/Extreme SSD/Python Bootcamp/Day 31/Mac/flash_card_project/images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0)
wrong_button.pack()


window.mainloop()




