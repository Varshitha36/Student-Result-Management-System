from tkinter import*
from PIL import Image,ImageTk
from viewresult import viewresult
from alogin import alogin
import os
class log:
    def __init__(self,root):
        self.root=root
        self.root.title("RESULT")
        self.root.geometry("1575x787+-10+-5")
        self.root.config(bg="steelblue4")
        self.label1=Label(self.root,text="WELCOME TO RESULT MANAGEMENT SYSTEM",bg="steelblue4",fg="white",font="italic 30 bold").pack(pady=(250,0),anchor="center")

        frame=Frame(self.root,bg="steelblue4")

        b1=Button(frame,text="STUDENT ENTRY",bg="grey",fg="white",font=4,command=self.student_login)
        b1.pack(side=LEFT,padx=30,pady=20)
        b2=Button(frame,text="Faculty ENTRY",bg="grey",fg="white",font=4,command=self.admin_login)
        b2.pack(side=LEFT,padx=30,pady=20)

        frame.pack(side=TOP,pady=20)
    def student_login(self):
        self.root.destroy()
        os.system('python viewresult.py')
        

    def admin_login(self):
        self.root.destroy()
        os.system('python alogin.py')
        


'''def studentlogin():
    mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="details")
    cur=mydb.cursor()
    cur.execute("select * from studentdetails")
    row=cur.fetchall()
    root=tk.Tk()
    root.title("student login")
    root.geometry("800x450")
    root.config(bg="steelblue4")
    label1=tk.Label(root,text="STUDENT LOGIN PAGE",bg="steelblue4",fg="white",font="italic 30 bold")
    label1.pack(pady=(250,0),anchor="center")
    frame=tk.Frame(root,bg="steelblue4")
    username=tk.Label(frame,text="USER NAME",bg="white",font=("serif",10,"bold")).pack(side=tk.LEFT,padx=30,pady=20)
    password=tk.Label(frame,text="PASSWORD",bg="white",font=("serif",10,"bold")).pack(side=tk.TOP,padx=30,pady=40)
    frame.pack(side=tk.TOP,pady=20)
    root.mainloop()
    
def adminlogin():
    mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="details")
    cur=mydb.cursor()
    cur.execute("select * from studentdetails")
    row=cur.fetchall()
    root=tk.Tk()
    root.title("student login")
    root.geometry("800x450")
    root.config(bg="steelblue4")
    label1=tk.Label(root,text="STUDENT LOGIN PAGE",bg="steelblue4",fg="white",font="italic 30 bold")
    label1.pack(pady=(250,0),anchor="center")
    frame=tk.Frame(root,bg="steelblue4")
    username=tk.Label(frame,text="USER NAME",bg="white",font=("serif",10,"bold")).pack(side=tk.LEFT,padx=30,pady=20)
    password=tk.Label(frame,text="PASSWORD",bg="white",font=("serif",10,"bold")).pack(side=tk.TOP,padx=30,pady=40)
    frame.pack(side=tk.TOP,pady=20)
    root.mainloop()   '''
    
    
    






if __name__=="__main__":
    root=Tk()
    obj=log(root)
    root.mainloop()