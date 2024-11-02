from tkinter import*
import mysql.connector
import os
from tkinter import ttk,messagebox
from forget import forgot1
class alogin:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1575x787+-10+-5")
        self.root.config(bg="black")
        self.root.focus_force()
        self.user_name=StringVar()
        self.pass_word=StringVar()
        frame_login = Frame(self.root, padx=100, pady=100,bg='steelblue4')
        frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)
        label_username = Label(frame_login, text="Username",bg='steelblue4')
        label_username.grid(row=0, column=0, pady=20, sticky=W)
        entry_username = Entry(frame_login,textvariable=self.user_name,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        entry_username.grid(row=0, column=1, pady=20, padx=10)
        label_password = Label(frame_login, text="Password",bg='steelblue4')
        label_password.grid(row=1, column=0, pady=50, sticky=W)
        entry_password = Entry(frame_login, show="*",textvariable=self.pass_word,border=1,bg="#d9d8d7",font=("serif",10,"bold"))
        entry_password.grid(row=1, column=1, pady=50, padx=10)
        login_button = Button(frame_login, text="Login",bg="grey",width=20,height=2,command=self.login1)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)
        forgot_password_link = Label(frame_login, text="Forgot Password?", fg="blue", cursor="hand2")
        forgot_password_link.grid(row=3, column=0, columnspan=2, pady=5)
        forgot_password_link.bind("<Button-1>", lambda e: self.forgot_password())

    def forgot_password(self):
        self.root.destroy()
        os.system('python forget.py')
    def login1(self):
        mydb=mysql.connector.connect(host='localhost',password='varsha',user='root',database="firstproject")
        cur=mydb.cursor()
        try:
            if self.user_name.get()=="" or self.pass_word.get()=='':
                messagebox.showerror("Error", "Enter Both the Username And Password",parent=self.root)
            else:
                
               
                cur.execute("select * from login  where username=%s and password=%s",(self.user_name.get(),self.pass_word.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Enter the Details Correctly",parent=self.root)
                    self.clear()
                else:
                    self.root.destroy()
                    os.system('python dashboard.py')
                    
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}",parent=self.root)
    def clear(self):
        self.user_name.set('')
        self.pass_word.set('')



        

        



if __name__=="__main__":
    root=Tk()
    obj=alogin(root)
    root.mainloop()