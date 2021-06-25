from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import cv2
import numpy as np


class Train:
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

        title_lbl = Label(f1, text="Training Dataset", font=("Courier", 20, "bold"), bg="#004C01")
        title_lbl.place(x=0, y=54, width=1540, height=30)

        fd = Image.open(r"icon\train.png")
        fd = fd.resize((70,70),Image.ANTIALIAS)
        self.fdd = ImageTk.PhotoImage(fd)
        btn22 = Button(f1,image=self.fdd,cursor="hand2",bd=0,bg="#004600",activebackground="#004600",command=self.train_classifier)
        btn22.place(x=580,y=380,width=80,height=80)
        btn1=Button(f1, text="Tarin Dataset", command=self.train_classifier, font=("calibri",25) ,cursor="hand2",bg="#004600",activebackground="#004600",bd=0)
        btn1.place(x=660, y=380, width=300, height=80)

        ex = Image.open(r"icon\x2.png")
        ex = ex.resize((39,38),Image.ANTIALIAS)
        self.exx = ImageTk.PhotoImage(ex)
        btn88 = Button(f1, image=self.exx,bg="#004600",bd=0,cursor="hand2", command=self.face_exit,activebackground="#004600")
        btn88.place(x=1400,y=760,width=40,height=40)
        btn8=Button(f1, text="Exit", command=self.face_exit, font=("calibri", 14) ,cursor="hand2",bg="#004600",fg="white",bd=0,activebackground="#004600",activeforeground="white")
        btn8.place(x=1440, y=760, width=90, height=40)

    def face_exit(self):
        self.root.destroy()

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        Faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            Faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(Faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Taining Dataset Completed!!",parent=self.root)
    

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()