from tkinter import *
import requests


def get_quotes():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    new_data = data['quote']
    canvas.itemconfig(quote_text, text=new_data)


window = Tk()
window.config(padx=20, pady=20)
canvas = Canvas(window, width=300, height=414)

background_image = PhotoImage(file='background.png')
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text='', width=250, font=('Arial', 21, 'bold'), fill='white')
canvas.grid(row=0, column=0)

button_image = PhotoImage(file='kanye.png')
kanye_button = Button(image=button_image, highlightthickness=0, command=get_quotes)
kanye_button.grid(row=1, column=0)


window.mainloop()
