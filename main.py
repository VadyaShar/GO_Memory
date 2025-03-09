import tkinter as tk
import json
import random


# Load JSON data
with open('GOGO.json', 'r', encoding='utf-8') as f:
    wort = json.load(f)

NUM_WORDS = 10

# Select random words
x = random.sample(list(wort.items()), NUM_WORDS)

# Function for button 1
def get_entry_value():
    value = entry.get().strip()
    An = value
    if An in x[0][1]:
        button.config(text="Ja", bg='blue')
    else:
        button.config(text="Nein", bg='red')

# Function for button 2
def get_entry_values():
    values = entry1.get().strip()
    An1 = values
    if An1 in x[1][1]:
        button1.config(text="Ja", bg='blue')
    else:
        button1.config(text="Nein", bg='red')

# Function for button 3
def get_entry_valuese():
    valuese = entry2.get().strip()
    An2 = valuese
    if An2 in x[2][1]:
        button2.config(text="Ja", bg='blue')
    else:
        button2.config(text="Nein", bg='red')


def get_entry_valuen():
    valuen = entry3.get().strip()
    An3 = valuen
    if An3 in x[3][1]:
        button3.config(text="Ja", bg='blue')
    else:
        button3.config(text="Nein", bg='red')

def get_entry_valuet():
    valuet = entry4.get().strip()
    An4 = valuet
    if An4 in x[4][1]:
        button4.config(text="Ja", bg='blue')
    else:
        button4.config(text="Nein", bg='red')


def get_entry_valuek():
    valuek = entry5.get().strip()
    An5 = valuek
    if An5 in x[5][1]:
        button5.config(text="Ja", bg='blue')
    else:
        button5.config(text="Nein", bg='red')


def get_entry_valuesen():
    valuesen = entry6.get().strip()
    An6 = valuesen
    if An6 in x[6][1]:
        button6.config(text="Ja", bg='blue')
    else:
        button6.config(text="Nein", bg='red')


def get_entry_valuent():
    valuent = entry7.get().strip()
    An7 = valuent
    if An7 in x[7][1]:
        button7.config(text="Ja", bg='blue')
    else:
        button7.config(text="Nein", bg='red')


def get_entry_valuets():
    valuets = entry8.get().strip()
    An8 = valuets
    if An8 in x[8][1]:
        button8.config(text="Ja", bg='blue')
    else:
        button8.config(text="Nein", bg='red')


def get_entry_valueku():
    valueku = entry9.get().strip()
    An9 = valueku
    if An9 in x[9][1]:
        button9.config(text="Ja", bg='blue')
    else:
        button9.config(text="Nein", bg='red')


window = tk.Tk()
window.title("GO_Memory")
window.geometry('310x580')
window.resizable(width=False, height=False)
window['bg'] = 'green'


label = tk.Label(window, text=x[0][0])
label.place(x=10, y=25)
entry = tk.Entry(window)
entry.place(x=140, y=25)

label1 = tk.Label(window, text=x[1][0])
label1.place(x=10, y=50)
entry1 = tk.Entry(window)
entry1.place(x=140, y=50)

label2 = tk.Label(window, text=x[2][0])
label2.place(x=10, y=75)
entry2 = tk.Entry(window)
entry2.place(x=140, y=75)

label3 = tk.Label(window, text=x[3][0])
label3.place(x=10, y=100)
entry3 = tk.Entry(window)
entry3.place(x=140, y=100)

label4 = tk.Label(window, text=x[4][0])
label4.place(x=10, y=125)
entry4 = tk.Entry(window)
entry4.place(x=140, y=125)

label5 = tk.Label(window, text=x[5][0])
label5.place(x=10, y=150)
entry5 = tk.Entry(window)
entry5.place(x=140, y=150)

label6 = tk.Label(window, text=x[6][0])
label6.place(x=10, y=175)
entry6 = tk.Entry(window)
entry6.place(x=140, y=175)

label7 = tk.Label(window, text=x[7][0])
label7.place(x=10, y=200)
entry7 = tk.Entry(window)
entry7.place(x=140, y=200)

label8 = tk.Label(window, text=x[8][0])
label8.place(x=10, y=225)
entry8 = tk.Entry(window)
entry8.place(x=140, y=225)

label9 = tk.Label(window, text=x[9][0])
label9.place(x=10, y=250)
entry9 = tk.Entry(window)
entry9.place(x=140, y=250)


button = tk.Button(window, text="Go: ", command=get_entry_value)
button.place(x=270, y=25)

button1 = tk.Button(window, text="Go: ", command=get_entry_values)
button1.place(x=270, y=50)

button2 = tk.Button(window, text="Go: ", command=get_entry_valuese)
button2.place(x=270, y=75)

button3 = tk.Button(window, text="Go: ", command=get_entry_valuen)
button3.place(x=270, y=100)

button4 = tk.Button(window, text="Go: ", command=get_entry_valuet)
button4.place(x=270, y=125)

button5 = tk.Button(window, text="Go: ", command=get_entry_valuek)
button5.place(x=270, y=150)

button6 = tk.Button(window, text="Go: ", command=get_entry_valuesen)
button6.place(x=270, y=175)

button7 = tk.Button(window, text="Go: ", command=get_entry_valuent)
button7.place(x=270, y=200)

button8 = tk.Button(window, text="Go: ", command=get_entry_valuets)
button8.place(x=270, y=225)

button9 = tk.Button(window, text="Go: ", command=get_entry_valueku)
button9.place(x=270, y=250)


def btn_command():
    info_str = f'Ответы: {str(x[0]) + "\n" + str(x[1]) + "\n" + str(x[2]) + "\n" + str(x[3]) + "\n" + str(x[4]) + "\n" + str(x[5]) + "\n" + str(x[6]) + "\n" + str(x[7]) + "\n" + str(x[8]) + "\n" + str(x[9])}'
    frame = tk.Frame(window, bg='grey')
    frame.place(relx=0.01, rely=0.01, relwidth=1, relheight=0.8)
    labels = tk.Label(frame, text=info_str)
    labels.pack()


btn = tk.Button(window, text="Ответы", command=btn_command)
btn.place(x=150, y=300)


# Start Tkinter event loop
window.mainloop()