from tkinter import*
from PIL import Image,ImageTk
from course import course
from student import student
from result import result
from delete import delete
from tkinter import ttk,messagebox
import mysql.connector
import os
class RMS:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1575x787+-10+-5")
        self.root.config(bg="white")
        #icon
        self.image=Image.open("student.jpg")
        self.image=self.image.resize((40,40))
        self.label=ImageTk.PhotoImage(self.image)

        #---title---
        self.title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",compound=LEFT,image=self.label,padx=10,font=("serif",30,"bold"),bg="#0b5377",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #--menu--
        menu=LabelFrame(self.root,text="menu",bg="light blue")
        menu.place(x=10,y=70,width=1490,height=80)
        b1=Button(menu,text="Course",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=220,height=40)
        b2=Button(menu,text="Student",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=270,y=5,width=220,height=40)
        b3=Button(menu,text="Result",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=520,y=5,width=220,height=40)
        b4=Button(menu,text="View Student Result",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.delete_result).place(x=770,y=5,width=200,height=40)
        b5=Button(menu,text="Logout",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1000,y=5,width=220,height=40)
        b6=Button(menu,text="EXIT",font=("serif",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1250,y=5,width=220,height=40)
        
        self.image1=Image.open("result.jpg")
        self.image1=self.image1.resize((1000,300))
        self.image1=ImageTk.PhotoImage(self.image1)
        self.title=Label(self.root,image=self.image1,font=("serif",30,"bold"),bg="black")
        self.title.place(x=220,y=180,height=400)
        self.total_students=Label(self.root,text="TOTAL STUDENTS\n[0]",bg="#0b5378",fg="white",font=("serif",14),border=10,relief=SUNKEN)
        self.total_students.place(x=250,y=550,width=270,height=125)
        self.total_courses=Label(self.root,text="TOTAL COURSES\n[0]",bg="#0b5378",fg="white",font=("serif",14),border=10,relief=SUNKEN)
        self.total_courses.place(x=590,y=550,width=270,height=125)
        
        self.total_results=Label(self.root,text="TOTAL RESULTS\n[0]",bg="#0b5378",fg="white",font=("serif",14),border=10,relief=SUNKEN)
        self.total_results.place(x=930,y=550,width=270,height=125)
        
        
        
        
        #--footer--
        footer=Label(text="SRMS-STUDENT RESULT MANAGEMENT SYSTEM\n FOR FUTHER ANY DOUBTS PLEASE CONTACT THIS NUMBER N0:7345261789\nTHANKU FOR USING THIS SRMS",bg="black",fg="white",font=("serif",10,"bold")).pack(side=BOTTOM,fill=X)
        self.update_details()
    def update_details(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        cur.execute('select count(*) from student')
        r1=cur.fetchone()
        c1=r1[0]
        self.total_students.config(text=f"TOTAL STUDENTS\n[{str(c1)}]")
        self.total_students.after(200,self.update_details)

        cur.execute('select count(*) from course')
        r2=cur.fetchone()
        c2=r2[0]
        self.total_courses.config(text=f"TOTAL COURSES\n[{str(c2)}]")
        cur.execute('select count(*) from result')
        r3=cur.fetchone()
        c3=r3[0]
        self.total_results.config(text=f"TOTAL RESULTS\n[{str(c3)}]")   
    def add_course(self):
        self.course_win=Toplevel(self.root)
        self.new_obj=course(self.course_win)

    def add_student(self):
        self.student_obj=Toplevel(self.root)
        self.new_obj1=student(self.student_obj)
    def add_result(self):
        self.result_obj=Toplevel(self.root)
        self.new_obj2=result(self.result_obj)
    def delete_result(self):
        self.stu_view=Toplevel(self.root)
        self.new_obj3=delete(self.stu_view)
    def logout(self):
        op=messagebox.askyesnocancel("confirm","do you really want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system('python login.py')
    def exit(self):
        op=messagebox.askyesnocancel("confirm","do you really want to exit",parent=self.root)
        if op==True:
            self.root.destroy()
            

    

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()