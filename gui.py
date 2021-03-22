#tkinter benodigt heden
import tkinter as tk
window = tk.Tk()

#frames
frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()

#content
#tekst
greet = tk.Label(master=frame_a,
    text="Welkom in de rik borghuis GUI experience wil je jezelf introduceren?",
    background="green",
    padx="125",
    pady="125",   
)
#naam
intro = tk.Entry(master=frame_b,
    background="black",
    foreground="green",
               
)
#tekst
enjoy = tk.Label(master=frame_c,
    text="Hello i hope u enjoyed im gonna speak gibberish now dgyihgdluqhgduqgbdi",
    background="blue",             
    padx="125",
    pady="125",
)

#packs
frame_a.pack()
frame_b.pack()
frame_c.pack()
greet.pack()
intro.pack()
enjoy.pack()
