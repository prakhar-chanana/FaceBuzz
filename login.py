from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recog_System
from place import PlaceholderEntry
import mysql.connector


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("FaceBuzz")
        self.root.geometry("1535x800+-10+0")
        ico = Image.open(r'img\Hotpot.png')
        photo=ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        wall = Image.open(r"img\wall.jpg")
        wall = wall.resize((1540,810),Image.ANTIALIAS)
        self.w1 = ImageTk.PhotoImage(wall)
        f1 = Label(self.root,image=self.w1)
        f1.place(x=-5,y=0)

        frame = Frame(f1,bg='black')
        frame.place(x=560,y=285,width=420,height=300)

        img1 = Image.open(r"img\Hotpot.png")
        img1 = img1.resize((60,60),Image.ANTIALIAS)
        self.i1 = ImageTk.PhotoImage(img1)
        l1 = Label(frame,image=self.i1,bg="black")
        l1.place(x=175,y=5)

        get_label = Label(frame, text="Login",font=('calibri',18,'bold'),bg="black",fg="white")
        get_label.place(x=175,y=70)

        self.textuser = PlaceholderEntry(frame,"Enter Email", font=('calibri',13),justify="center")
        self.textuser.place(x=75,y=115,width=270)

        self.textpass = ttk.Entry(frame,font=('calibri',13),show="●",justify="center")
        self.textpass.place(x=75,y=150,width=270)

        self.v = IntVar()
        pass_img = Image.open(r"icon\eye.png")
        pass_img = pass_img.resize((21,21),Image.ANTIALIAS)
        self.p1 = ImageTk.PhotoImage(pass_img)
        cnf_img = Image.open(r"icon\eye_slash.png")
        cnf_img = cnf_img.resize((21,21),Image.ANTIALIAS)
        self.p2 = ImageTk.PhotoImage(cnf_img)
        self.pebtn = Checkbutton(frame, image=self.p1, bd=0,indicatoron=0,onvalue=1,offvalue=0,command=self.mark,variable=self.v, activebackground="black",background="black",selectcolor="black")
        self.pebtn.place(x=319,y=151)

        loginto = Button(frame, text="Login", command=self.Log_In, font=('calibri',13,'bold'), fg="white", bg='red', activeforeground="white", activebackground="red",bd=0)
        loginto.place(x=150,y=185,width=120,height=35)

        regis = Button(frame, text="Register", command=self.register_win, font=('calibri',10,'bold'), borderwidth=0, fg="white", bg='black', activeforeground="white", activebackground="black")
        regis.place(x=130,y=245,width=160)

        forgt = Button(frame, text="Forgot Password?", command=self.forgot_password, font=('calibri',10,'bold'), borderwidth=0, fg="white", bg='black', activeforeground="white", activebackground="black")
        forgt.place(x=130,y=270,width=160)

    def mark(self):
        if self.v.get()==1:
            self.textpass.configure(show="")
            self.pebtn.configure(image=self.p2)
        elif self.v.get()==0:
            self.textpass.configure(show="●")
            self.pebtn.configure(image=self.p1)

    def Log_In(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields Required!!")
        elif self.textuser.get()=="prakhar" and self.textpass.get()=="1234":
            messagebox.showinfo("Login","Login Successful!!")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
            cur = conn.cursor()
            cur.execute("select * from register where Email=%s and Password=%s",(
                self.textuser.get(),
                self.textpass.get()
            ))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Invalid Credentials!!",parent=self.root)
            else:
                open_main = messagebox.askyesno("LOGIN","Do you want to Login!!",parent=self.root)
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recog_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def register_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def mark3(self):
        if self.v3.get()==1:
            self.pass_entry.configure(show="")
            self.p2btn.configure(image=self.p22)
        elif self.v3.get()==0:
            self.pass_entry.configure(show="●")
            self.p2btn.configure(image=self.p11)

    def reset_pwd(self):
        if self.Security_entry.get()=="Select":
            messagebox.showerror("ERROR","Select the Security Question!!",parent=self.root2)
        elif self.Sec_ans_entry.get()=="":
            messagebox.showerror("ERROR","Please Answer the Security Question!!",parent=self.root2)
        elif self.pass_entry.get()=="":
            messagebox.showerror("ERROR","Please enter New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
            cur = conn.cursor()
            query=("select * from register where Email=%s and Security_Question=%s and Security_Answer=%s")
            value=(self.textuser.get(),self.Security_entry.get(),self.Sec_ans_entry.get())
            cur.execute(query,value)
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Please enter Correct Answer!!",parent=self.root2)
            else:
                query1=("update register set Password=%s where Email=%s")
                value1=(self.pass_entry.get(),self.textuser.get())
                cur.execute(query1,value1)
                conn.commit()
                conn.close()
                messagebox.showinfo("INFO","Your Password has been Changed!! \n Login with New Password!!",parent=self.root2)
                self.root2.destroy()

    def forgot_password(self):
        if self.textuser.get()=="":
            messagebox.showerror("ERROR","Please Enter Email to Reset Password!!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
            cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            cur.execute(query,value)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("ERROR","Please enter valid Email!!",parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("FaceBuzz")
                self.root2.geometry("1535x800+-10+0")
                ico = Image.open(r"img\Hotpot.png")
                photo=ImageTk.PhotoImage(ico)
                self.root2.wm_iconphoto(False, photo)

                wall2 = Image.open(r"img\wall2.png")
                wall2 = wall2.resize((1540,810),Image.ANTIALIAS)
                self.w3 = ImageTk.PhotoImage(wall2)
                f3 = Label(self.root2,image=self.w3)
                f3.place(x=-5,y=0)

                frame = Frame(f3,bg='#0D0D0D')#0D0D0D
                frame.place(x=560,y=235,width=420,height=295)

                forg_label = Label(frame, text="Reset Password",font=('cailbri',18,'bold'),bg="#0D0D0D",fg="white")
                forg_label.place(x=110,y=20)

                self.Security_entry = ttk.Combobox(frame,font=('calibri',13), state="readonly",justify="center")
                self.Security_entry["values"]=('Select Security Question',"Your Birth Place","Your Petname","Your Girlfriend Name","Your School Name")
                self.Security_entry.current(0)
                self.Security_entry.place(x=75,y=70,width=270)

                self.Sec_ans_entry = PlaceholderEntry(frame, "Security Answer", font=('calibri',13),justify="center")
                self.Sec_ans_entry.place(x=75,y=110,width=270)

                pass_lbl = Label(frame,text="New Password",font=('calibri',13,"bold"),bg="#0D0D0D",fg="white")
                pass_lbl.place(x=155,y=140)

                self.pass_entry = ttk.Entry(frame,font=('calibri',13),show="●",justify="center")
                self.pass_entry.place(x=75,y=170,width=270)

                self.v3 = IntVar()
                pass1_img = Image.open(r"icon\eye2.png")
                pass1_img = pass1_img.resize((21,21),Image.ANTIALIAS)
                self.p11 = ImageTk.PhotoImage(pass1_img)
                cnf1_img = Image.open(r"icon\eye_slash2.png")
                cnf1_img = cnf1_img.resize((21,21),Image.ANTIALIAS)
                self.p22 = ImageTk.PhotoImage(cnf1_img)
                self.p2btn = Checkbutton(frame, image=self.p11,indicatoron=0,onvalue=1,offvalue=0,command=self.mark3,variable=self.v3,activebackground="#0D0D0D",background="#0D0D0D",selectcolor="#0D0D0D",bd=0)
                self.p2btn.place(x=319,y=171)

                rst_btn = Button(frame, text="Reset Password", command=self.reset_pwd, font=('calibri',13,'bold'), fg="white", bg='blue', activeforeground="white", activebackground="blue",bd=0)
                rst_btn.place(x=150,y=220,width=120,height=35)

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("FaceBuzz")
        self.root.geometry("1535x800+-10+0")
        ico = Image.open(r'img\Hotpot.png')
        photo=ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sec_ques = StringVar()
        self.var_sec_ans = StringVar()
        self.var_password = StringVar()
        self.var_cnf = StringVar()

        wall1 = Image.open(r"img\wall11.jpg")
        wall1 = wall1.resize((1540,810),Image.ANTIALIAS)
        self.w2 = ImageTk.PhotoImage(wall1)
        f2 = Label(self.root,image=self.w2)
        f2.place(x=-5,y=0)

        frame = Frame(f2,bg='black')
        frame.place(x=527,y=240,width=490,height=340)

        reg_lbl = Label(frame,text="Registration",font=('calibri',18,"bold"),bg="black",fg="white")
        reg_lbl.place(x=180,y=20)

        self.fname_entry = PlaceholderEntry(frame,"First Name", textvariable=self.var_fname, font=("calibri", 13), justify="center")
        self.fname_entry.place(x=10,y=70,width=230)

        self.lname_entry = PlaceholderEntry(frame,"Last Name", textvariable=self.var_lname, font=("calibri", 13), justify="center")
        self.lname_entry.place(x=250,y=70,width=230)

        self.email_entry = PlaceholderEntry(frame,"Email", textvariable=self.var_email, font=("calibri", 13), justify="center")
        self.email_entry.place(x=10,y=110,width=230)

        self.contact_entry = PlaceholderEntry(frame,"Contact", textvariable=self.var_contact, font=("calibri", 13), justify="center")
        self.contact_entry.place(x=250,y=110,width=230)

        self.Security_entry = ttk.Combobox(frame,textvariable=self.var_sec_ques,font=('calibri',13), state="readonly",justify="center")
        self.Security_entry["values"]=('Select Security Question',"Your Birth Place","Your Petname","Your Girlfriend Name","Your School Name")
        self.Security_entry.current(0)
        self.Security_entry.place(x=10,y=150,width=230)
        
        self.Sec_ans_entry = PlaceholderEntry(frame,"Security Answer", textvariable=self.var_sec_ans, font=("calibri", 13), justify="center")
        self.Sec_ans_entry.place(x=250,y=150,width=230)

        password_lbl = Label(frame,text="Password",font=('calibri',13),bg="black",fg="white")
        password_lbl.place(x=90,y=180)

        self.password_entry = ttk.Entry(frame, show="●",textvariable=self.var_password,font=('calibri',13),justify="center")
        self.password_entry.place(x=10,y=205,width=230)

        self.v1 = IntVar()
        pass_img = Image.open(r"icon\eye1.png")
        pass_img = pass_img.resize((21,21),Image.ANTIALIAS)
        self.p1 = ImageTk.PhotoImage(pass_img)
        cnf_img = Image.open(r"icon\eye_slash1.png")
        cnf_img = cnf_img.resize((21,21),Image.ANTIALIAS)
        self.p2 = ImageTk.PhotoImage(cnf_img)
        self.cbtn = Checkbutton(frame, image=self.p1,indicatoron=0,onvalue=1,offvalue=0,command=self.mark1,variable=self.v1,bd=0, activebackground="black",background="black",selectcolor="black")
        self.cbtn.place(x=214,y=206)

        cnf_lbl = Label(frame,text="Confirm Password",font=('calibri',13),bg="black",fg="white")
        cnf_lbl.place(x=300,y=180)

        self.v2 = IntVar()
        self.cnf_entry = ttk.Entry(frame,show="●",textvariable=self.var_cnf,font=('calibri',13),justify="center")
        self.cnf_entry.place(x=250,y=205,width=230)
        self.cnfbtn = Checkbutton(frame, image=self.p1,indicatoron=0,onvalue=1,offvalue=0,command=self.mark2,variable=self.v2,bd=0, activebackground="black",background="black",selectcolor="black")
        self.cnfbtn.place(x=454,y=206)

        self.var_check = IntVar()
        s = ttk.Style()
        s.configure("Black.TCheckbutton", foreground="white", background="black")
        checkbtn = ttk.Checkbutton(frame, style="Black.TCheckbutton", text="I Agree The Terms & Conditions", onvalue=1, offvalue=0, variable=self.var_check)
        checkbtn.place(x=20,y=240)

        reg_btn=Button(frame, text="Register Now", command=self.register_data,font=('calibri',12,"bold"),bg="green",fg="white", activeforeground="white", activebackground="green",bd=0)
        reg_btn.place(x=20,y=300,width=200)

        log_btn=Button(frame, text="Login Now", command=self.log,font=('calibri',12,"bold"),bg="green",fg="white", activeforeground="white", activebackground="green",bd=0)
        log_btn.place(x=270,y=300,width=200)

    def mark1(self):
        if self.v1.get()==1:
            self.password_entry.configure(show="")
            self.cbtn.configure(image=self.p2)
        elif self.v1.get()==0:
            self.password_entry.configure(show="●")
            self.cbtn.configure(image=self.p1)

    def mark2(self):
        if self.v2.get()==1:
            self.cnf_entry.configure(show="")
            self.cnfbtn.configure(image=self.p2)
        elif self.v2.get()==0:
            self.cnf_entry.configure(show="●")
            self.cnfbtn.configure(image=self.p1)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_sec_ques.get()=="Select Security Question" or self.var_sec_ans.get()=="":
            messagebox.showerror("ERROR","All Fields are Required!!",parent=self.root)
        elif self.var_password.get()!=self.var_cnf.get():
            messagebox.showerror("ERROR","Password & Confirm Password must be same!!",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("ERROR","Please Agree with our Terms & Conditions!!", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
            cur = conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row = cur.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","Email Already Registered!!",parent=self.root)
            else:
                cur.execute("insert into register (First_Name, Last_Name, Email, Contact, Security_Question, Security_Answer, Password) values (%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_sec_ques.get(),
                    self.var_sec_ans.get(),
                    self.var_password.get()
                ))
                messagebox.showinfo("Success","Successfully Registered!!",parent=self.root)
            conn.commit()
            conn.close()

    def log(self):
        self.root.destroy()

if __name__ == "__main__":
    main()