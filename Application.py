import tkinter as tk
import mysql.connector as sql
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk

class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Background.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Login',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 160,pady =140)
        L1 = tk.Label(border,text = 'Admin ID',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 50, y = 20)
        T1 = tk.Entry(border,width=30,bd=5)
        T1.place(x=180,y=20)
        L2 = tk.Label(border,text = 'Password',font = ('Arial bold',15),bg='#cc9c7c')
        L2.place(x = 50, y = 80)
        T2 = tk.Entry(border,width=30,show='*',bd=5)
        T2.place(x=180,y=80)

        def verify():
            try:
                with open('credential.txt','r') as f:
                    info = f.readlines()
                    i=0
                    for e in info:
                        u,p = e.split(',')
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i=1
                            break
                    if i==0:
                        messagebox.showinfo('ERROR','Please Enter correct admin id and password!!!')
            except:
                messagebox.showinfo('ERROR','Please Enter correct admin id and password!!!')

        B1 = tk.Button(border,text = 'Submit',font = ('Arial',15),bg='green',command=verify)
        B1.place(x = 150, y = 130)

        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg='deep sky blue')
            window.title('Register')
            window.geometry('470x220')
            l1 = tk.Label(window,text = 'Admin ID:',font = ('Arial',15),bg = 'deep sky blue')
            l1.place(x=10,y=10)
            t1 = tk.Entry(window,width=30,bd=5)
            t1.place(x=200,y=10)

            l2 = tk.Label(window,text = 'Password',font = ('Arial',15),bg = 'deep sky blue')
            l2.place(x=10,y=60)
            t2 = tk.Entry(window,width=30,show='*',bd=5)
            t2.place(x=200,y=60)

            l3 = tk.Label(window,text = 'Conform Password',font = ('Arial',15),bg = 'deep sky blue')
            l3.place(x=10,y=110)
            t3 = tk.Entry(window,width=30,show='*',bd=5)
            t3.place(x=200,y=110)

            def check():
                if t1.get()!='' or t2.get()!='' or t3.get()!='':
                    if t2.get()==t3.get():
                        with open('credential.txt','a') as f:
                            f.write(t1.get()+' , '+t2.get()+'\n')
                            messagebox.showinfo('Welcome','You are register successfully')
                    else:
                        messagebox.showinfo('ERROR',"Your password didn't get match!!!")
                else:
                    messagebox.showinfo('ERROR','Please fill the complete field!!!')


            b1 = tk.Button(window,text='Sign In',font=('Arial',15),bg='#ffc22a',command=check)
            b1.place(x=170,y=160)

            window.mainloop()

        B2 = tk.Button(self,text = 'Register',bg = 'dark orange',font = ('Arial',15),command=register)
        B2.place(x=650,y=10)

        #Button = tk.Button(self,text = 'Next',font = ('Arial',15),command=lambda: controller.show_frame(SecondPage))
        #Button.place(x = 650, y = 450)

class SecondPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Tailor1.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Customer Details',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 200,pady =10)

        L1 = tk.Label(border,text = 'Customer No :',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 10, y = 20)
        T1 = tk.Entry(border,width=30,bd=5)
        T1.place(x=150,y=20)
        L2 = tk.Label(border,text = 'Frist Name :',font = ('Arial bold',15),bg='#cc9c7c')
        L2.place(x = 10, y = 70)
        T2 = tk.Entry(border,width=30,bd=5)
        T2.place(x=150,y=70)
        L3 = tk.Label(border,text = 'Last Name :',font = ('Arial bold',15),bg='#cc9c7c')
        L3.place(x = 10, y = 120)
        T3 = tk.Entry(border,width=30,bd=5)
        T3.place(x=150,y=120)
        L4 = tk.Label(border,text = 'Mobile No :',font = ('Arial bold',15),bg='#cc9c7c')
        L4.place(x = 10, y = 170)
        T4 = tk.Entry(border,width=30,bd=5)
        T4.place(x=150,y=170)
        L5 = tk.Label(border,text = 'Address :',font = ('Arial bold',15),bg='#cc9c7c')
        L5.place(x = 10, y = 220)
        T5 = tk.Entry(border,width=30,bd=5)
        T5.place(x=150,y=220)
        L6 = tk.Label(border,text = 'Order Date :',font = ('Arial bold',15),bg='#cc9c7c')
        L6.place(x = 10, y = 270)
        T6 = tk.Entry(border,width=30,bd=5)
        T6.insert(0,'yyyy-mm-dd')
        T6.place(x=150,y=270)
        L7 = tk.Label(border,text = 'Delivery Date :',font = ('Arial bold',15),bg='#cc9c7c')
        L7.place(x = 10, y = 320)
        T7 = tk.Entry(border,width=30,bd=5)
        T7.insert(0,'yyyy-mm-dd')
        T7.place(x=150,y=320)



        def insert_cust():

            Cust_No=T1.get()
            C_Fname=T2.get()
            C_Lname=T3.get()
            C_Phone=T4.get()
            C_address=T5.get()
            O_date=T6.get()
            D_date=T7.get()

            try:

                con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
                cur=con.cursor()
                query="INSERT INTO Customer(Cust_No,C_Fname,C_Lname,C_PhoneNo,C_Address,OrderDate,DeliveryDate) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val=(Cust_No,C_Fname,C_Lname,C_Phone,C_address,O_date,D_date)
                cur.execute(query,val)
                con.commit()
                messagebox.showinfo("Information","Record inserted successfully")

            except Exception as e:
                print(e)
                con.rollback()
                con.close()

        B1 = tk.Button(border,text = 'Save',font = ('Arial',15),bg='light green',command=insert_cust)
        B1.place(x = 30, y = 360)
        B2 = tk.Button(border,text = 'Shirt',font = ('Arial',15),bg='deep sky blue',command=lambda: controller.show_frame(ThirdPage))
        B2.place(x = 120, y = 360)
        B3 = tk.Button(border,text = 'Pant',font = ('Arial',15),bg='dark orange',command=lambda: controller.show_frame(FourthPage))
        B3.place(x = 210, y = 360)

        B0 = tk.Button(self,text = 'Search',font = ('Arial',15),bg='deep sky blue',command=lambda: controller.show_frame(SixthPage))
        B0.place(x = 650, y = 10)

class ThirdPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Tailor1.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Shirt Measurement',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 220,pady =10)

        L0 = tk.Label(border,text = 'Customer No :',font = ('Arial bold',15),bg='#cc9c7c')
        L0.place(x = 10, y = 10)
        T0 = tk.Entry(border,width=15,bd=5)
        T0.place(x=150,y=10)

        L1 = tk.Label(border,text = 'Length :',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 10, y = 50)
        T1 = tk.Entry(border,width=15,bd=5)
        T1.place(x=150,y=50)

        L2 = tk.Label(border,text = 'Shoulder :',font = ('Arial bold',15),bg='#cc9c7c')
        L2.place(x = 10, y = 90)
        T2 = tk.Entry(border,width=15,bd=5)
        T2.place(x=150,y=90)

        L3 = tk.Label(border,text = 'Sleeves :',font = ('Arial bold',15),bg='#cc9c7c')
        L3.place(x = 10, y = 130)
        T3 = tk.Entry(border,width=15,bd=5)
        T3.place(x=150,y=130)

        L4 = tk.Label(border,text = 'Chest :',font = ('Arial bold',15),bg='#cc9c7c')
        L4.place(x = 10, y = 170)
        T4 = tk.Entry(border,width=15,bd=5)
        T4.place(x=150,y=170)

        L5 = tk.Label(border,text = 'Waist :',font = ('Arial bold',15),bg='#cc9c7c')
        L5.place(x = 10, y = 210)
        T5 = tk.Entry(border,width=15,bd=5)
        T5.place(x=150,y=210)

        L6 = tk.Label(border,text = 'Collar :',font = ('Arial bold',15),bg='#cc9c7c')
        L6.place(x = 10, y = 250)
        T6 = tk.Entry(border,width=15,bd=5)
        T6.place(x=150,y=250)

        L7 = tk.Label(border,text = 'Couf :',font = ('Arial bold',15),bg='#cc9c7c')
        L7.place(x = 10, y = 290)
        T7 = tk.Entry(border,width=15,bd=5)
        T7.place(x=150,y=290)

        def insert_shirt():

            Cust_No=T0.get()
            Length=T1.get()
            Shoulder=T2.get()
            Sleeves=T3.get()
            Chest=T4.get()
            Waist=T5.get()
            Collar=T6.get()
            Couf=T7.get()

            try:

                con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
                cur=con.cursor()
                query="INSERT INTO Shirt(Cust_No,Length,Shoulder,Sleeves,Chest,Waist,Collar,Couf) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(Cust_No,Length,Shoulder,Sleeves,Chest,Waist,Collar,Couf)
                cur.execute(query,val)
                con.commit()
                messagebox.showinfo("Information","Record inserted successfully")

            except Exception as e:
                print(e)
                con.rollback()
                con.close()

        B1 = tk.Button(border,text = 'Save',font = ('Arial',15),bg='light green',command=insert_shirt)
        B1.place(x = 10, y = 370)
        B2 = tk.Button(border,text = 'Pant',font = ('Arial',15),bg='dark orange',command=lambda: controller.show_frame(FourthPage))
        B2.place(x = 100, y = 370)
        B3 = tk.Button(border,text = 'Back',font = ('Arial',15),bg='gray',command=lambda: controller.show_frame(SecondPage))
        B3.place(x = 190, y = 370)
        B4 = tk.Button(border,text = 'Next',font = ('Arial',15),bg='blue',command=lambda: controller.show_frame(FifthPage))
        B4.place(x = 280, y = 370)

class FourthPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Tailor1.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Pant Measurement',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 220,pady =10)

        L0 = tk.Label(border,text = 'Customer No :',font = ('Arial bold',15),bg='#cc9c7c')
        L0.place(x = 10, y = 10)
        T0 = tk.Entry(border,width=15,bd=5)
        T0.place(x=150,y=10)

        L1 = tk.Label(border,text = 'Length :',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 10, y = 50)
        T1 = tk.Entry(border,width=15,bd=5)
        T1.place(x=150,y=50)

        L2 = tk.Label(border,text = 'Waist :',font = ('Arial bold',15),bg='#cc9c7c')
        L2.place(x = 10, y = 90)
        T2 = tk.Entry(border,width=15,bd=5)
        T2.place(x=150,y=90)

        L3 = tk.Label(border,text = 'Hip :',font = ('Arial bold',15),bg='#cc9c7c')
        L3.place(x = 10, y = 130)
        T3 = tk.Entry(border,width=15,bd=5)
        T3.place(x=150,y=130)

        L4 = tk.Label(border,text = 'Thigh :',font = ('Arial bold',15),bg='#cc9c7c')
        L4.place(x = 10, y = 170)
        T4 = tk.Entry(border,width=15,bd=5)
        T4.place(x=150,y=170)

        L5 = tk.Label(border,text = 'Knee :',font = ('Arial bold',15),bg='#cc9c7c')
        L5.place(x = 10, y = 210)
        T5 = tk.Entry(border,width=15,bd=5)
        T5.place(x=150,y=210)

        L6 = tk.Label(border,text = 'Bottom :',font = ('Arial bold',15),bg='#cc9c7c')
        L6.place(x = 10, y = 250)
        T6 = tk.Entry(border,width=15,bd=5)
        T6.place(x=150,y=250)

        L7 = tk.Label(border,text = 'Insame :',font = ('Arial bold',15),bg='#cc9c7c')
        L7.place(x = 10, y = 290)
        T7 = tk.Entry(border,width=15,bd=5)
        T7.place(x=150,y=290)

        def insert_Pant():

            Cust_No=T0.get()
            Length=T1.get()
            Waist=T2.get()
            Hip=T3.get()
            Thigh=T4.get()
            Knee=T5.get()
            Bottom=T6.get()
            Insame=T7.get()

            try:

                con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
                cur=con.cursor()
                query="INSERT INTO Pant(Cust_No,Length,Waist,Hip,Thigh,Knee,Bottom,Insame) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(Cust_No,Length,Waist,Hip,Thigh,Knee,Bottom,Insame)
                cur.execute(query,val)
                con.commit()
                messagebox.showinfo("Information","Record inserted successfully")

            except Exception as e:
                print(e)
                con.rollback()
                con.close()

        B1 = tk.Button(border,text = 'Save',font = ('Arial',15),bg='light green',command=insert_Pant)
        B1.place(x = 10, y = 370)
        B2 = tk.Button(border,text = 'Shirt',font = ('Arial',15),bg='deep sky blue',command=lambda: controller.show_frame(ThirdPage))
        B2.place(x = 100, y = 370)
        B3 = tk.Button(border,text = 'Back',font = ('Arial',15),bg='gray',command=lambda: controller.show_frame(SecondPage))
        B3.place(x = 190, y = 370)
        B4 = tk.Button(border,text = 'Next',font = ('Arial',15),bg='blue',command=lambda: controller.show_frame(FifthPage))
        B4.place(x = 280, y = 370)

class FifthPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Tailor1.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Order And Bill',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 220,pady =70)

        L0 = tk.Label(border,text = 'Customer No :',font = ('Arial bold',15),bg='#cc9c7c')
        L0.place(x = 10, y = 30)
        T0 = tk.Entry(border,width=15,bd=5)
        T0.place(x=180,y=30)

        L1 = tk.Label(border,text = 'Shirt Quantity :',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 10, y = 80)
        T1 = tk.Entry(border,width=15,bd=5)
        T1.place(x=180,y=80)

        L2 = tk.Label(border,text = 'Pant Quantity :',font = ('Arial bold',15),bg='#cc9c7c')
        L2.place(x = 10, y = 130)
        T2 = tk.Entry(border,width=15,bd=5)
        T2.place(x=180,y=130)

        L3 = tk.Label(border,text = 'Total Bill :',font = ('Arial bold',15),bg='#cc9c7c')
        L3.place(x = 10, y = 180)
        T3 = tk.Entry(border,width=15,bd=5)
        T3.place(x=180,y=180)

        def insert_Bill():

            Cust_No=T0.get()
            Shirt_qty=T1.get()
            Pant_qty=T2.get()
            Total_Bill=T3.get()

            try:

                con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
                cur=con.cursor()
                query="INSERT INTO Bill(Cust_No,Shirt_qty,Pant_qty,Total_Bill) VALUES (%s,%s,%s,%s)"
                val=(Cust_No,Shirt_qty,Pant_qty,Total_Bill)
                cur.execute(query,val)
                con.commit()
                messagebox.showinfo("Information","Record inserted successfully")

            except Exception as e:
                print(e)
                con.rollback()
                con.close()

        B1 = tk.Button(border,text = 'Save',font = ('Arial',15),bg='light green',command=insert_Bill)
        B1.place(x = 20, y = 240)

        Button = tk.Button(border,text = 'Home',font = ('Arial',15),bg='blue',command=lambda: controller.show_frame(SecondPage))
        Button.place(x = 200, y = 240)

        Button = tk.Button(self,text = 'BACK',font = ('Arial',15),command=lambda: controller.show_frame(FourthPage))
        Button.place(x = 0, y = 450)

class SixthPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open('Tailor1.jpg')
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        border = tk.LabelFrame(self,text='Order And Bill',bg='#cc9c7c',bd=10,font=('Arial',20))
        border.pack(fill='both',expand='yes',padx = 220,pady =60)

        L1 = tk.Label(border,text = 'Show :',font = ('Arial bold',15),bg='#cc9c7c')
        L1.place(x = 120, y = 30)

        def Cust_Details():
            window = tk.Tk()
            window.resizable(0,0)
            #window.configure(bg='deep sky blue')
            window.title('Customer Details')
            window.geometry('1450x800')

            con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
            cur=con.cursor()
            cur.execute('SELECT * FROM Customer')
            rows = cur.fetchall()

            frm = Frame(window)
            frm.pack(side=LEFT,padx=5)

            tv = ttk.Treeview(frm,columns=(1,2,3,4,5,6,7),show='headings',height='100')
            tv.pack()
            tv.heading(1, text='Customer No')
            tv.heading(2, text='First Name')
            tv.heading(3, text='Last Name')
            tv.heading(4, text='Phone No')
            tv.heading(5, text='Address')
            tv.heading(6, text='Order Date')
            tv.heading(7, text='Deliver yDate')

            for i in rows:
                tv.insert('','end',values=i)


            window.mainloop()


            #messagebox.showinfo("Information","Record inserted successfully")


        Button = tk.Button(border,text = 'Customer Details',font = ('Arial',15),bg='dark green',command=Cust_Details)
        Button.place(x = 80, y = 90)

        def Shirt_Measurement():
            window = tk.Tk()
            window.resizable(0,0)
            #window.configure(bg='deep sky blue')
            window.title('Shirt Measurement')
            window.geometry('1600x800')

            con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
            cur=con.cursor()
            cur.execute('SELECT * FROM Shirt')
            rows = cur.fetchall()

            frm = Frame(window)
            frm.pack(side=LEFT,padx=5)

            tv = ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8),show='headings',height='100')
            tv.pack()
            tv.heading(1, text='Customer No')
            tv.heading(2, text='Length')
            tv.heading(3, text='Shoulder')
            tv.heading(4, text='Sleeves')
            tv.heading(5, text='Chest')
            tv.heading(6, text='Waist')
            tv.heading(7, text='Collar')
            tv.heading(8, text='Couf')

            for i in rows:
                tv.insert('','end',values=i)


            window.mainloop()

        Button = tk.Button(border,text = 'Shirt Measurement',font = ('Arial',15),bg='dark orange',command=Shirt_Measurement)
        Button.place(x = 80, y = 150)

        def Pant_Measurement():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg='deep sky blue')
            window.title('Pant Measurement')
            window.geometry('1600x800')

            con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
            cur=con.cursor()
            cur.execute('SELECT * FROM Pant')
            rows = cur.fetchall()

            frm = Frame(window)
            frm.pack(side=LEFT,padx=5)

            tv = ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8),show='headings',height='100')
            tv.pack()
            tv.heading(1, text='Customer No')
            tv.heading(2, text='Length')
            tv.heading(3, text='Waist')
            tv.heading(4, text='Hip')
            tv.heading(5, text='Thigh')
            tv.heading(6, text='Knee')
            tv.heading(7, text='Bottom')
            tv.heading(8, text='Insame')

            for i in rows:
                tv.insert('','end',values=i)


            window.mainloop()

        Button = tk.Button(border,text = 'Pant Measurement',font = ('Arial',15),bg='blue',command=Pant_Measurement)
        Button.place(x = 80, y = 210)

        def Bill_Details():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg='deep sky blue')
            window.title('Bill Details')
            window.geometry('800x800')

            con=sql.connect(host='localhost',user='root',password='5821',database='NM_Tailor')
            cur=con.cursor()
            cur.execute('SELECT * FROM Bill')
            rows = cur.fetchall()

            frm = Frame(window)
            frm.pack(side=LEFT,padx=5)

            tv = ttk.Treeview(frm,columns=(1,2,3,4),show='headings',height='100')
            tv.pack()
            tv.heading(1, text='Customer No')
            tv.heading(2, text='Shirt_qty')
            tv.heading(3, text='Pant_qty')
            tv.heading(4, text='Bill')

            for i in rows:
                tv.insert('','end',values=i)


            window.mainloop()

        Button = tk.Button(border,text = 'Bill Details',font = ('Arial',15),bg='light blue',command=Bill_Details)
        Button.place(x = 80, y = 270)

        Button = tk.Button(self,text = 'HOME',font = ('Arial',15),command=lambda: controller.show_frame(SecondPage))
        Button.place(x = 650, y = 450)

        Button = tk.Button(self,text = 'BACK',font = ('Arial',15),command=lambda: controller.show_frame(FifthPage))
        Button.place(x = 100, y = 450)

class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0,minsize = 500)
        window.grid_columnconfigure(0,minsize = 800)
        self.frames = {}#It is for pointing current page
        for F in (FirstPage,SecondPage,ThirdPage,FourthPage,FifthPage,SixthPage):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row = 0,column = 0,sticky = 'nsew')
        self.show_frame(FirstPage)

    def show_frame(self,page):
        frame = self.frames[page]
        frame.tkraise()
        self.title('New Modern Tailor')

app = Application()
app.maxsize(800,500)
app.mainloop()
