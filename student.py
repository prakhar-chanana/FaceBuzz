from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1535x800+-10+0")
        self.root.title('FaceBuzz')
        ico = Image.open(r'img\logo_size_invert1.jpg')
        photo=ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        wall = Image.open(r"img\gg.jpg")
        wall = wall.resize((1540,810),Image.ANTIALIAS)
        self.w1 = ImageTk.PhotoImage(wall)
        f1 = Label(self.root,image=self.w1)
        f1.place(x=-5,y=0)

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_enroll = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_id = IntVar()
        self.var_id.set('')
        self.var_search = StringVar()
        self.var_srch_txt = StringVar()

        ttl_lbl = Label(f1, text=" FACEBUZZ", font=("Courier", 40, "bold"), bg="#499048", fg="red")
        ttl_lbl.place(x=0,y=0,width=1540,height=54)

        wallr = Image.open(r"img\Hotpot.png")
        wallr = wallr.resize((50,50),Image.ANTIALIAS)
        self.w = ImageTk.PhotoImage(wallr)
        f = Label(f1,image=self.w,bg="#499048")
        f.place(x=605,y=0)

        title_lbl = Label(f1, text="Student Details Management System", font=("Courier", 20, "bold"), bg="#499048",)
        title_lbl.place(x=0, y=54, width=1540, height=30)

        Left_frame = Frame(f1,bg="#499048")
        Left_frame.place(x=20, y=95, width=745, height=700)

        lf_lbl = Label(Left_frame, text="Student Details", font=("Courier", 12,"bold"),bg="#499048")
        lf_lbl.place(x=0,y=0,width=745)

        current_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information",font=('Courier', 12, 'bold'),bg="#499048")
        current_frame.place(x=10, y=25, width=725, height=150)

        dept_label = Label(current_frame, text='Department :', font=('calibri', 12),bg="#499048")
        dept_label.grid(row=0, column=0, padx=10, sticky=W)

        dept_combo = ttk.Combobox(current_frame, textvariable=self.var_dep, font=('calibri', 12), width=20,state="read only")
        dept_combo["values"] = (
            'Select Department', 'Faculty of Engineering', 'Faculty of Pharmacy', 'Faculty of Management')
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        course_label = Label(current_frame, text='Course :', font=('calibri', 12),bg="#499048")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_frame, textvariable=self.var_course, font=('calibri', 12), width=20,state="read only")
        course_combo["values"] = (
            'Select Cousre', 'B.Tech(CSE)', 'B.Tech(ME)', 'B.Tech(EC)', 'B.Tech(EX)', 'B.Tech(CE)', 'B.Tech(ME)',
            'M.Tech(CS)', 'M.Tech(DC)', 'Diploma(Mechanical)', 'Diploma(Civil)', 'Diploma(Mining)', 'B.Pharma',
            'M.Pharma',
            'D.Pharma', 'MBA')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        year_label = Label(current_frame, text='Year :', font=('calibri', 12),bg="#499048")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_frame, textvariable=self.var_year, font=('calibri', 12), width=20,state="read only")
        year_combo["values"] = ('Select Year', '1st Year', '2nd Year', '3rd Year', '4th Year')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        sem_label = Label(current_frame, text='Semester :', font=('calibri', 12),bg="#499048")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_frame, textvariable=self.var_semester, font=('calibri', 12), width=20,state="read only")
        sem_combo["values"] = (
            'Select Semester', '1st Semester', '2nd Semester', '3rd Semester', '4th Semester', '5th Semester',
            '6th Semester', '7th Semester', '8th Semester')
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        stu_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Student Information", font=('Courier', 12, 'bold'),bg="#499048")
        stu_frame.place(x=10, y=180, width=725, height=510)

        id_label = Label(stu_frame, text="ID :", font=('calibri',13),bg="#499048")
        id_label.grid(row=0, column=0, padx=5, pady=15, sticky=W)

        id2_label = Label(stu_frame, text="", textvariable=self.var_id, font=('calibri',13),bg="#499048")
        id2_label.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        roll_label = Label(stu_frame, text='Enroll No :', font=('calibri', 13),bg="#499048")
        roll_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        roll_entry = ttk.Entry(stu_frame, textvariable=self.var_enroll, width=20, font=('calibri', 13))
        roll_entry.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        name_label = Label(stu_frame, text='Name :', font=('calibri', 13),bg="#499048")
        name_label.grid(row=1, column=2, padx=5, pady=15, sticky=W)

        name_entry = ttk.Entry(stu_frame, textvariable=self.var_name, width=20, font=('calibri', 13))
        name_entry.grid(row=1, column=3, padx=5, pady=15, sticky=W)

        gender_label = Label(stu_frame, text='Gender :', font=('calibri', 13),bg="#499048")
        gender_label.grid(row=2, column=0, padx=5, pady=15, sticky=W)

        gender_combo = ttk.Combobox(stu_frame, textvariable=self.var_gender, font=('calibri', 13), width=18,state="read only")
        gender_combo["values"] = ('Select Gender', 'Male', 'Female', 'Other')
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=15, sticky=W)

        dob_label = Label(stu_frame, text='D.O.B (DD/MM/YYYY) :', font=('calibri', 13),bg="#499048")
        dob_label.grid(row=2, column=2, padx=5, pady=15, sticky=W)

        dob_entry = ttk.Entry(stu_frame, textvariable=self.var_dob, width=20, font=('calibri', 13))
        dob_entry.grid(row=2, column=3, padx=5, pady=15, sticky=W)

        email_label = Label(stu_frame, text='Email :', font=('calibri', 13),bg="#499048")
        email_label.grid(row=3, column=0, padx=5, pady=15, sticky=W)

        email_entry = ttk.Entry(stu_frame, textvariable=self.var_email, width=20, font=('calibri', 13))
        email_entry.grid(row=3, column=1, padx=5, pady=15, sticky=W)

        phone_label = Label(stu_frame, text='Phone No:', font=('calibri', 13),bg="#499048")
        phone_label.grid(row=3, column=2, padx=5, pady=15, sticky=W)

        phone_entry = ttk.Entry(stu_frame, textvariable=self.var_phone, width=20, font=('calibri', 13))
        phone_entry.grid(row=3, column=3, padx=5, pady=15, sticky=W)

        address_label = Label(stu_frame, text='Address :', font=('calibri', 13),bg="#499048")
        address_label.grid(row=4, column=0, padx=5, pady=15, sticky=W)

        address_entry = ttk.Entry(stu_frame, textvariable=self.var_address, width=20, font=('calibri', 13))
        address_entry.grid(row=4, column=1, padx=5, pady=15, sticky=W)

        teacher_label = Label(stu_frame, text='Teacher Name :', font=('calibri', 13),bg="#499048")
        teacher_label.grid(row=4, column=2, padx=5, pady=15, sticky=W)

        teacher_entry = ttk.Entry(stu_frame, textvariable=self.var_teacher, width=20, font=('calibri', 13))
        teacher_entry.grid(row=4, column=3, padx=5, pady=15, sticky=W)

        s = ttk.Style()
        s.configure("Green.TRadiobutton", background="#499048")
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(stu_frame,style="Green.TRadiobutton", variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio_btn1.grid(row=5, column=0,padx=5,pady=10)

        radio_btn2 = ttk.Radiobutton(stu_frame, variable=self.var_radio1, text="No Photo Sample", value="No",style="Green.TRadiobutton")
        radio_btn2.grid(row=5, column=1,padx=5,pady=10)

        btn_frame = Frame(stu_frame,bg="#499048")
        btn_frame.place(x=0, y=410, width=718, height=75)

        save_btn = Button(btn_frame, width=19, text='Save', font=('calibri', 13), command=self.add_data,bd=0)
        save_btn.grid(row=0, column=0, padx=2,pady=2)

        update_btn = Button(btn_frame, width=19, text='Update', font=('calibri', 13), command=self.update_data,bd=0)
        update_btn.grid(row=0, column=1, padx=2,pady=2)

        delete_btn = Button(btn_frame, width=19, text='Delete', font=('calibri', 13), command=self.delete_data,bd=0)
        delete_btn.grid(row=0, column=2, padx=2,pady=2)

        reset_btn = Button(btn_frame, width=19, text='Reset', font=('calibri', 13), command=self.reset_data,bd=0)
        reset_btn.grid(row=0, column=3, padx=2,pady=2)

        take_photo_btn = Button(btn_frame, width=39, text='Take Photo Sample',font=('calibri', 13), command=self.generate_dataset,bd=0)
        take_photo_btn.grid(row=1, column=0, columnspan=2, padx=2,pady=2)

        update_photo_btn = Button(btn_frame, width=39, text='Update Photo Sample', font=('calibri', 13),bd=0,command=self.up_dataset)
        update_photo_btn.grid(row=1, column=2, columnspan=2, padx=2,pady=2)

        right_frame = Frame(f1,bd=0,bg="#499048")
        right_frame.place(x=775, y=95, width=745, height=700)

        rt_lbl = Label(right_frame, text="Student Search", font=("Courier", 12,"bold"),bg="#499048")
        rt_lbl.place(x=0,y=0,width=745)

        Search_frame = LabelFrame(right_frame, text="Search System", bd=2, relief=RIDGE, font=('Courier', 12, 'bold'),bg="#499048")
        Search_frame.place(x=10, y=25, width=725, height=150)

        search_label = Label(Search_frame, text='Search By :', font=('calibri', 13),bg="#499048")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, textvariable=self.var_search, font=('calibri', 13), width=15, state="read only")
        search_combo["values"] = ('Select', 'Roll','Name','Email','Department','Course')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(Search_frame, textvariable=self.var_srch_txt, width=15, font=('calibri', 13))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn = Button(Search_frame, width=13, text='Search', font=('calibri', 13),bd=0,command=self.search_data)
        Search_btn.grid(row=0, column=3, padx=4)

        show_all_btn = Button(Search_frame, width=13, text='Show All', font=('calibri', 13),bd=0,command=self.fetch_data)
        show_all_btn.grid(row=0, column=4, padx=4)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="#499048")
        table_frame.place(x=10, y=180, width=725, height=510)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=('id', 'dep', 'course', 'year', 'sem', 'enroll', 'name', 'gender', 'dob', 'email', 'phone', 'address', 'teacher', 'photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('id', text='ID')
        self.student_table.column('id', width=20)
        self.student_table.heading("dep", text="Department")
        self.student_table.column('dep', width=150)
        self.student_table.heading('course', text='Course')
        self.student_table.column('course', width=80)
        self.student_table.heading('year', text='Year')
        self.student_table.column('year', width=60)
        self.student_table.heading('sem', text='Semester')
        self.student_table.column('sem', width=80)
        self.student_table.heading('enroll', text='Enroll No.')
        self.student_table.column('enroll', width=100)
        self.student_table.heading('name', text='Name')
        self.student_table.column('name', width=100)
        self.student_table.heading('gender', text='Gender')
        self.student_table.column('gender', width=60)
        self.student_table.heading('dob', text='DOB')
        self.student_table.column('dob', width=80)
        self.student_table.heading('email', text='Email')
        self.student_table.column('email', width=200)
        self.student_table.heading('phone', text='Phone')
        self.student_table.column('phone', width=80)
        self.student_table.heading('address', text='Address')
        self.student_table.column('address', width=100)
        self.student_table.heading('teacher', text='Teacher')
        self.student_table.column('teacher', width=100)
        self.student_table.heading('photo', text='PhotoSampleStatus')
        self.student_table.column('photo', width=150)
        self.student_table['show'] = 'headings'

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_enroll.get() == '':
            messagebox.showerror('Error', 'All Fields are Required!', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student (Department, Course, Year, Semester, Enroll, Name, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_enroll.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Student setails has been added Successfully!', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f"Due To :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_enroll.set(data[5]),
        self.var_name.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

    def update_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_enroll.get() == '':
            messagebox.showerror('Error', 'All Fields are Required!', parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this Student Detail!", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root",database="face_app")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        'update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Enroll=%s',
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_enroll.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo('Success', 'Student details successfully Updated!', parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f"Due To :{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_enroll.get() == "":
            messagebox.showerror("Error", 'Enroll No. Required!', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Do you want delete this Student!', parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root",database="face_app")
                    my_cursor = conn.cursor()
                    sql = 'delete from student where Enroll=%s'
                    val = (self.var_enroll.get(),)
                    my_cursor.execute(sql, val)


                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Student successfully deleted!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f"Due To :{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_enroll.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_enroll.get() == '':
            messagebox.showerror('Error', 'All Fields are Required!', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    'update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where ID=%s',
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id
                    ))
                conn.commit()
                self.fetch_data()
                self.abc = str(self.var_id.get())
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user." + str(self.abc) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo('Result', 'Dataset Generated!',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f"Due To :{str(es)}",parent=self.root)

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_app")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student where " + str(self.var_search.get()) + " LIKE '" + str(self.var_srch_txt.get()) + "%'")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def up_dataset(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_enroll.get() == '':
            messagebox.showerror('Error', 'All Fields are Required!', parent=self.root)
        else:
            try:
                self.xyz = str(self.var_id.get())

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user." + str(self.xyz) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo('Result', 'Dataset Updated!',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
