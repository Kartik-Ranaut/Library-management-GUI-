from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as ms
from tkcalendar import *
from smtplib import *
from tkinter import ttk

#..........................................................#..........................................................#.................................................................#


      
#................................Dashboard................................................................................................................................
def screen3():
      global main3
      main3=Toplevel(main)
      main3.title("Dashboard")
      main3.geometry('900x600')
      main3.minsize(900,600)
      main3.maxsize(900,600)
      photo6 = PhotoImage(file = "logo.png")
      main3.iconphoto(False, photo6)
       
      canvas=Canvas(main3,width=900,height=600)
      img=PhotoImage(file="dashboard.png")
      canvas.create_image(0,0,anchor=NW,image=img)
      canvas.pack()
      

#...........................defining what will happenn when we click publish...................................
      def publish():
            global user_id
            global book_id
            global email_id
            
            user_id=StringVar()
            book_id=StringVar()
            email_id=StringVar()
            book=LabelFrame(main3,text="Publish the book",font=("Arial",15),width=550,height=460)
            book.place(x=175,y=100)

            canvas1=Canvas(book, width=550,height=460)
            canvas1.pack(expand = 'yes', fill = 'both',anchor=NE)
            img1=PhotoImage(file='book.png')
            canvas1.create_image(280,200,image=img1)
            

            cal=Calendar(book)
            cal.place(x=10,y=180)
            date="Current Date : "+cal.get_date()
            date1=cal.get_date()
            def bb():
                  main3.destroy()
                  screen3()
            iim=PhotoImage(file="start.png")                 
            Button(main3,image=iim,border=0,command=bb).place(x=235,y=139)
            def submit_book():
                  userid=user_id.get()
                  bookid=book_id.get()
                  if (userid=="" or bookid=="" ):
                        mb.showinfo("Error","all fields are required",parent=main3)
                  else:
                        try:
                              userid=int(userid)
                              bookid=int(bookid)
                              sql=ms.connect(host='localhost',user='root',passwd='Anu@2008',database='project')
                              cur=sql.cursor()
                              cur.execute("select * from publish_data where user_id=%s and book_id=%s ",(userid,bookid))
                              data=cur.fetchall()
                              count=cur.rowcount
                              cur.execute("select date_of_issue from publish_data where user_id=%s and book_id=%s ",(userid,bookid))
                              datesql=cur.fetchall()
                              cur.execute("select email_id from publish_data where user_id=%s and book_id=%s ",(userid,bookid))
                              emailid=cur.fetchone()
                              cur.execute("delete from publish_data where user_id=%s and book_id=%s ",(userid,bookid))
                              sql.commit()
                        except Exception as a:
                              print(a)
                              mb.showinfo("Error","There can be sevral reasons for that: \n1. No Internet Connection \n2. UserID or BookID is starting with 0 or not a interger value",parent=main3)
                              
                        data='WE enter the data, \n submit the book \n date of issue:'+str(datesql)+"\n the data you entered while publishing the book is:"+str(data)
                        if count==0:
                              mb.showinfo('Error','Student id or Book id did not match')
                        else:
                              mb.showinfo("Sucess",data,parent=main3)
                              def send_mail():
                                    message=("""Subject: Verification message
Dear Student you have submitted the book to our library today.\n date of issue:"""+str(datesql)+"date of submission:"+str(date1)+"\nDetails \nUSER ID:" +str(userid)+'\nBOOK ID '+str(bookid)+"\n Hope you enjoyed the reading :) ")
                                    server=SMTP_SSL("smtp.gmail.com", 465)
                                    server.login("bharatah.dharam@gmail.com", "mybnxpnvxdqwqyax")
                                    server.sendmail("bharatah.dharam@gmail.com",emailid,message)
                                    server.quit()
                              send_mail()
                        
 
            def publish_book():
                  userid=user_id.get()
                  bookid=book_id.get()
                  emailid=email_id.get()

            #............................send mail......................................
                  try:
                        userid=int(userid)
                        bookid=int(bookid)
                        def send_mail():
                              message=("""Subject: Varification message
Dear Student you have published a book from our library today. \nWe urge you to submitted it before 7 day otherwise extra charges will be applied. \n Details \nUSER ID:""" +str(userid)+'\nBOOK ID '+str(bookid)+'\nEMAIL ID '+str(emailid)+'\nDate: '+str(date1)+"""\n Hope you will enjoy the book :) \n Happy reading.""")
                              server=SMTP_SSL("smtp.gmail.com", 465)
                              server.login("bharatah.dharam@gmail.com", "mybnxpnvxdqwqyax")
                              server.sendmail("bharatah.dharam@gmail.com",emailid,message)
                              server.quit()
                        if (userid=="" or bookid=="" or emailid==""):
                              mb.showinfo("Error","all fields are required",parent=main3)
                        else:
                              send_mail()
                              sql=ms.connect(host='localhost',user='root',password='Anu@2008',database='project')
                              cur=sql.cursor()
                              cur.execute("insert into publish_data(user_id,book_id,email_id,date_of_issue) values(%s,%s,%s,%s) ",(userid,bookid,emailid,date1))
                              sql.commit()
                              
                              mb.showinfo("Sucess","data entered",parent=main3)
                  except Exception as c:
                           print(c)
                           mb.showinfo("Error","There can be sevral reasons for that: \n1. Invalid Email Address \n2. This user has already published the book \n3. No Internet Connection \n4. UserID or BookID is starting with 0 or not a integer value",parent=main3)
                        
                        
                        
            
            Entry(book,textvariable=user_id).place(x=410,y=180)
            Entry(book,textvariable=book_id).place(x=410,y=225)
            Entry(book,textvariable=email_id).place(x=410,y=270)
            Label(book,text="Student ID",font=("Arial",15)).place(x=290,y=180)
            Label(book,text="Book ID",font=("Arial",15)).place(x=290,y=225)
            Label(book,text="Email Id",font=("Arial",15)).place(x=290,y=270)

            Label(book,text=date,font=("Arial",15)).place(x=290,y=320)
            imag3=PhotoImage(file='publish_icon.png')
            Button(book, image=imag3,width=100,height=50,border=0,command=publish_book).place(x=420,y=410)

            imag4=PhotoImage(file='submit_icon.png')
            Button(book, image=imag4,width=100,height=50,border=0,command=submit_book).place(x=30,y=410)

            
            main3.mainloop()
