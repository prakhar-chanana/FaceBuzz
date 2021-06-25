from tkinter import * 
from tkinter import messagebox
from student import Student
from train import Train
from face_recog import Face_Recog
from attendance import Attendance
from developer import Developer
from help_desk import Help_Desk
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import os


class Face_Recog_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1535x800+-10+0")
        self.root.title('FaceBuzz')
        ico = Image.open(r"img\Hotpot.png")
        photo=ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        wall = Image.open(r"img\gradRed.png")
        wall = wall.resize((1540,810),Image.ANTIALIAS)
        self.w1 = ImageTk.PhotoImage(wall)
        f1 = Label(self.root,image=self.w1)
        f1.place(x=-5,y=0)

        fr = Frame(f1,bg="green")
        fr.place(x=0,y=0,width=1540,height=50)

        title_lbl = Label(fr, text=" FACEBUZZ", font=("Courier", 40, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=54)

        wallr = Image.open(r"img\Hotpot.png")
        wallr = wallr.resize((50,50),Image.ANTIALIAS)
        self.w = ImageTk.PhotoImage(wallr)
        f = Label(fr,image=self.w,bg="black")
        f.place(x=605,y=0)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(fr, font=("Digital-7 Mono", 15, "bold"), bg="black", fg="red")
        lbl.place(x=0,y=0,width=150,height=50)
        time()

        sd = Image.open(r"icon\st.png")
        sd = sd.resize((80,78),Image.ANTIALIAS)
        self.sdd = ImageTk.PhotoImage(sd)
        btn11 = Button(f1,image=self.sdd,cursor="hand2",bd=0,bg="#360000",activebackground="#360000",command=self.student_details) #360000
        btn11.place(x=580,y=200)
        btn1=Button(f1, text="Student Details",bd=0, command=self.student_details, font=("calibri", 14) ,cursor="hand2",bg="#360000", fg="white",activebackground="#360000",activeforeground="white")
        btn1.place(x=660, y=200, width=300, height=80)

        fd = Image.open(r"icon\Faceid.png")
        fd = fd.resize((80,78),Image.ANTIALIAS)
        self.fdd = ImageTk.PhotoImage(fd)
        btn22 = Button(f1,image=self.fdd,cursor="hand2",bd=0,bg="#480000",activebackground="#480000",command=self.face_Recog) #480000
        btn22.place(x=580,y=300)
        btn2=Button(f1, text="Face Detector",bd=0, command=self.face_Recog, font=("calibri", 14) ,cursor="hand2", bg="#480000", fg="white", activeforeground="white",activebackground="#480000")
        btn2.place(x=660, y=300, width=300, height=80)

        at = Image.open(r"icon\att.png")
        at = at.resize((80,78),Image.ANTIALIAS)
        self.att = ImageTk.PhotoImage(at)
        btn33 = Button(f1,image=self.att,cursor="hand2",bd=0,bg="#500000",activebackground="#500000",command=self.attendance) #500000
        btn33.place(x=580,y=400)
        btn3=Button(f1, text="Attendance",bd=0, command=self.attendance, font=("calibri", 14) ,cursor="hand2",bg="#500000",fg="white",activebackground="#500000",activeforeground="white")
        btn3.place(x=660, y=400, width=300, height=80)

        td = Image.open(r"icon\train.png")
        td = td.resize((80,78),Image.ANTIALIAS)
        self.tdd = ImageTk.PhotoImage(td)
        btn55 = Button(f1,image=self.tdd,cursor="hand2",bd=0,bg="#5B0000",activebackground="#5B0000",command=self.train_data) #5B0000
        btn55.place(x=580,y=500)
        btn5=Button(f1, text="Train Data", command=self.train_data, font=("calibri", 14) ,cursor="hand2",bg="#5B0000",fg="white",bd=0,activeforeground="white",activebackground="#5B0000")
        btn5.place(x=660, y=500, width=300, height=80)

        ds = Image.open(r"icon\filter.png")
        ds = ds.resize((80,78),Image.ANTIALIAS)
        self.dss = ImageTk.PhotoImage(ds)
        btn66 = Button(f1,image=self.dss,cursor="hand2",bd=0,bg="#6B0000",activebackground="#6B0000",command=self.open_image) #6B0000
        btn66.place(x=580,y=600)
        btn6=Button(f1, text="Dataset",bd=0, command=self.open_image, font=("calibri", 14) ,cursor="hand2",bg="#6B0000",activebackground="#6B0000",fg="white",activeforeground="white")
        btn6.place(x=660, y=600, width=300, height=80)



        hel = Image.open(r"icon\help.png")
        hel = hel.resize((39,38),Image.ANTIALIAS)
        self.hell = ImageTk.PhotoImage(hel)
        btn44 = Button(f1,image=self.hell,cursor="hand2",bd=0,bg="#7F0101",activebackground="#7F0101",command=self.help)
        btn44.place(x=1400,y=660)
        btn4=Button(f1, text="Help Desk", command=self.help, font=("calibri", 14) ,cursor="hand2",bd=0,bg="#7F0101",activebackground="#7F0101",fg="white",activeforeground="white")
        btn4.place(x=1440, y=660, width=90, height=40)

        dev = Image.open(r"icon\dev.png")
        dev = dev.resize((39,38),Image.ANTIALIAS)
        self.devv = ImageTk.PhotoImage(dev)
        btn77=Button(f1,image=self.devv,bd=0,bg="#7F0101",activebackground="#7F0101",cursor="hand2",command=self.developers) #7F0101
        btn77.place(x=1400,y=710)
        btn7=Button(f1, text="Developer", command=self.developers, font=("calibri", 14) ,cursor="hand2",bd=0,bg="#7F0101",activebackground="#7F0101",fg="white",activeforeground="white")
        btn7.place(x=1440, y=710, width=90, height=40)

        ex = Image.open(r"icon\x2.png")
        ex = ex.resize((39,38),Image.ANTIALIAS)
        self.exx = ImageTk.PhotoImage(ex)
        btn88 = Button(f1, image=self.exx,bg="#870000",bd=0,cursor="hand2", command=self.face_exit,activebackground="#600000") #870000
        btn88.place(x=1400,y=760)
        btn8=Button(f1, text="Exit", command=self.face_exit, font=("calibri", 14) ,cursor="hand2",bg="#870000",fg="white",bd=0,activebackground="#600000",activeforeground="white")
        btn8.place(x=1440, y=760, width=90, height=40)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_image(self):
        os.startfile("data")

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_Recog(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recog(self.new_window)
    
    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developers(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_Desk(self.new_window)

    def face_exit(self):
        self.face_exit = messagebox.askyesno("FaceBuzz","Are you sure to EXIT!", parent=self.root)
        if self.face_exit>0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog_System(root)
    root.mainloop()