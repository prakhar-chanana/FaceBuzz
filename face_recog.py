from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recog:
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

        title_lbl = Label(f1, text="Face Detector", font=("Courier", 20, "bold"), bg="#004C01")
        title_lbl.place(x=0, y=54, width=1540, height=30)

        fd = Image.open(r"icon\Faceid.png")
        fd = fd.resize((70,70),Image.ANTIALIAS)
        self.fdd = ImageTk.PhotoImage(fd)
        btn22 = Button(f1,image=self.fdd,cursor="hand2",bd=0,bg="#004600",activebackground="#004600",command=self.face_rEcog)
        btn22.place(x=580,y=380,width=80,height=80)
        btn1=Button(f1, text="Face Detector", command=self.face_rEcog, font=("calibri",25) ,cursor="hand2",bg="#004600",activebackground="#004600",bd=0)
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

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((','))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    def face_rEcog(self):
        def recognify(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grey_image,scaleFactor,minNeighbors)
            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grey_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
                my_cursor = conn.cursor()
                my_cursor.execute("Select Name from student where ID="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                my_cursor.execute("Select Enroll from student where ID="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                my_cursor.execute("Select Course from student where ID="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                my_cursor.execute("Select ID from student where ID="+str(id))
                i = str(my_cursor.fetchone())
                i = "+".join(i)

                if confidence>77:
                    cv2.putText(img,f"Enroll No.: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name : {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course : {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord = recognify(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog(root)
    root.mainloop()