#................data button.........................................
      def data():
            book=Label(main3,text="Publish the book",font=("Arial",15),width=900,height=600)
            book.place(x=0,y=0)

            canvas1=Canvas(book, width=900,height=600)
            canvas1.pack(expand = 'yes', fill = 'both',anchor=NW)
            img1=PhotoImage(file='data1.png')
            canvas1.create_image(0,0,anchor=NW,image=img1)

#           # my sql connectivity......................................
            book1=LabelFrame(main3,text="Publish the book",font=("Arial",15),width=600,height=600)
            book1.place(x=248,y=150)

            sql=ms.connect(host='localhost',user='root',password='Anu@2008',database='project')
            cur=sql.cursor()
            cur.execute("select * from publish_data")
            rows=cur.fetchall()
            h=len(rows)
            sql.commit()
            frame=Frame(book1)
            frame.pack(side=LEFT,padx=8)
            tb=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height=20)
            tb.pack()
            tb.heading(1, text="User ID")
            tb.column(1,minwidth=0,width=120,stretch=NO)
            tb.heading(2, text="Book ID")
            tb.column(2,minwidth=0,width=120,stretch=NO)
            tb.heading(3, text="Email ID")
            tb.column(3,minwidth=0,width=160,stretch=NO)
            tb.heading(4, text="Date of Issue")
            tb.column(4,minwidth=0,width=120,stretch=NO)
            for i in rows:
                  tb.insert("",'end',values=i)

            def bb():
                  main3.destroy()
                  screen3()
            iim=PhotoImage(file="start.png")                 
            Button(main3,image=iim,border=0,command=bb).place(x=800,y=40)

            global userId
            userId=StringVar()
            Entry(main3,textvariable=userId).place(x=310,y=120)
            def search():
                  exit
                  
            Button(main3,text="Search",command=search).place(x=490,y=120)
            
            
            
            main3.mainloop()

            
      data1=PhotoImage(file='data.png')
      Button(main3,image=data1,width=50,height=50,border=0,command=data).place(x=780,y=450)
      publish1=PhotoImage(file='publish.png')
      Button(main3,image=publish1,width=50,height=50,border=0,command=publish).place(x=73,y=450)
  
      main3.mainloop()

def one():
      global main
      main=Tk()
      main.title("Haree Krishna Library")
      main.geometry('900x600')
      main.minsize(900,600)
      main.maxsize(900,600)
      photo = PhotoImage(file = "logo.png")
      main.iconphoto(False, photo)

#.................canvas .........................................
      canvas=Canvas(main,width=900,height=600)
      img=PhotoImage(file="bg.png")
      canvas.create_image(0,0,anchor=NW,image=img)
      canvas.pack()
#.................Button.........................
      Button(main,text="Continue as Librarian",font=('Arial',10),command=librarian).place(x=675,y=527)

      main.mainloop()

#......................... Loginuser.....................check details in server...................
def login_user():
      user_info=username_login.get()
      pass_info=password_login.get()
      if user_info=="" or pass_info=="" :
            mb.showinfo("Error","all fields are required",parent=main1)
      else:
            sql=ms.connect(host='localhost',user='root',password='Anu@2008',database='project')
            cur=sql.cursor()
            cur.execute("select name,password from owner where name=%s and password=%s ",(user_info,pass_info))
            data=cur.fetchall()
            count=cur.rowcount
            if count==0:
                  mb.showinfo('Error','Password or Username did not match')
                  main1.destroy()
                  librarian()
            else:
                  main1.destroy()
                  screen3()

#.............................user interface..................................................................      
def librarian():
      global main1
      main1=Toplevel(main)
      main1.title("enter your login details")
      main1.geometry("900x600")
      main1.minsize(900,600)
      main1.maxsize(900,600)
      photo9 = PhotoImage(file = "logo.png")
      main1.iconphoto(False, photo9)
      global username_login
      global password_login
      username_login=StringVar()
      password_login=StringVar()
       
      canvas=Canvas(main1,width=900,height=600)
      img=PhotoImage(file="login_bg.png")
      canvas.create_image(0,0,anchor=NW,image=img)
      canvas.pack()
      def log():
            login=LabelFrame(main1,text="Login",font=("Arial",15),width=460,height=420)
            login.place(x=207,y=30)

            canvas=Canvas(login, width=500,height=500)
            canvas.pack(anchor=NE)
            img=PhotoImage(file='login.png')
            canvas.create_image(270,300,image=img)


            Label(login,text=" Username").place(x=205,y=219)
            Label(login,text=" Password").place(x=205,y=255)
            Entry(login,textvariable=username_login).place(x=292,y=220)
            Entry(login,textvariable=password_login,show='*').place(x=292,y=255)
            
            imag=PhotoImage(file='loginicon.png')
            Button(main1,image=imag,width=50,height=50,border=0,command=login_user).place(x=810,y=520)
            main1.mainloop()
      log()
      main1.mainloop()


one()


                  
                       




