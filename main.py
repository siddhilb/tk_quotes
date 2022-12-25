import tkinter as tk
import random
win = tk.Tk()
win.geometry('800x800')
rquote = random.choice(list(open('quotes.txt')))
quote = tk.Label(font=('Arial',40),text=f"{rquote}",wraplength=800, justify="center")

def generate():
    global rquote
    #print(rquote)
    quote.pack()
    rquote = random.choice(list(open('quotes.txt')))
    quote.config(text=rquote)
    print(rquote.index('~'))
generate = tk.Button(font=('Arial',30),text='Click to generate quote',command=generate)
generate.pack(padx=0,pady=50)
#print(quotes)
win.mainloop()