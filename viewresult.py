from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class viewresult:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1575x787+-10+-5")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="View Your Results",bg="#128cc9").place(x=20,y=10,width=1500,height=50)
        self.var_search=StringVar()
        r_select=Label(self.root,text="SEARCH By ROLLNO",bg="white",font=("serif",10,"bold")).place(x=300,y=200,width=180,height=40)
        self.var_roll1=Entry(self.root,textvariable=self.var_search,bg="white",font=("serif",10,"bold")).place(x=550,y=200,width=310,height=40)
        self.search1=Button(self.root,text="SEARCH",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.search).place(x=900,y=200,width=90,height=40)
        self.clear1=Button(self.root,text="CLEAR",font=("serif",10,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.clear).place(x=700,y=500,width=90,height=40)
        r_roll=Label(self.root,text="ROLL NO",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=190,y=300,width=180,height=50)
        r_name=Label(self.root,text="NAME",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=370,y=300,width=180,height=50)
        r_course=Label(self.root,text="COURSE",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=550,y=300,width=180,height=50)
        r_marks_ob=Label(self.root,text="MARKS OBTAINED ",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=730,y=300,width=180,height=50)
        r_full_marks=Label(self.root,text="FULL MARKS",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=910,y=300,width=180,height=50)
        r_percentage=Label(self.root,text="PERCENTAGE",bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE).place(x=1090,y=300,width=180,height=50)
        self.roll=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.roll.place(x=190,y=350,width=180,height=50)
        self.name=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.name.place(x=370,y=350,width=180,height=50)
        self.course=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.course.place(x=550,y=350,width=180,height=50)
        self.marks_ob=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.marks_ob.place(x=730,y=350,width=180,height=50)
        self.full_marks=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.full_marks.place(x=910,y=350,width=180,height=50)
        self.percentage=Label(self.root,bg="white",font=("serif",10,"bold"),bd=2,relief=GROOVE)
        self.percentage.place(x=1090,y=350,width=180,height=50)
    def search(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("error","Roll no is required",parent=self.root) 
            else:
                roll_no = self.var_search.get()  # Get the roll number
                cur.execute("SELECT * FROM result WHERE roll=%s", (roll_no,))
                rows=cur.fetchone()
                
                if rows!=None:
                    self.roll.config(text=rows[1])
                    self.name.config(text=rows[2])
                    self.course.config(text=rows[3])
                    self.marks_ob.config(text=rows[4])
                    self.full_marks.config(text=rows[5])
                    self.percentage.config(text=rows[6])
                    
                else:
                    messagebox.showerror("error","No record found",parent=self.root)       
                mydb.commit()
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")
    def clear(self):
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.percentage.config(text="")
    
    



if __name__=="__main__":
    root=Tk()
    obj=viewresult(root)
    root.mainloop()