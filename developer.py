from tkinter import *
from PIL import Image,ImageTk
import webbrowser as wb


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1535x800+-10+0")
        self.root.title('FaceBuzz')
        ico = Image.open(r'img\logo_size_invert1.jpg')
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

        title_lbl = Label(f1, text="Developers", font=("Courier", 20, "bold"), bg="#004C01")
        title_lbl.place(x=0, y=54, width=1540, height=30)

        Pframe = Frame(f1, bd=0,bg="#004600")
        Pframe.place(x=360,y=255,width=360,height=415)

        Pimg = Image.open(r"img\Prakhar.jpg")
        Pimg = Pimg.resize((200,200),Image.ANTIALIAS)
        self.PCimg = ImageTk.PhotoImage(Pimg)

        Plbl = Label(Pframe,image=self.PCimg,bg="#499048")
        Plbl.place(x=80,y=15)

        Pdev_label = Label(Pframe, text='Prakhar Chanana', font=('Courier', 20,"bold"),justify="center",bg="#004600",fg="white")
        Pdev_label.place(x=10, y=230,width=340)

        clg = Label(Pframe,text="VNS Group of Institutions, Bhopal", font=("Courier",12),justify="center",bg="#004600",fg="white")
        clg.place(x=10, y=270,width=340)

        uni = Label(Pframe, text="RGPV",font=("Courier",15,"bold"),justify="center",bg="#004600",fg="white")
        uni.place(x=10,y=297,width=340)

        bs1 = Image.open(r"icon\envelope.png")
        bs1 =bs1.resize((50,50),Image.ANTIALIAS)
        self.bs11 = ImageTk.PhotoImage(bs1)
        btn1=Button(Pframe,bd=0,image=self.bs11,command=self.Pmail,bg="#004600",activebackground="#004600")
        btn1.place(x=90,y=350)

        bs2 = Image.open(r"icon\Linkedin.png")
        bs2 = bs2.resize((50,50),Image.ANTIALIAS)
        self.bs22 = ImageTk.PhotoImage(bs2)
        btn2=Button(Pframe,bd=0,image=self.bs22,command=self.Plink,bg="#004600",activebackground="#004600")
        btn2.place(x=150,y=350)

        bs3 = Image.open(r"icon\github.png")
        bs3 = bs3.resize((50,50),Image.ANTIALIAS)
        self.bs33 = ImageTk.PhotoImage(bs3)
        btn3 = Button(Pframe,bd=0,image=self.bs33,command=self.Pgit,bg="#004600",activebackground="#004600")
        btn3.place(x=210,y=350)

        Kframe = Frame(f1,bd=0,bg="#004600")
        Kframe.place(x=820,y=255,width=360,height=415)

        Kimg = Image.open(r"img\KG.jpg")
        Kimg = Kimg.resize((160,200),Image.ANTIALIAS)
        self.KGimg = ImageTk.PhotoImage(Kimg)

        Klbl = Label(Kframe,image=self.KGimg,bg="#499048")
        Klbl.place(x=100,y=15)

        Kdev_label = Label(Kframe, text='Kavya Gupta', font=('Courier', 20,"bold"),justify="center",bg="#004600",fg="white")
        Kdev_label.place(x=10, y=230,width=340)

        clg = Label(Kframe,text="VNS Group of Institutions, Bhopal", font=("Courier",12),justify="center",bg="#004600",fg="white")
        clg.place(x=10, y=270,width=340)

        uni = Label(Kframe, text="RGPV",font=("Courier",15,"bold"),justify="center",bg="#004600",fg="white")
        uni.place(x=10,y=297,width=340)

        btn1=Button(Kframe,bd=0,image=self.bs11, command=self.Kmail,bg="#004600",activebackground="#004600")
        btn1.place(x=125,y=350)

        btn2=Button(Kframe,bd=0,image=self.bs22,command=self.Klink,bg="#004600",activebackground="#004600")
        btn2.place(x=185,y=350)

        ex = Image.open(r"icon\x2.png")
        ex = ex.resize((39,38),Image.ANTIALIAS)
        self.exx = ImageTk.PhotoImage(ex)
        btn88 = Button(f1, image=self.exx,bg="#004600",bd=0,cursor="hand2", command=self.face_exit,activebackground="#004600")
        btn88.place(x=1400,y=760,width=40,height=40)
        btn8=Button(f1, text="Exit", command=self.face_exit, font=("calibri", 14) ,cursor="hand2",bg="#004600",fg="white",bd=0,activebackground="#004600",activeforeground="white")
        btn8.place(x=1440, y=760, width=90, height=40)

    def face_exit(self):
        self.root.destroy()

    def Pmail(self):
        new = 1
        url = "mailto:prakhar.chanana@gmail.com"
        wb.open(url,new=new)

    def Kmail(self):
        new = 1
        url = "mailto:kavyag200@gmail.com"
        wb.open(url,new=new)

    def Plink(self):
        new = 1
        url = "https://www.linkedin.com/in/prakhar-chanana"
        wb.open(url,new=new)

    def Klink(self):
        new = 1
        url = "https://www.linkedin.com/in/kavya-g"
        wb.open(url,new=new)

    def Pgit(self):
        new = 1
        url = "https://github.com/prakhar-chanana"
        wb.open(url,new=new)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()