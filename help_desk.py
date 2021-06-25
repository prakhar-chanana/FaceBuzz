from tkinter import *
from PIL import Image,ImageTk
import webbrowser as wb


class Help_Desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1535x800+-10+0")
        self.root.title('FaceBuzz')
        ico = Image.open(r'img\Hotpot.png')
        photo=ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        wall = Image.open(r"img\gg1.jpg")
        wall = wall.resize((1540,810),Image.ANTIALIAS)
        self.w1 = ImageTk.PhotoImage(wall)
        f1 = Label(self.root,image=self.w1)
        f1.place(x=-5,y=0)

        ttl_lbl = Label(f1, text=" FACEBUZZ", font=("Courier", 40, "bold"), bg="#004C01", fg="red")
        ttl_lbl.place(x=0,y=0,width=1540,height=54)

        wallr = Image.open(r"img\Hotpot.png")
        wallr = wallr.resize((50,50),Image.ANTIALIAS)
        self.w = ImageTk.PhotoImage(wallr)
        f = Label(f1,image=self.w,bg="#004C01")
        f.place(x=605,y=0)

        title_lbl = Label(f1, text="Help Desk", font=("Courier", 20, "bold"), bg="#004C01")
        title_lbl.place(x=0, y=54, width=1540, height=30)

        pass_img = Image.open(r"icon\envelope.png")
        pass_img = pass_img.resize((70,70),Image.ANTIALIAS)
        self.p1 = ImageTk.PhotoImage(pass_img)
        btn = Button(f1, image=self.p1, command=self.opn, bd=0, activebackground="#004600",background="#004600")
        btn.place(x=580,y=380,width=80,height=80)
        btn1 = Button(f1, text="help.faceubzz@gmial.com", command=self.opn,font=("Courier", 14, "bold") ,cursor="hand2",bg="#004600",fg="red",bd=0,activebackground="#004600",activeforeground="red")
        btn1.place(x=660,y=380,width=300,height=80)

        ex = Image.open(r"icon\x2.png")
        ex = ex.resize((39,38),Image.ANTIALIAS)
        self.exx = ImageTk.PhotoImage(ex)
        btn88 = Button(f1, image=self.exx,bg="#004600",bd=0,cursor="hand2", command=self.face_exit,activebackground="#004600")
        btn88.place(x=1400,y=760,width=40,height=40)
        btn8=Button(f1, text="Exit", command=self.face_exit, font=("calibri", 14) ,cursor="hand2",bg="#004600",fg="white",bd=0,activebackground="#004600",activeforeground="white")
        btn8.place(x=1440, y=760, width=90, height=40)

    def face_exit(self):
        self.root.destroy()

    def opn(self):
        new = 1
        url = "mailto:prakhar.chanana@gmail.com"
        wb.open(url,new=new)

if __name__ == "__main__":
    root = Tk()
    obj = Help_Desk(root)
    root.mainloop()