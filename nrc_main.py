import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

class refugeewebapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage,Homepage,refugeedetails,refugeefamily,flapage,mypage,lastpage,cancelledpage):
            frame=F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="white")
        self.controller=controller
        self.controller.title('NRC')
        
        load = Image.open("bg.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="white")
        LeftFrame.place(x=400,y=250,width=470,height=300)
        l1 =tk.Label(LeftFrame, font=('Norwester',15),text="Username:",fg='black',bg='white')
        l1.grid(row=1,column=0)
        t1 =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        t1.grid(row=1,column=1,padx=6,pady=20)
        l2=tk.Label(LeftFrame, font=('Norwester',15),text="Password:",fg="black",bg="white",padx=1,)
        l2.grid(row=2,column=0)
        t2=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid",show='$')
        t2.grid(row=2,column=1,pady=6, padx=20)
        def verify():
            flag=0
            with open("cred.txt", "r") as f:
                info=f.readlines()
               
                for e in info:
                    u,p=e.split(",")
                    if u.strip()== t1.get() and p.strip()==t2.get():
                        controller.show_frame(Homepage)
                        flag=1
                        break
                    
                if flag!=1:
                    messagebox.showinfo("NRC","Your Credentials didn't match!!!")          
                    
        fs_btn=tk.Button(LeftFrame,text="Submit",font=('Norwester',15),command=verify,fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=3,column=1)
        l4 =tk.Label(LeftFrame, font=('Norwester',15),text="New User! Click Register:",fg='black',bg='white')
        l4.grid(row=4,column=0)
        
        def register():
            window=tk.Tk()
            window.title("Register")
            l1=tk.Label(window,text="User Name",font=('Norwester',15),fg='black',bg='white')
            l1.place(x=10,y=10)
            t1=tk.Entry(window,font=('Norwester',15),width =15,borderwidth=1, relief="solid")
            t1.place(x=200,y=10)
            l2=tk.Label(window,text="Password",font=('Norwester',15),fg='black',bg='white')
            l2.place(x=10,y=60)
            t2=tk.Entry(window,font=('Norwester',15),width =15,borderwidth=1, relief="solid",show='$')
            t2.place(x=200,y=60)
            l3=tk.Label(window,text="Re enter password",font=('Norwester',15),fg='black',bg='white')
            l3.place(x=10,y=110)
            t3=tk.Entry(window,font=('Norwester',15),width =15,borderwidth=1, relief="solid",show='$')
            t3.place(x=200,y=110)
            def spy():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("cred.txt","a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("NRC","Registered Successfully!!!")
                    else:
                        messagebox.showinfo("NRC","Your Password didn't match!!!")
                else:
                    messagebox.showinfo("NRC","Please provide details!!!")
                    
            b1=tk.Button(window,text='Sign in',font=('Norwester',15),fg='white',bg='#000000',command=spy)
            b1.place(x=170,y=150)
            window.geometry("470x220")
            window.mainloop()
        ls_btn=tk.Button(LeftFrame,text="Register",font=('Norwester',15),command=register,fg="#000000",bg='white',padx=1)
        ls_btn.grid(row=5,column=1)
        
class Homepage(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent,bg='#7EB1DB')
        self.contoller=controller
        
        label1=tk.Label(self,text='TABLE OF CONTENTS',font=('Norwester',35),fg='white',bg='#7EB1DB')
        label1.pack(pady=25)
        
        b_frame=tk.Frame(self,bg='#7EB1DB')  
        b_frame.pack(fill='both',expand=True)

        fs_btn=tk.Button(b_frame,text="Enter Refugee Details",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(refugeedetails),relief='solid',borderwidth=2,width=25,height=3)
        fs_btn.grid(row=3,column=2)
        fs_btn.grid(padx=25)
        fs_btn.grid(pady=50)
        fa_btn=tk.Button(b_frame,text="Enter Family Details ",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(refugeefamily),relief='solid',borderwidth=2,width=25,height=3)
        fa_btn.grid(row=4,column=2)
        fa_btn.grid(padx=25)
        fa_btn.grid(pady=50)
        cr_btn=tk.Button(b_frame,text="Enter Reason for fled",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(flapage),relief='solid',borderwidth=2,width=25,height=3)
        cr_btn.grid(row=5,column=2)
        cr_btn.grid(padx=25)
        cr_btn.grid(pady=50)
        cr1_btn=tk.Button(b_frame,text="Enter Documents Details",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(mypage),relief='solid',borderwidth=2,width=25,height=3)
        cr1_btn.grid(row=3,column=5)
        cr1_btn.grid(padx=930)
        cr1_btn.grid(pady=50)
        cr2_btn=tk.Button(b_frame,text="Enter other Details",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(lastpage),relief='solid',borderwidth=2,width=25,height=3)
        cr2_btn.grid(row=4,column=5)
        cr2_btn.grid(padx=930)
        cr2_btn.grid(pady=50)
        cr3_btn=tk.Button(b_frame,text="View Cancelled Refugees",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(cancelledpage),relief='solid',borderwidth=2,width=25,height=3)
        cr3_btn.grid(row=5,column=5)
        cr3_btn.grid(padx=930)
        cr3_btn.grid(pady=50)
        cr4_btn=tk.Button(b_frame,text="Exit",font=('Norwester',15),bg='white',fg='#2C4072',command=lambda: controller.show_frame(StartPage),relief='solid',borderwidth=2,width=25,height=3)
        cr4_btn.grid(row=90,column=2)
        cr4_btn.grid(padx=25)
        cr4_btn.grid(pady=50)
        load = Image.open("bg0.png")
        resize_image = load.resize((520, 520))
        photo=ImageTk.PhotoImage(resize_image)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=500,y=250)



class refugeedetails(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='REFUGEE DETAILS',font=('Norwester',40),fg='#2C4072',bg='#7EB1DB')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='solid',bg="#7EB1DB")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='solid',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=700,width=200,height=50)
        
        co_no =tk.Label(LeftFrame, font=('Norwester',15),text="Refugee id :",fg='black',bg='white')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_rna=tk.Label(LeftFrame, font=('Norwester',15),text="Name:",fg="black",bg="white",padx=1)
        co_rna.grid(row=3,column=0)
        co_rna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_rna_en.grid(row=3,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('Norwester',15),text="Age:",fg='black',bg='white',padx=1)
        co_age.grid(row=5,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_age_en.grid(row=5,column=1,pady=6, padx=20)
        co_nat=tk.Label(LeftFrame,font=('Norwester',15),text="Nationality:",fg='black',bg='white',padx=1)
        co_nat.grid(row=7,column=0)
        co_nat_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_nat_en.grid(row=7,column=1,pady=6, padx=20)
        co_dob=tk.Label(LeftFrame,font=('Norwester',15),text="Date of birth:",fg='black',bg='white',padx=1)
        co_dob.grid(row=9,column=0)
        co_dob_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_dob_en.grid(row=9,column=1,pady=6, padx=20)
        co_gen=tk.Label(LeftFrame,font=('Norwester',15),text="Gender:",fg='black',bg='white',padx=1)
        co_gen.grid(row=12,column=0)
        co_gen_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_gen_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            if co_no_en.get()!="" and co_rna_en.get()!="" and co_age_en.get()!="" and co_nat_en.get()!="" and co_dob_en.get()!="" and co_gen_en.get()!="":
                conn=sqlite3.connect('b.db')
                c=conn.cursor()
                c.execute("INSERT INTO refugee VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                        {
                                'f_no':co_no_en.get(),
                                'f_na':co_rna_en.get(),
                                'f_da':co_age_en.get(),
                                'f_so':co_nat_en.get(),
                                'f_de':co_dob_en.get(),
                                'f_ti':co_gen_en.get()

                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Details", "Submitted Sucessfully")
                
            else:
                    messagebox.showinfo("Refugee","Please provide details!!!")
        s_btn=tk.Button(BottomFrame,font=('Norwester',22),text='Submit',command=submit,fg='black',bg='white',padx=5)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_rna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_nat_en.delete(0,'end')
            co_dob_en.delete(0,'end')
            co_gen_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('Norwester',22),text='Reset',command=reset,fg='black',bg='white',padx=2)
        l_btn.grid(row=2,column=1)

        fli_id=tk.Label(LeftFrame,font=('Norwester',15),text='Enter the co ID to delete:',fg='black',bg='white',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        def delete():

            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE FROM refugee WHERE refugee_id ="+ fli_id_en.get())
            
            conn.commit()
            conn.close()

        delet_btn=tk.Button(BottomFrame1,font=('Norwester',22),text='Delete',command=delete,fg='black',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT *FROM refugee")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            refugeelist.insert('','end',value=num)

        def selected(event):
            viewinfo=refugeelist.focus()
            mysl=refugeelist.item(viewinfo)
            r=mysl['values']
            
            co_no_en.insert(0,r[0])
           
            co_rna_en.insert(1,r[1])
           
            co_age_en.insert(2,r[2])
            
            co_nat_en.insert(3,r[3])
            
            co_dob_en.insert(4,r[4])
           
            co_gen_en.insert(5,r[5])
          
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
   
        refugeelist= ttk.Treeview(RightFrame,height=16,column=("cono","corna","coage","conat","codob","cogen"), yscrollcommand=scrollbar.set )
        refugeelist.heading("cono",text="Refugee id")
        refugeelist.heading("corna",text="Name")
        refugeelist.heading("coage",text="Age")
        refugeelist.heading("conat",text="nat")
        refugeelist.heading("codob",text="dob")
        refugeelist.heading("cogen",text="gen")

        refugeelist['show']='headings'

        refugeelist.column("cono",width=90)
        refugeelist.column("corna",width=90)
        refugeelist.column("coage",width=90)
        refugeelist.column("conat",width=90)
        refugeelist.column("codob",width=90)
        refugeelist.column("cogen",width=90)

        refugeelist.bind('<ButtonRelease>',selected)
        refugeelist.grid(row=0,column=0,sticky='ns')

        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            refugeelist.delete(*refugeelist.get_children())
            for row in searchData(co_no_en.get(),co_rna_en.get(),co_age_en.get(),co_nat_en.get(),co_dob_en.get(),co_gen_en.get()):
                refugeelist.insert('','end',value=row)
        def searchData(refugee_id="",name="",age="",nationality="",dateofbirth="",gender=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM refugee WHERE refugee_id=? OR name=? OR age=? OR nationality=? OR dateofbirth=? OR gender=? ", \
                (refugee_id,name,age,nationality,dateofbirth,gender))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('Norwester',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=co_no_en.get()
            a=co_rna_en.get()
            m=co_age_en.get()
            e=co_nat_en.get()
            s=co_dob_en.get()
            i=co_gen_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE refugee SET name=?, age=?,nationality=?, dateofbirth=? , gender=?  WHERE refugee_id=?",(a,m,s,e,i,n))
            conn.commit()  
            conn.close()

        u_btn=tk.Button(BottomFrame3,font=('Norwester',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
            
class refugeefamily(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='FAMILY DETAILS',font=('Norwester',40),fg='#2C4072', bg='#7EB1DB')
        label2.pack()
        global sd
        
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        LeftFrame.place(x=100,y=100,width=470,height=450)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        RightFrame.place(x=700,y=100,width=760,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=650,width=200,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
        fl_no =tk.Label(LeftFrame, font=('Norwester',15),text="Refugee id:",fg='black', bg='white')
        fl_no.grid(row=1,column=0)
        fl_no_en =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        fl_no_en.grid(row=1,column=1,padx=6,pady=20)
        fl_na=tk.Label(LeftFrame, font=('Norwester',15),text="Refugee name:",fg="black",padx=1)
        fl_na.grid(row=2,column=0)
        fl_na_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_na_en.grid(row=2,column=1,pady=6, padx=20)
        fl_type=tk.Label(LeftFrame,font=('Norwester',15),text="Father name:",fg='black',padx=1)
        fl_type.grid(row=3,column=0)
        fl_type_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_type_en.grid(row=3,column=1,pady=6, padx=20)
        fl_from=tk.Label(LeftFrame,font=('Norwester',15),text="Mother name:",fg='black',padx=1)
        fl_from.grid(row=4,column=0)
        fl_from_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_from_en.grid(row=4,column=1,pady=6, padx=20)
        fl_de=tk.Label(LeftFrame,font=('Norwester',15),text="Spouse name:",fg='black',padx=1)
        fl_de.grid(row=5,column=0)
        fl_de_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_de_en.grid(row=5,column=1,pady=6, padx=20)
        fl_ca=tk.Label(LeftFrame,font=('Norwester',15),text="Number of Children:",fg='black',padx=1)
        fl_ca.grid(row=6,column=0)
        fl_ca_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_ca_en.grid(row=6,column=1,pady=6, padx=20)
        fl_da=tk.Label(LeftFrame,font=('Norwester',15),text="Permanent Address:",fg='black',padx=1)
        fl_da.grid(row=7,column=0)
        fl_da_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_da_en.grid(row=7,column=1,pady=6, padx=20)
        fl_ti=tk.Label(LeftFrame,font=('Norwester',15),text="Hometown Address:",fg='black',padx=1)
        fl_ti.grid(row=8,column=0)
        fl_ti_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fl_ti_en.grid(row=8,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO familydetails VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti,:u,:g)",
                      {
                             'f_no':fl_no_en.get(),
                             'f_na':fl_na_en.get(),
                             'f_da':fl_type_en.get(),
                             'f_so':fl_from_en.get(),
                             'f_de':fl_de_en.get(),
                             'f_ti':fl_ca_en.get(),
                             'u':fl_da_en.get(),
                             'g':fl_ti_en.get()
                             
                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('Norwester',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            fl_no_en.delete(0,'end')
            fl_na_en.delete(0,'end')
            fl_type_en.delete(0,'end')
            fl_from_en.delete(0,'end')
            fl_de_en.delete(0,'end')
            fl_ca_en.delete(0,'end')
            fl_da_en.delete(0,'end')
            fl_ti_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('Norwester',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)

        fli_id=tk.Label(LeftFrame,font=('Norwester',15),text='Enter the no of childrens to erase:',fg='black',bg='white',padx=1)
        fli_id.grid(row=12,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fli_id_en.grid(row=12,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM familydetails")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            refugeelist.insert('','end',value=num)
            
        def selected(event):
            viewinfo=refugeelist.focus()
            mysl=refugeelist.item(viewinfo)
            r=mysl['values']
            fl_no_en.insert(0,r[0])
            fl_na_en.insert(1,r[1])
            fl_type_en.insert(2,r[2])
            fl_from_en.insert(3,r[3])
            fl_de_en.insert(4,r[4])
            fl_ca_en.insert(5,r[5])
            fl_da_en.insert(6,r[6])
            fl_ti_en.insert(7,r[7]) 
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        
        refugeelist= ttk.Treeview(RightFrame, height=16,column=("fno","fna","ffrom","fto","fca","fda","fti","schedco"), yscrollcommand=scrollbar.set )
        refugeelist.heading("fno",text="Refugee id")
        refugeelist.heading("fna",text="Refugee name")
        refugeelist.heading("ffrom",text="Father name")
        refugeelist.heading("fto",text="mother name")
        refugeelist.heading("fca",text="spouse name")
        refugeelist.heading("fda",text="no of childer")
        refugeelist.heading("fti",text="permanent address")
        refugeelist.heading("schedco",text="hometownadress")

        refugeelist['show']='headings'

        refugeelist.column("fno",width=90)
        refugeelist.column("fna",width=90)
        refugeelist.column("ffrom",width=90)
        refugeelist.column("fto",width=90)
        refugeelist.column("fca",width=90)
        refugeelist.column("fda",width=90)
        refugeelist.column("fti",width=90)
        refugeelist.column("schedco",width=90)

        refugeelist.bind('<ButtonRelease>',selected)

        refugeelist.grid(row=0,column=0,sticky='ns')

        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)      

        def deleteRec():
                con=sqlite3.connect("b.db")
                cur = con.cursor()
                cur.execute("DELETE FROM familydetails WHERE no_of_childs ="+fli_id_en.get())
                con.commit()
                con.close
        delet_btn=tk.Button(BottomFrame1,font=('Norwester',22),text='Delete',command=deleteRec,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def searchDatabase():
            refugeelist.delete(*refugeelist.get_children())
            
            for row in searchData(fl_no_en.get(),fl_na_en.get(),fl_type_en.get(),fl_from_en.get(),fl_de_en.get(),fl_ca_en.get(),fl_da_en.get(),fl_ti_en.get()):
                refugeelist.insert('','end',value=row)
                
        def searchData(refugee_id="",name="",father_name="",mother_name="",souse_name="",no_of_childs="",permanent_address="",hometownaddress=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM familydetails WHERE refugee_id =? OR name=? OR father_name=? OR mother_name=? OR souse_name=? OR no_of_childs=? OR permanent_address=? OR hometownaddress=?", \
                        (refugee_id,name,father_name,mother_name,souse_name,no_of_childs,permanent_address,hometownaddress))
            rows=cur.fetchall()
            
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('Norwester',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        
        def update():
            
            n=fl_no_en.get()
            a=fl_na_en.get()
            m=fl_type_en.get()
            e=fl_from_en.get()
            s=fl_de_en.get()
            i=fl_ca_en.get()
            j=fl_da_en.get()
            k=fl_ti_en.get()
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE familydetails SET name=?, father_name=?, mother_name=?, souse_name=?,no_of_childs=?,permanent_address=?,hometownaddress=? WHERE refugee_id=? ",(a,m,e,s,i,j,k,n))
            conn.commit()
            conn.close()
        u_btn=tk.Button(BottomFrame3,font=('Norwester',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
            
class flapage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='Enter Reason for fled',font=('Norwester',40),fg='#2C4072',bg='#7EB1DB')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=650,width=200,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
        co_no =tk.Label(LeftFrame, font=('Norwester',15),text="Refugee ID:",fg='black',bg='white')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_rna=tk.Label(LeftFrame, font=('Norwester',15),text="Refugee Name:",fg="black",bg="white",padx=1)
        co_rna.grid(row=3,column=0)
        co_rna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_rna_en.grid(row=3,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('Norwester',15),text="reasons:",fg='black',bg='white',padx=1)
        co_age.grid(row=5,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_age_en.grid(row=5,column=1,pady=6, padx=20)
        co_nat=tk.Label(LeftFrame,font=('Norwester',15),text="Present Address:",fg='black',bg='white',padx=1)
        co_nat.grid(row=7,column=0)
        co_nat_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_nat_en.grid(row=7,column=1,pady=6, padx=20)
        co_dob=tk.Label(LeftFrame,font=('Norwester',15),text="Present Occupation:",fg='black',bg='white',padx=1)
        co_dob.grid(row=9,column=0)
        co_dob_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_dob_en.grid(row=9,column=1,pady=6, padx=20)
        co_gen=tk.Label(LeftFrame,font=('Norwester',15),text="Duration Of Stay:",fg='black',bg='white',padx=1)
        co_gen.grid(row=12,column=0)
        co_gen_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_gen_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO reasonsforcoming VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_rna_en.get(),
                             'f_da':co_age_en.get(),
                             'f_so':co_nat_en.get(),
                             'f_de':co_dob_en.get(),
                             'f_ti':co_gen_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('Norwester',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_rna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_nat_en.delete(0,'end')
            co_dob_en.delete(0,'end')
            co_gen_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('Norwester',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)
        
        fli_id=tk.Label(LeftFrame,font=('Norwester',15),text='Enter the duration of stay to delete:',fg='black',bg='white',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        def delete():
             
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from reasonsforcoming WHERE duration_of_stay="+ fli_id_en.get())       
            
            conn.commit()
            conn.close()
        
        delet_btn=tk.Button(BottomFrame1,font=('Norwester',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM reasonsforcoming")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            refugeelist.insert('','end',value=num)

        def selected(event):
            viewinfo=refugeelist.focus()
            mysl=refugeelist.item(viewinfo)
            r=mysl['values']
            
            co_no_en.insert(0,r[0])
           
            co_rna_en.insert(1,r[1])
           
            co_age_en.insert(2,r[2])

            co_nat_en.insert(3,r[3])
            
            co_dob_en.insert(4,r[4])
           
            co_gen_en.insert(5,r[5])
        
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')

        refugeelist= ttk.Treeview(RightFrame, height=16,column=("cono","corna","coage","conat","codob","cogen"), yscrollcommand=scrollbar.set )
        refugeelist.heading("cono",text="Refugee id")
        refugeelist.heading("corna",text="Refugee name")
        refugeelist.heading("coage",text="Reason for arrival")
        refugeelist.heading("conat",text="Present address")
        refugeelist.heading("codob",text="Present Occupation")
        refugeelist.heading("cogen",text="Duration of Stay")

        refugeelist['show']='headings'

        refugeelist.column("cono",width=90)
        refugeelist.column("corna",width=90)
        refugeelist.column("coage",width=90)
        refugeelist.column("conat",width=90)
        refugeelist.column("codob",width=90)
        refugeelist.column("cogen",width=90)
        refugeelist.bind('<ButtonRelease>',selected)

        refugeelist.grid(row=0,column=0,sticky='ns')
 
        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            refugeelist.delete(*refugeelist.get_children())
            for row in searchData(co_no_en.get(),co_rna_en.get(),co_age_en.get(),co_nat_en.get(),co_dob_en.get(),co_gen_en.get()):
                refugeelist.insert('','end',value=row)
        def searchData(refugee_id="",name="",reason="",present_address="",present_occupation="",duration_of_stay=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT  *FROM reasonsforcoming WHERE refugee_id=? OR name=? OR reason=? OR present_address=? OR present_occupation=? OR duration_of_stay=? ", \
                (refugee_id,name,reason,present_address,present_occupation,duration_of_stay))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('Norwester',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        
        def update():
            n=co_no_en.get()
            a=co_rna_en.get()
            m=co_age_en.get()
            e=co_nat_en.get()
            s=co_dob_en.get()
            i=co_gen_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE reasonsforcoming SET name=?, reason=?, present_address=?, present_occupation=?, duration_of_stay=?  WHERE refugee_id=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()

        u_btn=tk.Button(BottomFrame3,font=('Norwester',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)

class mypage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='Enter Documents Details',font=('Norwester',40),fg='#2C4072',bg='#7EB1DB')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        RightFrame.place(x=700,y=100,width=640,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=650,width=200,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
        co_no =tk.Label(LeftFrame, font=('Norwester',15),text="Refugee ID:",fg='black',bg='white')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('Norwester',15),text="Refugee name:",fg="black",bg="white",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('Norwester',15),text="NRC Code:",fg='black',bg='white',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('Norwester',15),text="Caste:",fg='black',bg='white',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('Norwester',15),text="Criminal cases:",fg='black',bg='white',padx=1)
        co_age.grid(row=9,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_age_en.grid(row=9,column=1,pady=6, padx=20)
        co_assf=tk.Label(LeftFrame,font=('Norwester',15),text="Bank account no:",fg='black',bg='white',padx=1)
        co_assf.grid(row=12,column=0)
        co_assf_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_assf_en.grid(row=12,column=1,pady=6, padx=20)
        
        co_email=tk.Label(LeftFrame,font=('Norwester',15),text="religon:",fg='black',bg='white',padx=1)
        co_email.grid(row=13,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_email_en.grid(row=13,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO documents VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:fc,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_fna_en.get(),
                             'f_da':co_lna_en.get(),
                             'f_so':co_age_en.get(),
                             'f_de':co_cno_en.get(),
                             'fc':co_assf_en.get(),
                             'f_ti':co_email_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('Norwester',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_assf_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('Norwester',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)
    
        fli_id=tk.Label(LeftFrame,font=('Norwester',15),text='Enter the NRC_code to delete:',fg='black',bg='white',padx=1)
        fli_id.grid(row=15,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fli_id_en.grid(row=15,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)

        def delete():

            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from documents WHERE nrc_code="+ fli_id_en.get())     
            
            conn.commit()
            conn.close()
        
        delet_btn=tk.Button(BottomFrame1,font=('Norwester',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM documents")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            refugeelist.insert('','end',value=num)
        
        def selected(event):
            viewinfo=refugeelist.focus()
            mysl=refugeelist.item(viewinfo)
            r=mysl['values']
            
            co_no_en.insert(0,r[0])
          
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])
            
            co_cno_en.insert(4,r[4])
            
            co_age_en.insert(3,r[3])
            
            co_assf_en.insert(5,r[5])
            
            co_email_en.insert(6,r[6])
             
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        
        refugeelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coass","coemail"), yscrollcommand=scrollbar.set )
        refugeelist.heading("coid",text="refugee Id")
        refugeelist.heading("cofna",text="Name")
        refugeelist.heading("colna",text="NRC_code")
        refugeelist.heading("cocono",text="Caste")
        refugeelist.heading("coag",text="Criminal_records")
        refugeelist.heading("coass",text="Bnak_acc")
        refugeelist.heading("coemail",text="Religon")
        refugeelist['show']='headings'

        refugeelist.column("coid",width=90)
        refugeelist.column("cofna",width=90)
        refugeelist.column("colna",width=90)
        refugeelist.column("cocono",width=90)
        refugeelist.column("coag",width=90)
        refugeelist.column("coass",width=90)
        refugeelist.column("coemail",width=9)
        refugeelist.bind('<ButtonRelease>',selected)

        refugeelist.grid(row=0,column=0,sticky='ns')

        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            refugeelist.delete(*refugeelist.get_children())
            for row in searchData(co_no_en.get(),co_fna_en.get(),co_lna_en.get(),co_cno_en.get(),co_age_en.get(),co_assf_en.get(),co_email_en.get()):
                refugeelist.insert('','end',value=row)
        def searchData(refugee_id="",name="",nrc_code="",caste="",criminal_records="",bank_acc="",religon=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM documents WHERE refugee_id=? OR name=? OR nrc_code=? OR caste=? OR criminal_records=? OR bank_acc=? OR religon=?", \
                (refugee_id,name,nrc_code,caste,criminal_records,bank_acc,religon))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('Norwester',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=co_no_en.get()
            a=co_fna_en.get()
            m=co_lna_en.get()
            e=co_cno_en.get()
            s=co_age_en.get()
            l=co_assf_en.get()
            i=co_email_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE documents SET name=?, nrc_code=?, caste=?, criminal_records=?,bank_acc=?, religon=?  WHERE refugee_id=?",(a,m,e,l,s,i,n))
            conn.commit()
            conn.close()

        u_btn=tk.Button(BottomFrame3,font=('Norwester',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)

class lastpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='Enter Personal Identification Details',font=('Norwester',40),fg='#2C4072',bg='#7EB1DB')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
    
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=650,width=200,height=50)
        
        co_no =tk.Label(LeftFrame, font=('Norwester',15),text="refugee_id:",fg='black',bg='white')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('Norwester',15),width =15,borderwidth=1, relief="solid")
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('Norwester',15),text="References:",fg="black",bg="white",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('Norwester',15),text="Relationship:",fg='black',bg='white',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('Norwester',15),text="Houseless:",fg='black',bg='white',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('Norwester',15),text="Medical records:",fg='black',bg='white',padx=1)
        co_age.grid(row=9,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_age_en.grid(row=9,column=1,pady=6, padx=20)
        co_email=tk.Label(LeftFrame,font=('Norwester',15),text="vis_dist_mark:",fg='black',bg='white',padx=1)
        co_email.grid(row=12,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        co_email_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO others VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_fna_en.get(),
                             'f_da':co_lna_en.get(),
                             'f_so':co_cno_en.get(),
                             'f_de':co_age_en.get(),
                             'f_ti':co_email_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('Norwester',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('Norwester',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)

        fli_id=tk.Label(LeftFrame,font=('Norwester',15),text='Enter the medical_records to delete:',fg='black',bg='white',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('Norwester',15),width=15,borderwidth=1, relief="solid")
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        def delete():
  
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from others WHERE medical_records= "+fli_id_en.get())          
            
            conn.commit()
            conn.close()
        
        delet_btn=tk.Button(BottomFrame1,font=('Norwester',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM others")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            refugeelist.insert('','end',value=num)
    
        def selected(event):
            viewinfo=refugeelist.focus()
            mysl=refugeelist.item(viewinfo)
            r=mysl['values']
            
            co_no_en.insert(0,r[0])
           
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])

            co_cno_en.insert(3,r[3])
            
            co_age_en.insert(4,r[4])
           
            co_email_en.insert(5,r[5])
              
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        
        refugeelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        refugeelist.heading("coid",text="Refugee id")
        refugeelist.heading("cofna",text="References")
        refugeelist.heading("colna",text="Relationship ")
        refugeelist.heading("cocono",text="houseless")
        refugeelist.heading("coag",text="medical records")
        refugeelist.heading("coemail",text="vis_dis_mark")

        refugeelist['show']='headings'

        refugeelist.column("coid",width=90)
        refugeelist.column("cofna",width=90)
        refugeelist.column("colna",width=90)
        refugeelist.column("cocono",width=90)
        refugeelist.column("coag",width=90)
        refugeelist.column("coemail",width=90)

        refugeelist.bind('<ButtonRelease>',selected)

        refugeelist.grid(row=0,column=0,sticky='ns')

        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            refugeelist.delete(*refugeelist.get_children())
            for row in searchData(co_no_en.get(),co_fna_en.get(),co_lna_en.get(),co_cno_en.get(),co_age_en.get(),co_email_en.get()):
                refugeelist.insert('','end',value=row)
        def searchData(refugee_id="",name="",physically_disabled="",houseless="",medical_records="",vis_din_mark=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM others WHERE refugee_id=? OR name=? OR physically_disabled=? OR houseless=? OR medical_records=? OR vis_din_mark=? ", \
                (refugee_id,name,physically_disabled,houseless,medical_records,vis_din_mark))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('Norwester',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=co_no_en.get()
            a=co_fna_en.get()
            m=co_lna_en.get()
            e=co_cno_en.get()
            s=co_age_en.get()
            i=co_email_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE others SET  name=?, physically_disabled=?, houseless=?,medical_records=? ,vis_din_mark=?  WHERE refugee_id=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
    
        u_btn=tk.Button(BottomFrame3,font=('Norwester',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)

class cancelledpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#7EB1DB')

        load = Image.open("bg2.png")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)

        label2=tk.Label(self,text='Cancelled Refugee ID',font=('Norwester',40),fg='#2C4072',bg='#7EB1DB')
        label2.pack()
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        RightFrame.place(x=500,y=100,width=560,height=370)
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        BottomFrame2=tk.Frame(self,bd=1,relief='ridge',bg="#7EB1DB")
        BottomFrame2.place(x=600,y=550,width=320,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#7EB1DB")
        BottomFrame5.place(x=600,y=650,width=200,height=50)
        
        refugeelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coass","coemail"), yscrollcommand=scrollbar.set )
        refugeelist.heading("coid",text="Cancelled Refugee_id")
        refugeelist.heading("cofna",text="name")
        refugeelist.heading("colna",text="age")
        refugeelist.heading("cocono",text="naqtionality")
        refugeelist.heading("coag",text="dateofbirth")
        refugeelist.heading("coass",text="gender")
        
        refugeelist['show']='headings'

        refugeelist.column("coid",width=90)
        refugeelist.column("cofna",width=90)
        refugeelist.column("colna",width=90)
        refugeelist.column("cocono",width=90)
        refugeelist.column("coag",width=90)
        refugeelist.column("coass",width=90)
        
        refugeelist.grid(row=0,column=0,sticky='ns')
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM DELETED_R")
            row =cur.fetchall()
            refugeelist.delete(*refugeelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            refugeelist.insert('','end',value=num)
        d_btn=tk.Button(BottomFrame2,font=('Norwester',22),text='View Cancelled refugees',command=viewData,fg='black',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        fs_btn=tk.Button(BottomFrame5,text="Back to Contents",font=('Norwester',18),command=lambda: controller.show_frame(Homepage),fg="black",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)     
       
app=refugeewebapp()
app.mainloop()