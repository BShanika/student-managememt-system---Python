import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win=tk.Tk()
win.geometry("1350x400+0+0")
win.title("Student Mangement System")

style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background="lightgray")
style.configure("TCombobox", fieldbackground="lightgray")
win.configure(bg="gray")

title_label=tk.Label(win,text="Student Management System",font=("Arial",30),border=12,relief=tk.GROOVE,bg="indigo",foreground="white")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Student Records",font=("Arial",15),bg="lightgray",fg="black",bd=7,relief=tk.GROOVE)
detail_frame.place(x=20,y=90,width=470,height=585)

data_frame=tk.Frame(win,bd=7,bg="black",relief=tk.GROOVE)
data_frame.place(x=510,y=90,width=825,height=585)

id=tk.StringVar()
name=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()
grade=tk.StringVar()
address=tk.StringVar()
cno=tk.StringVar()
gname=tk.StringVar()

search_by=tk.StringVar()

id_lbl=tk.Label(detail_frame,text="Student ID",font=('Arial',15),bg="lightgray")
id_lbl.grid(row=0,column=0,padx=2,pady=12)

id_ent=tk.Entry(detail_frame,font=("Arial",15),textvariable=id,bg="lightgray", width=21)
id_ent.grid(row=0,column=1,padx=2,pady=12)

name_lbl=tk.Label(detail_frame,text="Name",font=('Arial',15),bg="lightgray")
name_lbl.grid(row=1,column=0,padx=2,pady=12)

name_ent=tk.Entry(detail_frame,font=("arial",15),textvariable=name,bg="lightgray", width=21)
name_ent.grid(row=1,column=1,padx=2,pady=12)

gender_lbl=tk.Label(detail_frame,text="Gender",font=('Arial',15),bg="lightgray")
gender_lbl.grid(row=2,column=0,padx=2,pady=12)

gender_combobox=ttk.Combobox(detail_frame,font=("arial",15),state="readonly", values=["Male", "Female"],textvariable=gender, width=20)
gender_combobox.grid(row=2,column=1,padx=2,pady=12)
gender_combobox['style'] = 'TCombobox'

dob_lbl=tk.Label(detail_frame,text="Date of Birth",font=('Arial',15),bg="lightgray")
dob_lbl.grid(row=3,column=0,padx=2,pady=12)

dob_ent=tk.Entry(detail_frame,font=("arial",15),textvariable=dob,bg="lightgray", width=21)
dob_ent.grid(row=3,column=1,padx=2,pady=12)

grade_lbl=tk.Label(detail_frame,text="Grade",font=('Arial',15),bg="lightgray")
grade_lbl.grid(row=4,column=0,padx=2,pady=12)

grade_combobox=ttk.Combobox(detail_frame,font=("arial",15),state="readonly", values=["1","2","3","4","5","6","7","8","9","10","11","12","13"],textvariable=grade, width=20)
grade_combobox.grid(row=4,column=1,padx=2,pady=12)
grade_combobox['style'] = 'TCombobox'

address_lbl=tk.Label(detail_frame,text="Address",font=('Arial',15),bg="lightgray")
address_lbl.grid(row=5,column=0,padx=2,pady=12)

address_ent=tk.Entry(detail_frame,font=("arial",15),textvariable=address,bg="lightgray", width=21)
address_ent.grid(row=5,column=1,padx=2,pady=12)

cntctno_lbl=tk.Label(detail_frame,text="Contact No",font=('Arial',15),bg="lightgray")
cntctno_lbl.grid(row=6,column=0,padx=2,pady=12)

cntctno_ent=tk.Entry(detail_frame,font=("arial",15),textvariable=cno,bg="lightgray", width=21)
cntctno_ent.grid(row=6,column=1,padx=2,pady=12)

gname_lbl=tk.Label(detail_frame,text="Guardian's Name",font=('Arial',15),bg="lightgray")
gname_lbl.grid(row=7,column=0,padx=2,pady=12)

gname_ent=tk.Entry(detail_frame,font=("arial",15),textvariable=gname,bg="lightgray", width=21)
gname_ent.grid(row=7,column=1,padx=2,pady=12)


#function
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="std")
    curr=conn.cursor()
    curr.execute("SELECT * FROM data")
    rows=curr.fetchall()
    search_in['values'] = [row[0] for row in rows]
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

