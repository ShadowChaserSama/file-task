import tkinter as tk
import json

window = tk.Tk()
window.geometry('500x500+100+120')
window.resizable(0,0)
window.title('LeaderBoard App')


data = {}
with open('text.json','r',encoding='utf-8') as f:
    data = json.load(f)


def leave():
    return exit()

def show():
    window2 = tk.Toplevel(window)
    window2.title('Leaderboard')
    window2.geometry('250x250')
    window2.resizable(0,0)
    
    L = sorted(data.items(),key=lambda p : p[1],reverse=True)
    
    for i,(name,score) in enumerate(L,start=1):
        text = tk.Label(window2,text=f'{i}# {name} -> {score}')
        text.pack()

def show2():
    window2 = tk.Toplevel(window)
    window2.title('Leaderboard')
    window2.geometry('250x250')
    window2.resizable(0,0)
    
    for i in data.keys():
        if 'm' in i.lower():
            text = tk.Label(window2,text=i)
            text.pack()


text = tk.Label(window,text='Select One: ',fg='red',font='Times 15')
text.pack(side=tk.TOP)

button1 = tk.Button(window,text='Show',bg='green',width=6,height=1,command=show)
button1.place(x=220,y=100)

button2 = tk.Button(window,text='Show2',bg='cyan',width=6,height=1,command=show2)
button2.place(x=300,y=100)

button3 = tk.Button(window,text='Quit',bg='red',width=6,height=1,command=leave)
button3.place(x=140,y=100)


window.mainloop()
