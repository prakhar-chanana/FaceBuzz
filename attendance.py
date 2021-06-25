from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime, time
from datetime import datetime

mydata = []

class Attendance:
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

        self.var_att_id = IntVar()
        self.var_att_id.set("")
        self.var_enroll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()

        ttl_lbl = Label(f1, text=" FACEBUZZ", font=("Courier", 40, "bold"), bg="#499048", fg="red") #006501
        ttl_lbl.place(x=0,y=0,width=1540,height=54)

        wallr = Image.open(r"img\Hotpot.png")
        wallr = wallr.resize((50,50),Image.ANTIALIAS)
        self.w = ImageTk.PhotoImage(wallr)
        f = Label(f1,image=self.w,bg="#499048")
        f.place(x=605,y=0)

        title_lbl = Label(f1, text="Attendance Management System", font=("Courier", 20, "bold"), bg="#499048")
        title_lbl.place(x=0, y=54, width=1540, height=30)

        Left_frame = Frame(f1,bg="#499048")
        Left_frame.place(x=20, y=95, width=745, height=700)

        lf_lbl = Label(Left_frame, text="Student Details", font=("Courier", 12,"bold"),bg="#499048")
        lf_lbl.place(x=0,y=0,width=745)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE,bg="#499048")
        left_inside_frame.place(x=10, y=25, width=725, height=665)

        att_id_label = Label(left_inside_frame, text='Attendance ID :', font=('calibri', 13), bg="#499048")
        att_id_label.grid(row=0, column=0, padx=5, pady=15, sticky=W)

        att_id_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_id, width=22, font=('calibri', 13))
        att_id_entry.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        enroll_label = Label(left_inside_frame, text='Enroll No.:', font=('calibri', 13), bg="#499048")
        enroll_label.grid(row=0, column=2, padx=5, pady=15, sticky=W)

        enroll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_enroll, width=22, font=('calibri', 13))
        enroll_entry.grid(row=0, column=3, padx=5, pady=15, sticky=W)

        name_label = Label(left_inside_frame, text='Name :', font=('calibri', 13),bg="#499048")
        name_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name, width=22, font=('calibri', 13))
        name_entry.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        dep_label = Label(left_inside_frame, text='Department :', font=('calibri', 13),bg="#499048")
        dep_label.grid(row=1, column=2, padx=5, pady=15, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_dep, width=22, font=('calibri', 13))
        dep_entry.grid(row=1, column=3, padx=5, pady=15, sticky=W)

        time_label = Label(left_inside_frame, text='Time :', font=('calibri', 13),bg="#499048")
        time_label.grid(row=2, column=2, padx=5, pady=15, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time, width=22, font=('calibri', 13))
        time_entry.grid(row=2, column=3, padx=5, pady=15, sticky=W)

        course_label = Label(left_inside_frame, text='Course :', font=('calibri', 13),bg="#499048")
        course_label.grid(row=2, column=0, padx=5, pady=15, sticky=W)

        course_entry = ttk.Entry(left_inside_frame, textvariable=self.var_course, width=22, font=('calibri', 13))
        course_entry.grid(row=2, column=1, padx=5, pady=15, sticky=W)

        attendance_status_label = Label(left_inside_frame, text='Attendance Status :', font=('calibri', 13),bg="#499048")
        attendance_status_label.grid(row=3, column=0, padx=5, pady=15, sticky=W)

        attendance_status_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance_status, font=('calibri', 13), width=20, state="read only")
        attendance_status_combo["values"] = ('Status', 'Present', 'Absent')
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=5, pady=15, sticky=W)

        date_label = Label(left_inside_frame, text='Date :', font=('calibri', 13),bg="#499048")
        date_label.grid(row=3, column=2, padx=5, pady=15, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_date, width=22, font=('calibri', 13))
        date_entry.grid(row=3, column=3, padx=5, pady=15, sticky=W)

        btn_frame = Frame(left_inside_frame,bg="#499048")
        btn_frame.place(x=0, y=580, width=718, height=75)

        import_csv_btn = Button(btn_frame, command=self.importCSV, width=39, text='Import csv', font=('calibri', 13),bd=0)
        import_csv_btn.grid(row=0, column=0, columnspan=2, padx=2,pady=2)

        export_csv_btn = Button(btn_frame, command=self.exportCSV, width=39, text='Export csv', font=('calibri', 13),bd=0)
        export_csv_btn.grid(row=0, column=2, columnspan=2, padx=2,pady=2)

        update_btn = Button(btn_frame, width=39, text='Update', font=('calibri', 13),bd=0)
        update_btn.grid(row=1, column=0, columnspan=2, padx=2,pady=2)

        reset_btn = Button(btn_frame, command=self.reset_data, width=39, text='Reset', font=('calibri', 13),bd=0)
        reset_btn.grid(row=1, column=2, columnspan=2, padx=2,pady=2)

        right_frame = Frame(f1, bg="#499048")
        right_frame.place(x=775, y=95, width=745, height=700)

        rt_lbl = Label(right_frame, text="Attendance Details", font=("Courier", 12,"bold"),bg="#499048")
        rt_lbl.place(x=0,y=0,width=745)

        table_frame = Frame(right_frame,bg="#499048",bd=2,relief=RIDGE)
        table_frame.place(x=10, y=25, width=725, height=665)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, columns=('id', 'enroll', 'name', 'dep', 'course', 'time', 'date', 'attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading('id', text='ID')
        self.attendance_table.column('id', width=20)
        self.attendance_table.heading('enroll', text='Enroll No.')
        self.attendance_table.column('enroll', width=100)
        self.attendance_table.heading('name', text='Name')
        self.attendance_table.column('name', width=100)
        self.attendance_table.heading("dep", text="Department")
        self.attendance_table.column('dep', width=150)
        self.attendance_table.heading('course', text='Course')
        self.attendance_table.column('course', width=80)
        self.attendance_table.heading('time', text='Time')
        self.attendance_table.column('time', width=100)
        self.attendance_table.heading('date', text='Date')
        self.attendance_table.column('date', width=100)
        self.attendance_table.heading('attendance', text='Attendance Status')
        self.attendance_table.column('attendance', width=150)
        self.attendance_table['show'] = 'headings'

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No DATA",'No Data found!',parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln, mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Data exported to "+os.path.basename(fln)+" successfully!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        rows = content["values"]

        self.var_att_id.set(rows[0]),
        self.var_enroll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_course.set(rows[4]),
        self.var_time.set(rows[5]),
        self.var_date.set(rows[6]),
        self.var_attendance_status.set(rows[7])

    def reset_data(self):
        self.var_att_id.set("")
        self.var_enroll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_course.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()