def add_func():
    if id.get()=="" or name.get()=="" :
        messagebox.showerror("Error!", "Please fill all the fields")  
    else:
        conn=pymysql.connect(host="localhost",user="root",password="",database="std") 
        curr=conn.cursor()
        query = "INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (id.get(), name.get(), gender.get(), dob.get(), grade.get(), address.get(), cno.get(), gname.get())
        curr.execute(query, values)
        conn.commit()
        conn.close()
        fetch_data()
        
def get_cursor(event):
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content['values']
    id.set(row[0])
    name.set(row[1])
    gender.set(row[2])
    dob.set(row[3])
    grade.set(row[4])
    address.set(row[5])
    cno.set(row[6])
    gname.set(row[7])
    
def clear_func():
    id.set("")
    name.set("")
    gender.set("")
    dob.set("")
    grade.set("")
    address.set("")
    cno.set("")
    gname.set("")
    search_in.set("")
    
    
def update_func():
   conn=pymysql.connect(host="localhost",user="root",password="",database="std") 
   curr=conn.cursor()  
   update_query = ("UPDATE data ""SET Name=%s, Gender=%s, DOB=%s, Grade=%s, Address=%s, Contact_No=%s, Guardian_Name=%s " "WHERE ID=%s")
   curr.execute(update_query, (name.get(), gender.get(), dob.get(), grade.get(), address.get(), cno.get(), gname.get(),id.get()))
   conn.commit()
   conn.close()
   fetch_data()
   clear_func()
   
def delete_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="std")
    curr = conn.cursor()
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showwarning("No item selected", "Please select a record to delete.")
        return

    confirmation = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this record?")
    if confirmation:
        for item in selected_item:
            content = student_table.item(item)
            row = content['values']
            curr.execute("DELETE FROM data WHERE ID = %s", row[0])
    conn.commit()
    conn.close()
    fetch_data()
    
def search_func():
    search_id = search_in.get()
    conn = pymysql.connect(host="localhost", user="root", password="", database="std")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data WHERE ID = %s", search_id)
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
        conn.commit()
    else:
        messagebox.showinfo("No Results", "No matching record found.")
    conn.close()
    
def view_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="std")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
    else:
        messagebox.showinfo("No records", "There are no records in the database.")
    conn.close()

  
#button
btn_frame=tk.Frame(detail_frame,bg="lightgray",relief=tk.GROOVE)
btn_frame.place(x=50,y=425,width=370,height=120)

add_btn=tk.Button(btn_frame,text="Add",font=('Arial',13),bg="gray",width=14,bd=9,command=add_func)
add_btn.grid(row=0,column=0,padx=12,pady=2)

update_btn=tk.Button(btn_frame,text="Update",font=('Arial',13),bg="gray",width=14,bd=9,command=update_func)
update_btn.grid(row=0,column=1,padx=12,pady=2)

clear_btn=tk.Button(btn_frame,text="Clear",font=('Arial',13),bg="gray",width=14,bd=9,command=clear_func)
clear_btn.grid(row=1,column=0,padx=12,pady=2)

delete_btn=tk.Button(btn_frame,text="Delete",font=('Arial',13),bg="gray",width=14,bd=9,command=delete_func)
delete_btn.grid(row=1,column=1,padx=12,pady=2)

#dataframe
search_frame=tk.Frame(data_frame,bg="lightgray",relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search",bg="lightgray",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",14),state="readonly",values=[id.get()])
search_in.grid(row=0,column=1,padx=12,pady=2)
search_in['style'] = 'TCombobox'

search_btn=tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=14,bg="gray",command=search_func)
search_btn.grid(row=0,column=2,padx=12,pady=2)

view_btn=tk.Button(search_frame,text="View",font=("Arial",13),bd=9,width=14,bg="gray",command=view_func)
view_btn.grid(row=0,column=3,padx=12,pady=2)

#database
main_frame=tk.Frame(data_frame,bg="lightgray",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Std ID","Name","Gender","DOB","Grade","Address","Contact No","Guardian's Name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Std ID",text="Std ID")
student_table.heading("Name",text="Name")
student_table.heading("Gender",text="Gender")
student_table.heading("DOB",text="DOB")
student_table.heading("Grade",text="Grade")
student_table.heading("Address",text="Address")
student_table.heading("Contact No",text="Contact No")
student_table.heading("Guardian's Name",text="Guardian's Name")

student_table['show']='headings'

student_table.column("Std ID",width=100)
student_table.column("Name",width=100)
student_table.column("Gender",width=100)
student_table.column("DOB",width=100)
student_table.column("Grade",width=100)
student_table.column("Address",width=100)
student_table.column("Contact No",width=100)
student_table.column("Guardian's Name",width=100)

student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

win.mainloop()
