from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class course:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1200x600+200+180")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="COURSE DETAILS",bg="#128cc9",fg="white",font=("serif",10,"bold")).place(x=20,y=10,width=1160,height=40)
        course=Label(self.root,text="COURSE NAME",bg="white",font=("serif",10,"bold")).place(x=10,y=70,width=120,height=30)
        duration=Label(self.root,text="DURATION",bg="white",font=("serif",10,"bold")).place(x=10,y=120,width=120,height=30)
        charges=Label(self.root,text="CHARGES",bg="white",font=("serif",10,"bold")).place(x=10,y=170,width=120,height=30)
        description=Label(self.root,text="DESCRIPTION",bg="white",font=("serif",10,"bold")).place(x=10,y=220,width=120,height=30)

        
        self.course_entry=StringVar()
        self.duration_entry=StringVar()
        self.charges_entry=StringVar()
        
        self.c_e=Entry(self.root,textvariable=self.course_entry,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        self.c_e.place(x=200,y=70,width=200,height=30)
        self.d_e=Entry(self.root,textvariable=self.duration_entry,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=200,y=120,width=200,height=30)
        self.ch_e=Entry(self.root,textvariable=self.charges_entry,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=200,y=170,width=200,height=30)

        self.description=Text(self.root,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        self.description.place(x=200,y=220,width=400,height=150)

        self.b1=Button(self.root,text="SAVE",font=("serif",15,"bold"),bg="#44b5db",fg="white",cursor="hand2",command=self.insert).place(x=130,y=450,width=100,height=40)
        self.b2=Button(self.root,text="UPDATE",font=("serif",15,"bold"),bg="#77d986",fg="white",cursor="hand2",command=self.update).place(x=250,y=450,width=100,height=40)
        self.b3=Button(self.root,text="DELETE",font=("serif",15,"bold"),bg="#d65f47",fg="white",cursor="hand2",comman=self.delete).place(x=370,y=450,width=100,height=40)
        self.b4=Button(self.root,text="CLEAR",font=("serif",15,"bold"),bg="#86acdb",fg="white",cursor="hand2",command=self.clear).place(x=490,y=450,width=100,height=40)
        
        self.c_n=Label(self.root,text="COURSE NAME",bg="white",font=("serif",10,"bold")).place(x=700,y=70,width=100,height=30)
        self.c_entry=StringVar()
        self.c_entry1=Entry(self.root,textvariable=self.c_entry,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=810,y=70,width=150,height=30)
        self.search=Button(self.root,text="SEARCH",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.search).place(x=980,y=60,width=90,height=40)
        self.frame=Frame(self.root,border=2,relief=RIDGE)
        self.frame.place(x=700,y=120,width=470,height=400)
        
        scrolly=Scrollbar(self.frame,orient=VERTICAL)
        scrollx=Scrollbar(self.frame,orient=HORIZONTAL)


        self.course_table=ttk.Treeview(self.frame,columns=("CID","COURSE","DURATION","CHARGES","DESCRIPTION"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)


        self.course_table.heading("CID",text="COURSEID")
        self.course_table.heading("COURSE",text="COURSE")
        self.course_table.heading("DURATION",text="DURATION")
        self.course_table.heading("CHARGES",text="CHARGES")
        self.course_table.heading("DESCRIPTION",text="DESCRIPTION")
        
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table["show"]='headings'
        self.course_table.column("CID",width=90)
        self.course_table.column("COURSE",width=90)
        self.course_table.column("DURATION",width=90)
        self.course_table.column("CHARGES",width=90)
        self.course_table.column("DESCRIPTION",width=300)
        self.show()
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        

    def get_data(self,ev):
        self.c_e.config(state='readonly')
       
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content['values']
        self.course_entry.set(row[1])
        self.duration_entry.set(row[2])
        self.charges_entry.set(row[3])
        self.description.delete("1.0",END)
        self.description.insert(END,row[4])
        

    def insert(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.course_entry.get()=="":
                messagebox.showerror("Error", "coursename is required",parent=self.root)
            else:
                
               
                cur.execute("select * from course  where coursename=%s",(self.course_entry.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","course is already existed",parent=self.root)
                else:
                    cur.execute("insert into course (coursename,duration,charges,description) values(%s,%s,%s,%s)",(
                        self.course_entry.get(),
                        self.duration_entry.get(),
                        self.charges_entry.get(),
                        self.description.get("1.0",END)
                    ))  
                    mydb.commit() 
                    messagebox.showinfo("success","the details are inserted successfully",parent=self.root)
                    self.show()         
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    def update(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.course_entry.get()=="":
                messagebox.showerror("Error", "coursename is required",parent=self.root)
            else:
                
               
                cur.execute("select * from course  where coursename=%s",(self.course_entry.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select course from the list",parent=self.root)
                else:
                    cur.execute("update course set duration=%s,charges=%s,description=%s where coursename=%s ",(
                        
                        self.duration_entry.get(),
                        self.charges_entry.get(),
                        self.description.get("1.0",END),
                        self.course_entry.get()
                    ))  
                    mydb.commit() 
                    messagebox.showinfo("success","the details are updated successfully",parent=self.root)
                    self.show()         
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    
    


    def show(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    def clear(self):
        self.show()
        self.course_entry.set("")
        self.duration_entry.set("")
        self.charges_entry.set("")
        self.c_entry.set("")

        self.description.delete("1.0",END)
        self.c_e.config(state=NORMAL)
    def delete(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.course_entry.get()=="":
                messagebox.showerror("Error", "coursename is required",parent=self.root)
            else:
                
               
                cur.execute("select * from course  where coursename=%s",(self.course_entry.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","no row selected",parent=self.root)
                else:
                    op=messagebox.askyesnocancel("confirm","do you really want to delete",parent=self.root)
                    if (op==True):
                        cur.execute("delete from course where  coursename=%s ",(
                        
                       
                        self.course_entry.get(),

                        ))
                        
                        messagebox.showinfo("success","the course is deleted successfully",parent=self.root)
                        self.clear()
                    

                    mydb.commit() 
                    
                    self.show()         
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root) 
    def search(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute(f"select * from course where coursename LIKE '%{self.c_entry.get()}%'")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
                

            
            mydb.commit()
                    



        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")

    
        
        
    
    
if __name__=="__main__":
    root=Tk()
    obj=course(root)
    root.mainloop()