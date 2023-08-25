from tkinter import *

        
def one():
    global main
  
    main=Tk()
    main.title("Haree Krishna Library")
    main.geometry('900x600')
    main.minsize(900,600)
    main.maxsize(900,600)
    global name
    global password
    name=StringVar()
    password=StringVar()
    def data():
        print("my name is kartik")
    Label(main,text='Welcome to Time Table Generator',font=("Arial",15),height="7").pack(side='top')
    Label(main,text='Log In',font=("Arial", 25)).pack()
    login=Frame(main)
    login.pack()
    Label(login,text='User Id ',font=("Arial",15)).grid(row=0,column=0,pady=25)
    Entry(login,textvariable=name).grid(row=0,column=1)
    Label(login,text='Password',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Entry(login,textvariable=password,show='*').grid(row=1,column=1)
    
        

    Button(main,text="Enter",font=("Arial",25),command=data()).pack(pady=50)
    main.mainloop()


one()
