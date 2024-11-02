from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class student:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1200x600+200+180")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="Student Details",bg="#128cc9",fg="white",font=("serif",10,"bold")).place(x=10,y=10,width=1150,height=40)
        
        self.roll_no=Label(self.root,text="Roll N0",bg="white",fg="black",font=("serif",10,"bold")).place(x=0,y=70,width=100,height=30)
        self.dateofbirth=Label(self.root,text="D.O.B(dd-mm-yy)",bg="white",fg="black",font=("serif",10,"bold")).place(x=330,y=70,width=120,height=30)
        self.name=Label(self.root,text="Name",bg="white",fg="black",font=("serif",10,"bold")).place(x=10,y=120,width=100,height=30)
        self.number=Label(self.root,text="Contact No",bg="white",fg="black",font=("serif",10,"bold")).place(x=330,y=120,width=100,height=30)
        self.email=Label(self.root,text="Email",bg="white",fg="black",font=("serif",10,"bold")).place(x=10,y=170,width=100,height=30)
        self.select_course=Label(self.root,text="Select Course",bg="white",fg="black",font=("serif",10,"bold")).place(x=330,y=170,width=100,height=30)
        self.gender=Label(self.root,text="Gender",bg="white",fg="black",font=("serif",10,"bold")).place(x=10,y=220,width=100,height=30)
        self.admission_date=Label(self.root,text="Admission Date",bg="white",fg="black",font=("serif",10,"bold")).place(x=330,y=220,width=100,height=30)
        self.state=Label(self.root,text="State",bg="white",fg="black",font=("serif",10,"bold")).place(x=50,y=280,width=60,height=30)
        self.city=Label(self.root,text="City",bg="white",fg="black",font=("serif",10,"bold")).place(x=250,y=280,width=60,height=30)
        self.pincode=Label(self.root,text="PinCode",bg="white",fg="black",font=("serif",10,"bold")).place(x=450,y=280,width=60,height=30)
        self.address=Label(self.root,text="Address",bg="white",fg="black",font=("serif",10,"bold")).place(x=10,y=330,width=100,height=30)

        self.roll1=StringVar()
        self.roll2=Entry(self.root,textvariable=self.roll1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=150,y=70,width=150,height=30)
        self.dateofbirth1=StringVar()
        self.dateofbirth2=Entry(self.root,textvariable=self.dateofbirth1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=470,y=70,width=150,height=30)
        self.name1=StringVar()
        self.name2=Entry(self.root,textvariable=self.name1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=150,y=120,width=150,height=30)
    
        self.number1=StringVar()
        self.number2=Entry(self.root,textvariable=self.number1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=470,y=120,width=150,height=30)
    
        self.email1=StringVar()
        self.email2=Entry(self.root,textvariable=self.email1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=150,y=170,width=150,height=30)
        self.list=[]
        self.fetch_course()
        self.admission_date1=StringVar()
        self.admission_date2=Entry(self.root,textvariable=self.admission_date1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=470,y=220,width=150,height=30)
        self.select_course1=ttk.Combobox(self.root,textvariable=self.select_course,font=("serif",10,"bold"),values=self.list,state='readonly',justify=CENTER)
        self.select_course1.set("Select")
        self.select_course1.place(x=470,y=170,width=150,height=30)

        self.gender1=ttk.Combobox(self.root,textvariable=self.gender,font=("serif",10,"bold"),values=("MALE","FEMALE","OTHER"),state='readonly',justify=CENTER)
        self.gender1.place(x=150,y=220,width=150,height=30)
        self.gender1.current(0)
        self.state1=StringVar()
        self.state2=Entry(self.root,textvariable=self.state1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=120,y=280,width=100,height=30)

        self.city1=StringVar() 
        self.city2=Entry(self.root,textvariable=self.city1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=310,y=280,width=100,height=30)

        self.pincode1=StringVar()
        self.pincode2=Entry(self.root,textvariable=self.pincode1,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=520,y=280,width=100,height=30)
        self.address1=Text(self.root,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        self.address1.place(x=130,y=330,width=490,height=100)
        #==================================================================================#
        
        self.b1=Button(self.root,text="SAVE",font=("serif",15,"bold"),bg="#44b5db",fg="white",cursor="hand2",command=self.insert).place(x=130,y=450,width=100,height=40)
        self.b2=Button(self.root,text="UPDATE",font=("serif",15,"bold"),bg="#77d986",fg="white",cursor="hand2",command=self.update).place(x=250,y=450,width=100,height=40)
        self.b3=Button(self.root,text="DELETE",font=("serif",15,"bold"),bg="#d65f47",fg="white",cursor="hand2",comman=self.delete).place(x=370,y=450,width=100,height=40)
        self.b4=Button(self.root,text="CLEAR",font=("serif",15,"bold"),bg="#86acdb",fg="white",cursor="hand2",command=self.clear).place(x=490,y=450,width=100,height=40)
        
        self.c_n=Label(self.root,text="Roll No ",bg="white",font=("serif",10,"bold")).place(x=700,y=70,width=100,height=30)
        self.c_entry=StringVar()
        self.c_entry1=Entry(self.root,textvariable=self.c_entry,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=810,y=70,width=150,height=30)
        self.search=Button(self.root,text="SEARCH",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.search).place(x=980,y=60,width=90,height=40)
        self.frame=Frame(self.root,border=2,relief=RIDGE)
        self.frame.place(x=700,y=120,width=470,height=400)
        
        scrolly=Scrollbar(self.frame,orient=VERTICAL)
        scrollx=Scrollbar(self.frame,orient=HORIZONTAL)

        #=============================================================================
        self.course_table=ttk.Treeview(self.frame,columns=("ROLL NO","NAME","EMAIL","GENDER","DATE OF BIRTH","CONTACT NO","ADMISSION","COURSE","STATE","CITY","PINCODE","ADDRESS"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)


        self.course_table.heading("ROLL NO",text="ROLL NO")
        self.course_table.heading("NAME",text="NAME")

        self.course_table.heading("EMAIL",text="EMAIL")
        self.course_table.heading("GENDER",text="GENDER")
        self.course_table.heading("DATE OF BIRTH",text="DATE OF BIRTH")
        self.course_table.heading("CONTACT NO",text="CONTACT NO")
        self.course_table.heading("ADMISSION",text="ADMISSION")
        self.course_table.heading("COURSE",text="COURSE")
        self.course_table.heading("STATE",text="STATE")
        self.course_table.heading("CITY",text="CITY")
        self.course_table.heading("PINCODE",text="PINCODE")
        self.course_table.heading("ADDRESS",text="ADDRESS")
        
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table["show"]='headings'
        self.course_table.column("ROLL NO",width=90)
        self.course_table.column("NAME",width=90)
        self.course_table.column("EMAIL",width=90)
        self.course_table.column("GENDER",width=90)
        self.course_table.column("DATE OF BIRTH",width=90)
        self.course_table.column("CONTACT NO",width=90)
        self.course_table.column("ADMISSION",width=90)
        self.course_table.column("COURSE",width=90)
        self.course_table.column("STATE",width=90)
        self.course_table.column("CITY",width=90)
        self.course_table.column("PINCODE",width=90)
        self.course_table.column("ADDRESS",width=90)
        self.show()
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        
       
        

    def insert(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.roll1.get()=="":
                messagebox.showerror("Error", "rollno is required",parent=self.root)
            else:
                
               
                cur.execute("select * from student  where rollno=%s",(self.roll1.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","student is already existed",parent=self.root)
                else:
                    cur.execute("insert into student (rollno,name,email,gender,dateofbirth,contactno,admission,course,state,city,pincode,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.roll1.get(),
                        self.name1.get(),
                        self.email1.get(),
                        self.gender1.get(),
                        self.dateofbirth1.get(),
                        self.number1.get(),
                        self.admission_date1.get(),
                        self.select_course1.get(),
                        self.state1.get(),
                        self.city1.get(),
                        self.pincode1.get(),
                        self.address1.get("1.0",END)
                    ))  
                    mydb.commit() 
                    messagebox.showinfo("success","the details are inserted successfully",parent=self.root)
                    self.show()         
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    
    

    def show(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)

    def fetch_course(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute("select coursename from course")
            rows=cur.fetchall()
            
            if len(rows)>0:
                for row in rows:
                    self.list.append(row[0])
              


        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    
   
    def search(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute(f"select * from student where rollno LIKE '%{self.c_entry.get()}%'")
            rows=cur.fetchall()
            if rows!=None:
                self.course_table.delete(*self.course_table.get_children())
                for row in rows:
                    self.course_table.insert('',END,values=row)
            elif rows==None:
                messagebox.showerror("error","No record found",parent=self.root)

                

            
            mydb.commit()

            
            
                    



        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")
    def update(self):
            mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
            cur=mydb.cursor()
            try:
                if self.roll1.get()=="":
                    messagebox.showerror("Error", "rollno is required",parent=self.root)
                else:
                    
                
                    cur.execute("select * from student  where rollno=%s",(self.roll1.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","select student from the list",parent=self.root)
                    else:
                        cur.execute("update student set name=%s,email=%s,gender=%s,dateofbirth=%s,contactno=%s,admission=%s,course=%s,state=%s,city=%s,pincode=%s,address=%s where rollno=%s ",(                        
                        self.name1.get(),
                        self.email1.get(),
                        self.gender1.get(),
                        self.dateofbirth1.get(),
                        self.number1.get(),
                        self.admission_date1.get(),
                        self.select_course1.get(),
                        self.state1.get(),
                        self.city1.get(),
                        self.pincode1.get(),
                        self.address1.get("1.0",END),
                        self.roll1.get(),
                        )) 
                        mydb.commit() 
                        messagebox.showinfo("success","the details are updated successfully",parent=self.root)
                        self.show()         
            except Exception as ex:
                messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
        
    
    def delete(self):
        mydb = mysql.connector.connect(host='localhost', password='varsha', user='root', database="firstproject")
        cur = mydb.cursor()
    
        if self.roll1.get() == "":
            messagebox.showerror("Error", "Roll No is required", parent=self.root)
        else:
            cur.execute("select * from student where rollno = %s", (self.roll1.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please select the student", parent=self.root)
            else:
                op = messagebox.askyesnocancel("Confirm", "Do you really want to delete?", parent=self.root)
                if op:
                    cur.execute("delete from student where rollno = %s", (self.roll1.get(),))
                    mydb.commit()
                    messagebox.showinfo("Success", "The student was deleted successfully", parent=self.root)
                    self.clear()
                    self.show()  # Refresh the table to reflect the changes
        
   
        
    def clear(self):
        self.show()
        self.roll1.set(""),
        self.name1.set(""),
        self.email1.set(""),
        self.gender1.set("SELECT"),
        self.dateofbirth1.set(""),
        self.number1.set(""),
        self.admission_date1.set(""),
        self.select_course1.set("SELECT"),
        self.state1.set(""),
        self.city1.set(""),
        self.pincode1.set(""),
        self.address1.delete("1.0",END)
        self.c_entry.set("")
        self.roll2.config(state=NORMAL)
        


        
    def get_data(self,ev):

        
        r=self.course_table.focus()

        content=self.course_table.item(r)
        row=content['values']
        self.roll1.set(row[0]),
        self.name1.set(row[1]),
        self.email1.set(row[2]),
        self.gender1.set(row[3]),
        self.dateofbirth1.set(row[4]),
        self.number1.set(row[5]),
        self.admission_date1.set(row[6]),
        self.select_course1.set(row[7]),
        self.state1.set(row[8]),
        self.city1.set(row[9]),
        self.pincode1.set(row[10]),
        self.address1.delete("1.0",END)
        self.address1.insert(END,row[11])
        

    
        




if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()