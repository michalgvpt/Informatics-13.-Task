
import tkinter as tk
canvas=tk.Tk() #constructor

at=tk.Label(canvas,text='koeficient a:')
at.pack()
a=tk.Entry(canvas)
a.pack()
bt=tk.Label(canvas,text='koeficient b:')
bt.pack()
b=tk.Entry(canvas)
b.pack()
ct=tk.Label(canvas,text='koeficient c:')
ct.pack()
c=tk.Entry(canvas)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka=int(a.get())
    kb=int(b.get())
    kc=int(c.get())
    dis=(kb**2)-4*ka*kc
    if dis<0:
        print("Doesn't have a solution in R")
        result.config(text="Doesn't have a solution in R")
    elif dis==0:
        print('Root is:'-kb/(2*ka))
        result.config(text='Root is:'-kb/(2*ka))
    else:
        print('Solution for x1 is:',((-kb+dis**0.5)/(2*ka)))
        print('Solution for x2 is:',((-kb-dis**0.5)/(2*ka)))
        result.config(text='x1:'+str((-kb+dis**0.5)/(2*ka))+'\n'+'x2:'+str((-kb-dis**0.5)/(2*ka)))

result=tk.Label(canvas,text='result')
result.pack()

button=tk.Button(canvas,text='Click me!!!',command=executor)
button.pack()

canvas.mainloop() 