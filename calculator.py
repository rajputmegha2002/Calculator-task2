from tkinter import *

def click(event):
    global scrval
    text = event.widget.cget("text")
    print(text)
    
    if text =="=":
        if scrval.get().isdigit():
           value = int(scrval.get())
        else:
           value=eval(scrbox.get())

        scrval.set(value)
        scrbox.update()

    elif text =="AC":
        scrval.set("")
        scrbox.update()

    elif text=="<--":
       ex=scrval.get()
       ex=ex[0:len(ex)-1]
       scrval.set(ex)
       scrbox.update()
       
    else:
        scrval.set(scrval.get() + text)
        scrbox.update()


root =Tk()
root.geometry("222x400")
root.title("Calculator")

scrval=StringVar()
scrval.set("")
scrbox= Entry(root,textvariable=scrval, font="lucida 20 bold")
scrbox.pack(padx=5,pady=8)

frame1= Frame (root, bg="yellow")
frame1.pack(side=TOP)

temp=1
for i in range (0,3):
  for j in range(0,3):
  
    button=Button(frame1, text=str(temp), padx=10, pady=12, font="licida 10 bold") 
    button.bind("<Button-1>", click)
    button.grid(row=i,column=j, padx=5, pady=8)
    temp=temp+1


button= Button(frame1, text="0", padx=10, pady=12, font="lucida 10 bold") 
button.bind("<Button-1>", click)  
button.grid(row=3, column=0, padx=5, pady=8)

button=Button(frame1, text=".", padx=10,pady=12, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=3, column=1, padx=5, pady=8)

button=Button(frame1, text="/", padx=10,pady=12, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=3, column=2, padx=5, pady=8)

button=Button(frame1, text="+", padx=10,pady=12, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=0, column=3, padx=5, pady=8)

button=Button(frame1, text="-", padx=10,pady=12, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=1, column=3, padx=5, pady=8)

button=Button(frame1, text="*", padx=10,pady=18, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=2, column=3, padx=5, pady=8)

button=Button(frame1, text="=", padx=10,pady=12, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=3, column=3, padx=5, pady=8)

button=Button(frame1, text="<--", padx=25,pady=8, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=4, column=0, padx=5, pady=8, columnspan=2)

button=Button(frame1, text="AC", padx=25,pady=8, font="lucida 10 bold")
button.bind("<Button>", click)
button.grid(row=4, column=2, padx=5, pady=8, columnspan=2)

root.mainloop() 


