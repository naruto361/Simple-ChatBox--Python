from tkinter import *
root=Tk()
def send():
    send='You : '+a.get()
    text.insert(END,'\n'+send)
    if(a.get().lower()=='hi' or a.get().lower()=='hi!' or a.get().lower()=='hi !'):
        text.insert(END,'\n'+"Bot : Hello")
    elif(a.get().lower()=='hello'):
        text.insert(END,'\n'+"Bot : Hi")
    elif(a.get().lower()=='how are you?' or a.get().lower()=='how are you'):
        text.insert(END,'\n'+"Bot : I am fine. How are you ?")
    elif(a.get().lower()=='i am fine'):
        text.insert(END,'\n'+"Bot : Nice to hear that")
    elif(a.get().lower()=='what is your name' or a.get().lower()=='what is your name?'):
        text.insert(END,'\n'+"Bot : My name is ChatBot")
    else:
        text.insert(END,'\n'+"Bot : I didn't get it")

text=Text(root,bg='light yellow')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,text='Send',bg='green',width=20,command=send).grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('Simple Chatbot')
root.mainloop()
