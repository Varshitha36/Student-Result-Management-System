from tkinter import*
import mysql.connector
import os
from tkinter import ttk,messagebox
class forgot1:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1575x787+-10+-5")
        self.root.config(bg="black")
        self.root.focus_force()
        self.username=StringVar()
        self.current_password=StringVar()
        self.renter_password=StringVar()
        frame_login = Frame(self.root, padx=100, pady=100,bg='steelblue4')
        frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)
        label_user = Label(frame_login, text="USERNAME",bg='steelblue4')
        label_user.grid(row=0, column=0, pady=20, sticky=W)
        entry_user = Entry(frame_login,textvariable=self.username,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        entry_user.grid(row=0, column=1, pady=20, padx=10)
        label_current = Label(frame_login, text="New Password",bg='steelblue4')
        label_current.grid(row=1, column=0, pady=50, sticky=W)
        entry_current = Entry(frame_login,textvariable=self.current_password,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        entry_current.grid(row=1, column=1, pady=50, padx=10)
        label_renter = Label(frame_login, text="RENTER Password",bg='steelblue4')
        label_renter.grid(row=2, column=0, pady=20, sticky=W)
        entry_renter = Entry(frame_login,textvariable=self.renter_password,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        entry_renter.grid(row=2, column=1, pady=20, padx=10)
        login_button = Button(frame_login, text="ENTER",bg="grey",width=20,height=2,command=self.enter)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)
    def enter(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.current_password.get()=="" or self.renter_password.get()=='' or self.username.get()=='':
                messagebox.showerror("Error", "Enter the entire details",parent=self.root)
            else:
                if self.current_password.get() != self.renter_password.get():
                    messagebox.showerror("Error", "Enter the details correctly",parent=self.root)
                else:
               
                    cur.execute("update login set password=%s where username=%s",(self.current_password.get(),self.username.get()))
                    mydb.commit()
                    self.root.destroy()
                    os.system('python alogin.py')
                    
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    def clear(self):
        self.username.set('')
        self.current_password.set('')
        self.renter_password.set('')

if __name__=="__main__":
    root=Tk()
    obj=forgot1(root)
    root.mainloop()