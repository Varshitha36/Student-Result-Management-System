from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class result:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1200x600+200+180")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_course()
        title=Label(self.root,text="Manage student results",bg="#128cc9").place(x=20,y=10,width=1150,height=50)
        r_select=Label(self.root,text="SELECT STUDENT",bg="white",font=("serif",10,"bold")).place(x=20,y=70,width=120,height=50)
        r_name=Label(self.root,text="NAME",bg="white",font=("serif",10,"bold")).place(x=20,y=140,width=120,height=50)
        r_course=Label(self.root,text="COURSE",bg="white",font=("serif",10,"bold")).place(x=20,y=210,width=120,height=50)
        r_marks_ob=Label(self.root,text="MARKS OBTAINED ",bg="white",font=("serif",10,"bold")).place(x=20,y=280,width=120,height=50)
        r_full_marks=Label(self.root,text="FULL MARKS",bg="white",font=("serif",10,"bold")).place(x=20,y=350,width=120,height=50)
        self.select_student=ttk.Combobox(self.root,textvariable=self.var_roll,font=("serif",10,"bold"),values=self.roll_list,state='readonly',justify=CENTER)
        
        self.select_student.place(x=280,y=80,width=200,height=30)
        self.select_student.set("Select")
        self.search=Button(self.root,text="SEARCH",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.search1).place(x=500,y=70,width=90,height=40)
        self.var_roll1=Entry(self.root,textvariable=self.var_name,border=1,bg="#d9d8d7",font=("serif",10,"bold"),state='readonly').place(x=280,y=140,width=310,height=30)
        self.var_course1=Entry(self.root,textvariable=self.var_course,border=1,bg="#d9d8d7",font=("serif",10,"bold"),state='readonly').place(x=280,y=210,width=310,height=30)
        self.var_marks1=Entry(self.root,textvariable=self.var_marks,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=280,y=280,width=310,height=30)
        self.var_full_marks1=Entry(self.root,textvariable=self.var_full_marks,border=1,bg="#d9d8d7",font=("serif",10,"bold")).place(x=280,y=350,width=310,height=30)
        self.submit1=Button(self.root,text="SUBMIT",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.insert).place(x=150,y=450,width=100,height=40)
        self.clear1=Button(self.root,text="CLEAR",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.clear).place(x=290,y=450,width=100,height=40)

        self.image1=Image.open("resut.PNG")
        self.image1=self.image1.resize((500,300))
        self.image1=ImageTk.PhotoImage(self.image1)
        self.title=Label(self.root,image=self.image1,font=("serif",30,"bold"),bg="black").place(x=650,y=100,height=400)


    def fetch_course(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            cur.execute("select rollno from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
                

            
            mydb.commit()
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")
    def search1(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            roll_no = self.var_roll.get()  # Get the roll number
            cur.execute("SELECT name, course FROM student WHERE rollno=%s", (roll_no,))
            rows=cur.fetchone()
            
            if rows!=None:
                self.var_name.set(rows[0])
                self.var_course.set(rows [1])
            else:
                messagebox.showerror("error","No record found",parent=self.root)

                

            
            mydb.commit()

            
            
                    



        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")


    def insert(self):
        try:
            # Debugging: Check if any variable is None
            if self.var_roll is None:
                raise ValueError("var_roll is None")
            if self.var_name is None:
                raise ValueError("var_name is None")
            if self.var_course is None:
                raise ValueError("var_course is None")
            if self.var_marks is None:
                raise ValueError("var_marks is None")
            if self.var_full_marks is None:
                raise ValueError("var_full_marks is None")

            # Check if var_name is empty
            if self.var_name.get() == "":
                messagebox.showerror("Error", "First search the student record", parent=self.root)
                return

            mydb = mysql.connector.connect(host='localhost', password='varsha', user='root', database='firstproject')
            cur = mydb.cursor()

            cur.execute("SELECT * FROM result WHERE roll = %s AND course = %s", (self.var_roll.get(), self.var_course.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Result is already present", parent=self.root)
            else:
                per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                cur.execute("INSERT INTO result (roll, name, course, marks, full_marks, per) VALUES (%s, %s, %s, %s, %s, %s)", (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(per)
                ))
                mydb.commit()
                messagebox.showinfo("Success", "The details are inserted successfully", parent=self.root)

        except ValueError as ve:
            messagebox.showerror("Error", f"Configuration error: {str(ve)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            if 'cur' in locals() and cur is not None:
                cur.close()
            if 'mydb' in locals() and mydb is not None:
                mydb.close()
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks .set("")

if __name__=="__main__":
    root=Tk()
    obj=result(root)
    root.mainloop()