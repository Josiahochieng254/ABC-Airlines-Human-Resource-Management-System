import tkinter as tk
import mysql.connector
from tkinter import messagebox
import datetime
import bcrypt
from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from twilio.rest import Client
import time
import threading
import smtplib
import io
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import Image, ImageTk


def call_AlertsNotifications():
    win1 = Toplevel(root)
    c_AlertsNotifications = AlertsNotifications
    c_AlertsNotifications(win1)
    return


def call_TaskAllocation():
    win2 = Toplevel(root)
    c_TaskAllocation = TaskAllocation
    c_TaskAllocation(win2)
    return


def call_BudgetForecasting():
    win3 = Toplevel(root)
    c_BudgetForecasting = BudgetForecasting
    c_BudgetForecasting(win3)


def call_SendEmail():
    win4 = Toplevel(root)
    c_SendEmail = SendEmail
    c_SendEmail(win4)


def call_CreateAccount():
    win5 = Toplevel(root)
    c_CreateAccount = CreateAccount
    c_CreateAccount(win5)
    return


def call_HrCreateAccount():
    win15 = Toplevel(root)
    c_HrCreateAccount = HrCreateAccount
    c_HrCreateAccount(win15)
    return


def call_ViewLeaveApplication():
    win6 = Toplevel(root)
    c_ViewLeaveApplication = ViewLeaveApplication
    c_ViewLeaveApplication(win6)
    return


class Employee:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        # Variables
        self.var_department = StringVar()
        self.var_designation = StringVar()
        self.var_address = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_marital_status = StringVar()
        self.var_date_of_joining = StringVar()
        self.var_gender = StringVar()
        self.var_phone_number = StringVar()
        self.var_id_number = StringVar()
        self.var_salary = StringVar()

        label_title = Label(self.root, text='ABC HUMAN RESOURCE MANAGEMENT SYSTEM', font=('times new roman', 35, 'bold'),
                            fg='darkblue', bg='white')
        label_title.place(x=0, y=0, width=1530, height=50)
        # logo
        image_logo = Image.open('company_images/logo.jpg')
        image_logo = image_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(image_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)
        # Image frame
        image_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        image_frame.place(x=0, y=50, width=1340, height=150)
        # 1st
        image = Image.open('company_images/employee_rep.jpg')
        image = image.resize((1490, 150), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.image = Label(self.root, image=self.photo)
        self.image.place(x=0, y=50, width=1510, height=160)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=8, y=220, width=1340, height=500)

        # Upper Frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                 font=('times new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=8, y=8, width=1320, height=210)

        # Labels and Entry Fields
        label_department = Label(upper_frame, text='Department:', font=('ariel', 11, 'bold'),
                                 bg='white')
        label_department.grid(row=0, column=0, padx=2, sticky=W)

        combo_department = ttk.Combobox(upper_frame, textvariable=self.var_department,
                                        font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_department['value'] = (
            'Select Department', 'HR', 'Software Engineer', 'Manager', 'Accountant', 'Receptionist', 'Secretary',
            'Staff')
        combo_department.current(0)
        combo_department.grid(row=0, column=1, padx=25, pady=7, sticky=W)

        # Label Designation
        label_designation = Label(upper_frame, text='Designation:', font=('ariel', 11, 'bold'),
                                  bg='white')
        label_designation.grid(row=1, column=0, padx=2, pady=7, sticky=W)
        text_designation = ttk.Entry(upper_frame, textvariable=self.var_designation, width=25,
                                     font=("arial", 11, 'bold'))
        text_designation.grid(row=1, column=1, pady=7, padx=25, sticky=W)

        # Address
        label_address = Label(upper_frame, text='Address:', font=('ariel', 11, 'bold'),
                              bg='white')
        label_address.grid(row=2, column=0, padx=2, pady=7, sticky=W)
        text_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=25,
                                 font=("arial", 11, 'bold'))
        text_address.grid(row=2, column=1, pady=7, padx=25, sticky=W)

        # Date of birth
        label_date_of_birth = Label(upper_frame, text='DateOfBirth:', font=('ariel', 11, 'bold'),
                                    bg='white')
        label_date_of_birth.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        text_date_of_birth = ttk.Entry(upper_frame, textvariable=self.var_date_of_birth, width=25,
                                       font=("arial", 11, 'bold'))
        text_date_of_birth.grid(row=3, column=1, pady=7, padx=25, sticky=W)

        button_budget_forecasting = Button(upper_frame, text='BudgetForecasting ',
                                           font=('arial', 11, 'bold'), width=18, bg='blue',
                                           command=call_BudgetForecasting)
        button_budget_forecasting.grid(row=4, column=1, padx=2)

        # Name
        label_name = Label(upper_frame, text='Name:', font=('ariel', 11, 'bold'),
                           bg='white')
        label_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        text_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=30, font=("arial", 11, 'bold'))
        text_name.grid(row=0, column=3, pady=7, padx=25)

        # Email
        label_email = Label(upper_frame, text='Email:', font=('ariel', 11, 'bold'),
                            bg='white')
        label_email.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        text_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=30,
                               font=("arial", 11, 'bold'))
        text_email.grid(row=1, column=3, pady=7, padx=25)
        # Marital status
        label_marital_status = Label(upper_frame, text='Marital Status:', font=('ariel', 11, 'bold'),
                                     bg='white')
        label_marital_status.grid(row=2, column=2, padx=2, sticky=W)

        combo_marital_status = ttk.Combobox(upper_frame, textvariable=self.var_marital_status,
                                            font=('arial', 12, 'bold'), width=25, state='readonly')
        combo_marital_status['value'] = ('Married', 'Unmarried')
        combo_marital_status.current(0)
        combo_marital_status.grid(row=2, column=3, padx=25, pady=7, sticky=W)

        # Date Of Joining
        label_date_of_joining = Label(upper_frame, text='DateOfJoining:', font=('ariel', 11, 'bold'),
                                      bg='white')
        label_date_of_joining.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        text_date_of_joining = ttk.Entry(upper_frame, textvariable=self.var_date_of_joining, width=30,
                                         font=("arial", 11, 'bold'))
        text_date_of_joining.grid(row=3, column=3, pady=7, padx=25)

        button_leave_approval = Button(upper_frame, text='LeaveApproval ',
                                       font=('arial', 11, 'bold'), width=18, bg='blue',
                                       command=call_ViewLeaveApplication)
        button_leave_approval.grid(row=4, column=3, padx=2)

        # Gender
        label_gender = Label(upper_frame, text='Gender:', font=('ariel', 11, 'bold'),
                             bg='white')
        label_gender.grid(row=0, column=4, padx=2, sticky=W)

        combo_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 12, 'bold'),
                                    width=20, state='readonly')
        combo_gender['value'] = ('Male', 'Female')
        combo_gender.current(0)
        combo_gender.grid(row=0, column=5, padx=25, pady=7, sticky=W)

        # phone number
        label_phone_number = Label(upper_frame, text='Phone No:', font=('ariel', 11, 'bold'),
                                   bg='white')
        label_phone_number.grid(row=1, column=4, padx=2, pady=7, sticky=W)
        text_phone_number = ttk.Entry(upper_frame, textvariable=self.var_phone_number, width=25,
                                      font=("arial", 11, 'bold'))
        text_phone_number.grid(row=1, column=5, pady=7, padx=25)

        # Identification Number
        label_id_number = Label(upper_frame, text='Id No:', font=('ariel', 11, 'bold'),
                                bg='white')
        label_id_number.grid(row=2, column=4, padx=2, pady=7, sticky=W)
        text_id_number = ttk.Entry(upper_frame, textvariable=self.var_id_number, width=25,
                                   font=("arial", 11, 'bold'))
        text_id_number.grid(row=2, column=5, pady=7, padx=25)

        # Salary
        label_salary = Label(upper_frame, text='Salary:', font=('ariel', 11, 'bold'),
                             bg='white')
        label_salary.grid(row=3, column=4, padx=2, pady=7, sticky=W)
        text_salary = ttk.Entry(upper_frame, textvariable=self.var_salary, width=25,
                                font=("arial", 11, 'bold'))
        text_salary.grid(row=3, column=5, pady=7, padx=25)

        # Add user Button

        button_add_user = Button(upper_frame, text='Add User', command=call_CreateAccount,
                                 font=('arial', 11, 'bold'), width=18, bg='blue')
        button_add_user.grid(row=4, column=5, padx=2)

        # Button Frames
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1180, y=1, width=120, height=180)
        # Save Button
        button_save = Button(button_frame, text='Save', command=self.add_data, font=('arial', 15, 'bold'),
                             width=9, bg='blue', fg='white')
        button_save.grid(row=0, column=0, padx=2, pady=1)
        # Update Button
        button_update = Button(button_frame, text='Update', command=self.update_data,
                               font=('arial', 15, 'bold'), width=9, bg='blue', fg='white')
        button_update.grid(row=1, column=0, padx=2, pady=1)
        # Delete Button
        button_delete = Button(button_frame, text='Delete', command=self.delete_data,
                               font=('arial', 15, 'bold'), width=9, bg='blue', fg='white')
        button_delete.grid(row=2, column=0, padx=2, pady=1)
        # Clear Button
        button_clear = Button(button_frame, text='Clear', command=self.reset_data,
                              font=('arial', 15, 'bold'), width=9, bg='blue', fg='white')
        button_clear.grid(row=3, column=0, padx=2, pady=1)

        # Down Frame
        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white',
                                text='Employee Information Table', font=('times new roman', 11, 'bold'),
                                fg='red')
        down_frame.place(x=8, y=220, width=1320, height=270)
        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                  text='Search Employee Information', font=('times new roman', 11, 'bold'),
                                  fg='red')
        search_frame.place(x=0, y=0, width=1317, height=60)
        # Search
        search_by = Label(search_frame, font=('arial', 11, 'bold'), text='Search By:', fg='white',
                          bg='red')
        search_by.grid(row=0, column=0, sticky=W, padx=5, pady=3)

        # Search
        self.var_combo_search = StringVar()
        combo_search_by_option = ttk.Combobox(search_frame, textvariable=self.var_combo_search,
                                              font=('arial', 12, 'bold'), width=21, state='readonly')
        combo_search_by_option['value'] = ('Select Option', 'phone_number', 'id_number')
        combo_search_by_option.current(0)
        combo_search_by_option.grid(row=0, column=1, padx=15, pady=1, sticky=W)

        self.var_search = StringVar()
        text_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22,
                                font=('arial', 11, 'bold'))
        text_search.grid(row=0, column=2, padx=20)

        button_search = Button(search_frame, text='Search', command=self.search_data,
                               font=('arial', 11, 'bold'),
                               width=14, bg='blue')
        button_search.grid(row=0, column=3, padx=2)

        button_show_all = Button(search_frame, text='Show All', command=self.fetch_data,
                                 font=('arial', 11, 'bold'),
                                 width=14, bg='blue')
        button_show_all.grid(row=0, column=4, padx=5)

        button_notifications = Button(search_frame, text='Notifications',
                                      font=('arial', 11, 'bold'), width=14, bg='blue',
                                      command=call_AlertsNotifications)
        button_notifications.grid(row=0, column=5, padx=5)

        button_sending_emails = Button(search_frame, text='SendingEmails',
                                       font=('arial', 11, 'bold'), width=14, bg='blue',
                                       command=call_SendEmail)
        button_sending_emails.grid(row=0, column=6, padx=5)

        button_task_allocation = Button(search_frame, text='TaskAllocation',
                                        font=('arial', 11, 'bold'), width=14, bg='blue',
                                        command=call_TaskAllocation)
        button_task_allocation.grid(row=0, column=7, padx=5)

        #   Employee Table
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1320, height=180)
        #  Scroll Bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(table_frame,
                                           columns=('department', 'designation', 'address', 'date_of_birth',
                                                    'name', 'email', 'marital_status', 'date_of_joining', 'gender'
                                                    , 'phone_number', 'id_number', 'salary',
                                                    )
                                           , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('department', text='Department')
        self.employee_table.heading('designation', text='Designation')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('date_of_birth', text='Date_Of_Birth')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('marital_status', text='Marital_Status')
        self.employee_table.heading('date_of_joining', text='Date_Of_Joining')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone_number', text='Phone_Number')
        self.employee_table.heading('id_number', text='Id_No')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('department', width=150)
        self.employee_table.column('designation', width=150)
        self.employee_table.column('address', width=150)
        self.employee_table.column('date_of_birth', width=150)
        self.employee_table.column('name', width=200)
        self.employee_table.column('email', width=200)
        self.employee_table.column('marital_status', width=150)
        self.employee_table.column('date_of_joining', width=150)
        self.employee_table.column('gender', width=150)
        self.employee_table.column('phone_number', width=150)
        self.employee_table.column('id_number', width=150)
        self.employee_table.column('salary', width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Declaration

    def add_data(self):
        if self.var_department.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                               database='employee_mng_system')
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "CREATE TABLE IF NOT EXISTS employees (department VARCHAR(255), designation VARCHAR(255), address VARCHAR(255),"
                    "date_of_birth VARCHAR(255),name VARCHAR(255),email VARCHAR(255),marital_status VARCHAR(255),date_of_joining VARCHAR(255),"
                    "gender VARCHAR(255),phone_number VARCHAR(255),id_number VARCHAR(255),salary VARCHAR(255))")

                my_cursor.execute('insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_department.get(),
                    self.var_designation.get(),
                    self.var_address.get(),
                    self.var_date_of_birth.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_marital_status.get(),
                    self.var_date_of_joining.get(),
                    self.var_gender.get(),
                    self.var_phone_number.get(),
                    self.var_id_number.get(),
                    self.var_salary.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added', parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror('Error'f'Due To:{str(es)}', parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                       database='employee_mng_system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employees ')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_department.set(data[0])
        self.var_designation.set(data[1])
        self.var_address.set(data[2])
        self.var_date_of_birth.set(data[3])
        self.var_name.set(data[4])
        self.var_email.set(data[5])
        self.var_marital_status.set(data[6])
        self.var_date_of_joining.set(data[7])
        self.var_gender.set(data[8])
        self.var_phone_number.set(data[9])
        self.var_id_number.set(data[10])
        self.var_salary.set(data[11])

    def update_data(self):
        if self.var_department.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are You Sure You Want To Update This Employee Data ?')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                                   database='employee_mng_system')
                    my_cursor = conn.cursor()
                    my_cursor.execute('UPDATE employees set department=%s,designation=%s,address=%s,'
                                      'date_of_birth=%s,name=%s,email=%s,marital_status=%s,date_of_joining=%s,'
                                      'gender=%s,phone_number=%s,salary=%s WHERE id_number=%s', (

                                          self.var_department.get(),
                                          self.var_designation.get(),
                                          self.var_address.get(),
                                          self.var_date_of_birth.get(),
                                          self.var_name.get(),
                                          self.var_email.get(),
                                          self.var_marital_status.get(),
                                          self.var_date_of_joining.get(),
                                          self.var_gender.get(),
                                          self.var_phone_number.get(),
                                          self.var_salary.get(),
                                          self.var_id_number.get()
                                      ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('success', 'Employee Successfully Updated', parent=self.root)

                else:
                    if not update:
                        return

            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_id_number.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                Delete = messagebox.askyesno('DELETE', 'ARE YOU SURE YOU WANT TO DELETE THIS EMPLOYEE DATA?',
                                             parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                                   database='employee_mng_system')
                    my_cursor = conn.cursor()
                    sql = 'DELETE from employees WHERE Id_Number=%s'
                    value = (self.var_id_number.get(),)
                    my_cursor.execute(sql, value)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Delete', 'Employee Successfully Deleted', parent=self.root)
                else:
                    if not Delete:
                        return
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    # Reset
    def reset_data(self):
        self.var_department.set('Select Department')
        self.var_designation.set('')
        self.var_address.set('')
        self.var_date_of_birth.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_marital_status.set('Marital_status')
        self.var_date_of_joining.set('')
        self.var_gender.set('Gender')
        self.var_phone_number.set('')
        self.var_id_number.set('')
        self.var_salary.set('')

    # Search
    def search_data(self):
        if self.var_combo_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                               database='employee_mng_system')
                my_cursor = conn.cursor()
                # The LIKE operator is used with the WHERE statement to search for a specific pattern in the table.
                # Suppose you want to search for values which start with “a” in the table, the LIKE statement is used
                # in such scenarios.
                my_cursor.execute(
                    'select * from employees where ' + str(self.var_combo_search.get()) + " LIKE'%" + str(
                        self.var_search.get() + "%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Error", "There Is No Such Employee")

                conn.commit()
                conn.close()

            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)


class AlertsNotifications:
    def __init__(self, root):
        self.root = root
        self.root.title("Alerts and Notifications")
        root.geometry("400x400+550+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_phone = tk.Label(root, text="PhoneNumber(+254):", bg="#0e21f1", font=('arial', 9, 'bold'))
        self.label_phone.place(x=0, y=10, width=130, height=30)

        self.entry_phone = tk.Entry(root)
        self.entry_phone.place(x=160, y=10, width=150, height=30)

        self.label_message = tk.Label(root, text="Message", bg="#0e21f1", font=('arial', 9, 'bold'))
        self.label_message.place(x=160, y=50, width=150, height=30)

        self.text_message = tk.Text(root, height=10, width=40, font=('arial', 9, 'bold'), bg="#0064ff")
        self.text_message.place(x=0, y=100, width=400, height=100)

        self.button_submit = tk.Button(root, text="Send", command=self.submit, bg="#14b3eb", font=('arial', 9, 'bold'))
        self.button_submit.place(x=160, y=220, width=150, height=30)

        self.button_send_to_all = tk.Button(root, text="Send To All", command=self.submit, bg="#14b3eb",
                                            font=('arial', 9, 'bold'))
        self.button_send_to_all.place(x=160, y=260, width=150, height=30)

        self.textbox = tk.Text(root, height=10, width=40, bg="#0064ff", font=('arial', 9, 'bold'))
        self.textbox.place(x=0, y=300, width=400, height=100)

    def submit(self):
        phone = self.entry_phone.get()
        message = self.text_message.get("1.0", tk.END)

        if self.entry_phone.get() == "" or self.text_message.get("1.0", tk.END) == "":
            tk.messagebox.showerror("Error", "Please enter both phone number and a message")
            return

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )
            # Create the 'notifications' table if it does not exist
            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS notifications (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255), timestamp DATETIME)")
            # Insert the notification record into the database
            sql = "INSERT INTO notifications (phone, message, timestamp) VALUES (%s,%s, NOW())"
            val = (phone, message,)
            mycursor.execute(sql, val)
            mydb.commit()
            # Send SMS notification using Twilio API
            account_sid = 'AC84e2709a5a0c2ca5a14a73a2c9e389e2'
            auth_token = '677880bb383d4b988f3c4d56b5144c0e'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message,
                from_='+15747667023',  # Twilio phone number
                to=phone
            )
            tk.messagebox.showinfo("SMS notification sent to", phone)
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{message} has been added to the database\n")

        # Start a new thread to display the notification
        t = threading.Thread(target=self.display_notification, args=(message,))
        t.start()

    def display_notification(self, message):
        # Wait for 10 seconds before displaying the notification
        time.sleep(10)

        # Show the notification in a message box
        tk.messagebox.showinfo("Notification", message)


class SendEmail:
    def __init__(self, root):
        self.root = root
        self.root.title("Send Email")
        root.geometry("400x400+450+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_recipient = tk.Label(root, text="Recipient:", bg="#0e21f1", font=('arial', 9, 'bold'))
        self.label_recipient.place(x=0, y=10, width=130, height=30)

        self.entry_recipient = tk.Entry(root)
        self.entry_recipient.place(x=160, y=10, width=150, height=30)

        self.label_subject = tk.Label(root, text="Subject:", bg="#0e21f1", font=('arial', 9, 'bold'))
        self.label_subject.place(x=0, y=50, width=130, height=30)

        self.entry_subject = tk.Entry(root)
        self.entry_subject.place(x=160, y=50, width=150, height=30)

        self.label_message = tk.Label(root, text="Message:", bg="#0e21f1", font=('arial', 9, 'bold'))
        self.label_message.place(x=160, y=90, width=150, height=30)

        self.text_message = tk.Text(root, height=10, width=40, font=('arial', 9, 'bold'))
        self.text_message.place(x=0, y=140, width=400, height=100)

        self.button_send = tk.Button(root, text="Send", command=self.send_email, bg="#14b3eb",
                                     font=('arial', 9, 'bold'))
        self.button_send.place(x=160, y=270, width=150, height=30)

        self.button_send_to_all = tk.Button(root, text="Send To All", command=self.send_email, bg="#14b3eb",
                                            font=('arial', 9, 'bold'))
        self.button_send_to_all.place(x=160, y=310, width=150, height=30)

    def send_email(self):
        recipient = self.entry_recipient.get()
        subject = self.entry_subject.get()
        message = self.text_message.get("1.0", tk.END)

        if not recipient:
            tk.messagebox.showerror("Error", "Please enter a recipient")
            return
        if not subject:
            tk.messagebox.showerror("Error", "Please enter a subject")
            return
        if not message:
            tk.messagebox.showerror("Error", "Please enter a message")
            return

        try:
            # Send the email using SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('cmuriithi866@gmail.com', 'sneszhfirikahiuw')
            server.sendmail('cmuriithi866@gmail.com', recipient, f'Subject: {subject}\n\n{message}')
            server.close()
        except smtplib.SMTPException as e:
            tk.messagebox.showerror("Error", f"Error sending email: {str(e)}")
            return

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )

            # Create the 'emails' table if it does not exist
            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS emails (id INT AUTO_INCREMENT PRIMARY KEY, recipient VARCHAR(255), subject VARCHAR(255), message TEXT, timestamp DATETIME)")
            # Insert the email record into the database
            sql = "INSERT INTO emails (recipient, subject, message,timestamp) VALUES (%s, %s, %s,NOW())"
            val = (recipient, subject, message)
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        tk.messagebox.showinfo("Success", "Email sent and record added to the database.")


class TaskAllocation:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Allocation")
        root.geometry("400x400+400+150")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create the task entry fields
        self.task_name_label = tk.Label(root, text="Task Name:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.task_name_label.place(x=0, y=10, width=130, height=30)
        self.task_name_entry = tk.Entry(root, font=('arial', 10, 'bold'))
        self.task_name_entry.place(x=160, y=10, width=150, height=30)

        self.assigned_user_label = tk.Label(root, text="Assigned To:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.assigned_user_label.place(x=0, y=50, width=130, height=30)
        self.assigned_user_entry = tk.Entry(root, font=('arial', 10, 'bold'))
        self.assigned_user_entry.place(x=160, y=50, width=150, height=30)

        self.status_label = tk.Label(root, text="Status:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.status_label.place(x=160, y=90, width=150, height=30)
        self.status_entry = tk.Entry(root, font=('arial', 10, 'bold'))
        self.status_entry.place(x=160, y=50, width=150, height=30)

        # Create the task allocation and view tasks buttons
        self.allocate_button = tk.Button(root, text="Allocate Task", font=('arial', 10, 'bold'),
                                         bg="#14b3eb", command=self.allocate_task)
        self.allocate_button.place(x=160, y=90, width=150, height=30)

        self.view_button = tk.Button(root, text="View Allocated Tasks", font=('arial', 10, 'bold'),
                                     bg="#14b3eb", command=self.view_tasks)
        self.view_button.place(x=160, y=130, width=150, height=30)

        # Create the task listbox
        self.task_listbox = tk.Listbox(root, font=('arial', 10, 'bold'), bg='black', fg='green')
        self.task_listbox.place(x=0, y=180, width=400, height=220)

        # Function to allocate tasks to users

    def allocate_task(self):
        # Get the task name, assigned user, and status from the user
        task_name = self.task_name_entry.get()
        assigned_user = self.assigned_user_entry.get()
        status = self.status_entry.get()

        if self.task_name_entry.get() == "" or self.assigned_user_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            # Create a connection to MySQL database
            db = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )

            # Create a cursor to interact with the database
            cursor = db.cursor()

            # Create the tasks table if it doesn't exist
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), assigned_to VARCHAR(255), status VARCHAR(255))")
            # Insert the task into the database
            sql = "INSERT INTO tasks (name, assigned_to, status) VALUES (%s, %s, %s)"
            values = (task_name, assigned_user, status)
            cursor.execute(sql, values)
            db.commit()

            # Show a message box confirming the task allocation
            messagebox.showinfo("Task Allocation", "Task allocated successfully!")

            # Clear the task entry fields
            self.task_name_entry.delete(0, END)
            self.assigned_user_entry.delete(0, END)
            self.status_entry.delete(0, END)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

    # Function to view allocated tasks
    def view_tasks(self):
        # Clear the listbox
        self.task_listbox.delete(0, END)

        # Select all tasks from the database
        select_query = "SELECT * FROM tasks"
        cursor.execute(select_query)
        tasks = cursor.fetchall()

        # Add each task to the listbox
        for task in tasks:
            self.task_listbox.insert(END, f"{task[1]} - Assigned to: {task[2]} - Status: {task[3]}")


class BudgetForecasting:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Forecasting")
        root.geometry("400x400+550+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_category = tk.Label(root, text="Category:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.label_category.place(x=0, y=10, width=130, height=30)

        self.entry_category = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_category.place(x=160, y=10, width=150, height=30)

        self.label_amount = tk.Label(root, text="Amount:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.label_amount.place(x=0, y=50, width=130, height=30)

        self.entry_amount = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_amount.place(x=160, y=50, width=150, height=30)

        self.label_month = tk.Label(root, text="Month:", bg="#0e21f1", font=('arial', 10, 'bold'))
        self.label_month.place(x=0, y=90, width=130, height=30)

        self.entry_month = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_month.place(x=160, y=90, width=150, height=30)

        self.button_submit = tk.Button(root, text="Submit", command=self.submit, font=('arial', 10, 'bold'),
                                       bg="#14b3eb")
        self.button_submit.place(x=160, y=140, width=150, height=30)

        self.textbox = tk.Text(root, height=10, width=40, font=('arial', 10, 'bold'), bg='black', fg='green')
        self.textbox.place(x=0, y=180, width=400, height=230)

    def submit(self):
        category = self.entry_category.get()
        amount = self.entry_amount.get()
        month = self.entry_month.get()

        if not category:
            tk.messagebox.showerror("Error", "Please enter a category")
            return

        if not amount:
            tk.messagebox.showerror("Error", "Please enter an amount")
            return

        if not month:
            tk.messagebox.showerror("Error", "Please enter a month")
            return

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )

            # Create the 'expenses' table if it does not exist
            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS expenses (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(255), amount DECIMAL(10, 2), month VARCHAR(255))")

            # Insert the expense record into the database
            sql = "INSERT INTO expenses (category, amount, month) VALUES (%s, %s, %s)"
            val = (category, amount, month)
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{category} for {month} has been added to the database\n")


# Create a connection to MySQL database
mydb = mysql.connector.connect(
    host='localhost', username='root', password='locoz0227',
    database='employee_mng_system'
)

# Create a cursor to interact with the database
cursor = mydb.cursor()


class ViewLeaveApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("LeaveApplication")
        root.geometry("400x400+350+200")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create the leave entry fields
        self.label_name = tk.Label(root, text="Name:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_name.place(x=0, y=10, width=130, height=30)

        self.entry_name = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_name.place(x=160, y=10, width=150, height=30)

        self.label_status = tk.Label(root, text="Status:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_status.place(x=0, y=50, width=130, height=30)

        self.entry_status = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_status.place(x=160, y=50, width=150, height=30)

        # Create the leave application and view leave status buttons
        self.button_update_status = tk.Button(root, text="Update Status", font=('arial', 10, 'bold'),
                                              command=self.approve_leave, bg="#14b3eb")
        self.button_update_status.place(x=0, y=90, width=130, height=30)

        self.button_view = tk.Button(root, text="View Leave Status", font=('arial', 10, 'bold'),
                                     command=self.view_leaves, bg="#14b3eb")
        self.button_view.place(x=160, y=90, width=150, height=30)

        # Create the leave listbox
        self.listbox_leave = tk.Listbox(root, height=10, width=35, font=('arial', 10, 'bold'),
                                        bg='black', fg='green')
        self.listbox_leave.place(x=0, y=140, width=400, height=270)

    # Function to apply for leave
    def approve_leave(self):
        try:
            update = messagebox.askyesno('Update', 'Are You Sure You Want To Update This Employee Data ?')
            if update > 0:
                # Create a connection to MySQL database
                mydb = mysql.connector.connect(
                    host='localhost', username='root', password='locoz0227',
                    database='employee_mng_system'
                )

                # Create a cursor to interact with the database
                cursor = mydb.cursor(buffered=True)
                # Create the 'expenses' table if it does not exist
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS leaves (status VARCHAR(255), name VARCHAR(255))")

                # Insert the leave approval into the database
                cursor.execute("UPDATE leaves SET status=%s WHERE name=%s",
                               (self.entry_status.get(), self.entry_name.get()))
                mydb.commit()
                messagebox.showinfo("Success", "Leave status updated successfully")

                # Clear the leave entry fields
                self.entry_name.delete(0, END)
                self.entry_status.delete(0, END)

        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

    # Function to view leave status
    def view_leaves(self):
        # Clear the listbox
        self.listbox_leave.delete(0, END)

        # Select all leave applications from the database
        select_query = "SELECT * FROM leaves"
        cursor.execute(select_query)
        leaves = cursor.fetchall()

        # Add each leave application to the listbox
        for leave in leaves:
            self.listbox_leave.insert(END,
                                      f"{leave[1]} - Start Date: {leave[2]} - End Date: {leave[3]} - Reason: {leave[4]} - Status: {leave[5]}")


def call_AttendanceTracker():
    win7 = Toplevel(root)
    c_AttendanceTracker = AttendanceTracker
    c_AttendanceTracker(win7)
    return


def call_AbsenceManager():
    win8 = Toplevel(root)
    c_AbsenceManager = AbsenceManager
    c_AbsenceManager(win8)
    return


def call_EmployeePortal():
    win9 = Toplevel(root)
    c_EmployeePortal = EmployeePortal
    c_EmployeePortal(win9)
    return


def call_LeaveApplication():
    win10 = Toplevel(root)
    c_LeaveApplication = LeaveApplication
    c_LeaveApplication(win10)
    return


def call_ImageView():
    win16 = Toplevel(root)
    c_ImageView = ImageView
    c_ImageView(win16)
    return


class User:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        label_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'),
                            fg='darkblue', bg='white')
        label_title.place(x=0, y=0, width=1530, height=50)
        # logo
        image_logo = Image.open('company_images/logo.jpeg')
        image_logo = image_logo.resize((50, 50), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image_logo)

        root.logo = Label(self.root, image=root.photo_logo)
        root.logo.place(x=270, y=0, width=50, height=50)
        # Image frame
        image_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        image_frame.place(x=0, y=50, width=1340, height=150)
        # 1st
        image = Image.open('company_images/employee_rep.jpeg')
        image = image.resize((1490, 150), Image.LANCZOS)
        root.photo = ImageTk.PhotoImage(image)

        root.image = Label(self.root, image=root.photo)
        root.image.place(x=0, y=50, width=1510, height=160)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=8, y=220, width=1340, height=500)

        # Upper Frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                 font=('times new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=8, y=8, width=1320, height=210)

        # Button Frames
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1180, y=1, width=120, height=180)
        # Save Button
        button_attendance = Button(button_frame, text='Attendance', font=('arial', 15, 'bold'), width=9,
                                   bg='blue', fg='white', command=call_AttendanceTracker)
        button_attendance.grid(row=0, column=0, padx=2, pady=1)
        # Update Button
        button_AbsenceManagement = Button(button_frame, text='AbsenceM', font=('arial', 15, 'bold'),
                                          width=9, bg='blue', fg='white', command=call_AbsenceManager)
        button_AbsenceManagement.grid(row=1, column=0, padx=2, pady=1)
        # Delete Button
        button_EmployeePortal = Button(button_frame, text='EmployeeP', font=('arial', 15, 'bold'),
                                       width=9, bg='blue', fg='white', command=call_EmployeePortal)
        button_EmployeePortal.grid(row=2, column=0, padx=2, pady=1)
        # Clear Button
        button_Leave_Application = Button(button_frame, text='LeaveApp', font=('arial', 15, 'bold'),
                                          width=9,
                                          bg='blue', fg='white', command=call_LeaveApplication)
        button_Leave_Application.grid(row=3, column=0, padx=2, pady=1)


class AttendanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Attendance Tracker")
        root.geometry("400x400+450+350")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_name = tk.Label(root, text="Enter Your Names:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_name.place(x=0, y=10, width=130, height=30)

        self.entry_name = tk.Entry(root, width=25, font=('arial', 10, 'bold'))
        self.entry_name.place(x=160, y=10, width=150, height=30)

        self.button_in = tk.Button(root, text="Clock In", command=self.clock_in,
                                   font=('arial', 10, 'bold'), bg="#14b3eb", fg='white')
        self.button_in.place(x=160, y=60, width=150, height=30)

        self.button_out = tk.Button(root, text="Clock Out", command=self.clock_out,
                                    font=('arial', 10, 'bold'), bg="#14b3eb", fg='white')
        self.button_out.place(x=160, y=100, width=150, height=30)

        self.textbox = tk.Text(root, height=11, width=45, font=('arial', 10, 'bold'), bg='black',
                               fg='green')
        self.textbox.place(x=0, y=160, width=400, height=250)

    def clock_in(self):
        name = self.entry_name.get()

        if not name:
            tk.messagebox.showerror("Error", "Please enter your name")
            return

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )

            # Create the 'attendance' table if it does not exist
            mycursor = mydb.cursor()
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS attendance (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                "clock_in DATETIME, clock_out DATETIME)")

            # Insert a new record with the current timestamp
            sql = "INSERT INTO attendance (name, clock_in) VALUES (%s, %s)"
            val = (name, datetime.now())
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{name} clocked in at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    def clock_out(self):
        name = self.entry_name.get()

        if not name:
            tk.messagebox.showerror("Error", "Please enter your name")
            return

        try:
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )

            # Create the 'attendance' table if it does not exist
            mycursor = mydb.cursor()

            # Update the latest record with the current timestamp
            sql = "UPDATE attendance SET clock_out = %s WHERE name = %s AND id = (SELECT MAX(id)%s)"
            val = (datetime.now(), name, name)
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error updating data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{name} clocked out at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


class AbsenceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Absence Manager")
        root.geometry("400x400+350+150")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_name = tk.Label(root, text="Enter your name:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_name.place(x=0, y=10, width=160, height=30)

        self.entry_name = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_name.place(x=190, y=10, width=150, height=30)

        self.label_start = tk.Label(root, text="Start Date (YYYY-MM-DD):", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_start.place(x=0, y=50, width=160, height=30)

        self.entry_start = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_start.place(x=190, y=50, width=150, height=30)

        self.label_end = tk.Label(root, text="End Date (YYYY-MM-DD):", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_end.place(x=0, y=90, width=160, height=30)

        self.entry_end = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_end.place(x=190, y=90, width=150, height=30)

        self.button_submit = tk.Button(root, text="Submit", command=self.submit,
                                       font=('arial', 10, 'bold'), bg="#14b3eb", fg='white')
        self.button_submit.place(x=190, y=140, width=150, height=30)

        self.textbox = tk.Text(root, height=10, width=45, font=('arial', 10, 'bold'), bg='black',
                               fg='green')
        self.textbox.place(x=0, y=200, width=400, height=250)

    def submit(self):
        name = self.entry_name.get()
        start_date = self.entry_start.get()
        end_date = self.entry_end.get()

        if not name:
            tk.messagebox.showerror("Error", "Please enter your name")
            return

        if not start_date:
            tk.messagebox.showerror("Error", "Please enter a start date")
            return

        if not end_date:
            tk.messagebox.showerror("Error", "Please enter an end date")
            return

        try:
            # Convert the date strings to datetime objects
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

            # Insert a new record for each day in the absence period
            delta = timedelta(days=1)
            while start_date_obj <= end_date_obj:
                # Connect to MySQL database
                mydb = mysql.connector.connect(
                    host='localhost', username='root', password='locoz0227',
                    database='employee_mng_system'
                )

                # Create the 'absence' table if it does not exist
                mycursor = mydb.cursor()
                mycursor.execute(
                    "CREATE TABLE IF NOT EXISTS absence (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), start_date DATE, end_date DATE)")

                sql = "INSERT INTO absence (name, start_date, end_date) VALUES (%s, %s, %s)"
                val = (name, start_date_obj.date(), start_date_obj.date())
                mycursor.execute(sql, val)
                start_date_obj += delta

                mydb.commit()
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format")
            return
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{name} will be absent from {start_date} to {end_date}\n")


class EmployeePortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Portal")
        root.geometry("400x400+450+180")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create and place the GUI widgets
        self.label_name = tk.Label(root, text="Name:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_name.place(x=0, y=10, width=130, height=30)

        self.entry_name = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_name.place(x=180, y=10, width=150, height=30)

        self.label_email = tk.Label(root, text="Email:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_email.place(x=0, y=50, width=130, height=30)

        self.entry_email = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_email.place(x=180, y=50, width=150, height=30)

        self.label_phone = tk.Label(root, text="Phone:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_phone.place(x=0, y=90, width=130, height=30)

        self.entry_phone = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_phone.place(x=180, y=90, width=150, height=30)

        self.label_address = tk.Label(root, text="Address:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_address.place(x=0, y=130, width=130, height=30)

        self.entry_address = tk.Entry(root, font=('arial', 10, 'bold'))
        self.entry_address.place(x=180, y=130, width=150, height=30)

        self.add_picture = tk.Button(root, text="Add Image", command=call_ImageView,
                                     font=('arial', 10, 'bold'), bg="#14b3eb", fg='white')
        self.add_picture.place(x=0, y=170, width=150, height=30)

        self.button_submit = tk.Button(root, text="Submit", command=self.submit,
                                       font=('arial', 10, 'bold'), bg="#14b3eb", fg='white')
        self.button_submit.place(x=180, y=170, width=150, height=30)

        self.textbox = tk.Text(root, height=10, width=40, font=('arial', 10, 'bold'), bg='black', fg='green')
        self.textbox.place(x=0, y=230, width=400, height=270)

    def submit(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()

        if not name:
            tk.messagebox.showerror("Error", "Please enter your name")
            return

        if not email:
            tk.messagebox.showerror("Error", "Please enter your email address")
            return

        if not phone:
            tk.messagebox.showerror("Error", "Please enter your phone number")
            return

        if not address:
            tk.messagebox.showerror("Error", "Please enter your address")
            return

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host='localhost', username='root', password='locoz0227',
                database='employee_mng_system'
            )
            # Create the 'employees' table if it does not exist
            mycursor = mydb.cursor()

            mycursor.execute('UPDATE employees set email=%s,phone_number=%s,address=%s WHERE name=%s', (
                self.entry_email.get(), self.entry_phone.get(), self.entry_address.get(), self.entry_name.get()))
            mydb.commit()
        except mysql.connector.Error as e:
            tk.messagebox.showerror("Error", f"Error inserting data: {str(e)}")
            return

        self.textbox.insert(tk.END, f"{name} has been added to the database\n")


class LeaveApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("LeaveApplication")
        root.geometry("400x400+250+130")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create the leave entry fields
        self.label_name = tk.Label(root, text="Name:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_name.place(x=0, y=10, width=160, height=30)

        self.entry_name = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_name.place(x=180, y=10, width=150, height=30)

        self.label_start_date = tk.Label(root, text="Start Date (YYYY-MM-DD):", font=('arial', 10, 'bold'),
                                         bg="#0e21f1")
        self.label_start_date.place(x=0, y=50, width=160, height=30)

        self.entry_start_date = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_start_date.place(x=180, y=50, width=150, height=30)

        self.label_end_date = tk.Label(root, text="End Date (YYYY-MM-DD):", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_end_date.place(x=0, y=90, width=160, height=30)

        self.entry_end_date = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_end_date.place(x=180, y=90, width=150, height=30)

        self.label_reason = tk.Label(root, text="Reason:", font=('arial', 10, 'bold'), bg="#0e21f1")
        self.label_reason.place(x=0, y=130, width=160, height=30)

        self.entry_reason = tk.Entry(root, font=('arial', 10, 'bold'), width=35)
        self.entry_reason.place(x=180, y=130, width=150, height=30)

        # Create the leave application and view leave status buttons
        self.button_apply = tk.Button(root, text="Apply for Leave", font=('arial', 10, 'bold'),
                                      command=self.apply_leave, bg="#14b3eb")
        self.button_apply.place(x=180, y=170, width=150, height=30)

        self.button_view = tk.Button(root, text="View Leave Status", font=('arial', 10, 'bold'),
                                     command=self.view_leaves, bg="#14b3eb")
        self.button_view.place(x=180, y=210, width=150, height=30)

        # Create the leave listbox
        self.listbox_leave = tk.Listbox(root, height=10, width=35, font=('arial', 10, 'bold'),
                                        bg='black', fg='green')
        self.listbox_leave.place(x=0, y=260, width=400, height=140)

    # Function to apply for leave
    def apply_leave(self):
        # Get the leave details from the user
        name = self.entry_name.get()
        start_date = self.entry_start_date.get()
        end_date = self.entry_end_date.get()
        reason = self.entry_reason.get()
        status = "Pending"
        # Create a connection to MySQL database
        mydb = mysql.connector.connect(
            host='localhost', username='root', password='locoz0227',
            database='employee_mng_system'
        )

        # Create a cursor to interact with the database
        cursor = mydb.cursor()

        # Create the leaves table if it doesn't exist
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS leaves (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), start_date DATE, end_date DATE, reason VARCHAR(255), status VARCHAR(255))")

        # Insert the leave application into the database
        insert_query = "INSERT INTO leaves (name, start_date, end_date, reason, status) VALUES (%s, %s, %s, %s, %s)"
        values = (name, start_date, end_date, reason, status)
        cursor.execute(insert_query, values)
        mydb.commit()

        # Show a message box confirming the leave application
        messagebox.showinfo("Leave Application", "Leave application submitted successfully!")

        # Clear the leave entry fields
        self.entry_name.delete(0, END)
        self.entry_start_date.delete(0, END)
        self.entry_end_date.delete(0, END)
        self.entry_reason.delete(0, END)

    # Function to view leave status
    def view_leaves(self):
        # Clear the listbox
        self.listbox_leave.delete(0, END)

        # Select all leave applications from the database
        select_query = "SELECT * FROM leaves"
        cursor.execute(select_query)
        leaves = cursor.fetchall()

        # Add each leave application to the listbox
        for leave in leaves:
            self.listbox_leave.insert(END,
                                      f"{leave[1]} - Start Date: {leave[2]} - End Date: {leave[3]} - Reason: {leave[4]} - Status: {leave[5]}")


class ImageView:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("300x380")
        self.root.resizable(False, False)
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = tk.Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)
        # Create GUI elements
        self.id_label = tk.Label(root, text="ID NO:", bg="#0e21f1")
        self.id_label.place(x=0, y=10, width=130, height=30)

        self.id_entry = tk.Entry(root, font=('arial', 10, 'bold'))
        self.id_entry.place(x=160, y=10, width=150, height=30)

        self.display_button = tk.Button(root, text="Display", command=self.display_image, font=('arial', 10, 'bold'),
                                        bg="#14b3eb")
        self.display_button.place(x=160, y=60, width=150, height=30)

        self.save_button = tk.Button(root, text="Save", command=self.save_image, font=('arial', 10, 'bold'),
                                     bg="#14b3eb")
        self.save_button.place(x=0, y=60, width=130, height=30)

        self.image_label = tk.Label(root)
        self.image_label.place(x=0, y=130, width=300, height=250)

    # Define functions
    def display_image(self):
        # Retrieve image from database
        id_number = self.id_entry.get()
        if self.id_entry.get() == "":
            messagebox.showerror("Error", "Id number required")
            return
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="locoz0227",
            database="employee_mng_system"
        )

        cursor = mydb.cursor()
        cursor.execute("SELECT image FROM images WHERE id_number = %s", (id_number,))
        result = cursor.fetchone()
        if result is not None:
            # Convert image data to PIL Image object
            image_data = result[0]
            image = Image.open(io.BytesIO(image_data))
            # Resize image to fit label
            image = image.resize((300, 250), Image.LANCZOS)
            # Convert PIL Image object to Tkinter PhotoImage object
            photo_image = ImageTk.PhotoImage(image)
            # Display image in label
            self.image_label.config(image=photo_image)
            self.image_label.image = photo_image
        else:
            messagebox.showerror("Error", "Image not found")

    def save_image(self):
        # Open image file and read image data
        id_number = self.id_entry.get()
        if self.id_entry.get() == "":
            messagebox.showerror("Error", "Id number required")
            return
        filename = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.gif")])
        with open(filename, "rb") as f:
            image_data = f.read()
            # Convert image data to PIL Image object
            image = Image.open(io.BytesIO(image_data))
            # Resize image to fit label
            image = image.resize((250, 250), Image.LANCZOS)
            # Convert PIL Image object to Tkinter PhotoImage object
            photo_image = ImageTk.PhotoImage(image)
            # Display image in label
            self.image_label.config(image=photo_image)
            self.image_label.image = photo_image

        # Insert image data into database
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="locoz0227",
            database="employee_mng_system"
        )

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO images (image,id_number) VALUES (%s,%s)", (image_data, id_number))
        mydb.commit()
        messagebox.showinfo("Success", "Image saved")


class ResetPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Reset Password")
        root.geometry("400x400+250+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)

        # Create the username label and entry
        self.username_label = tk.Label(root, text="Username:", font=('ariel', 11, 'bold'), bg="#0e21f1")
        self.username_entry = tk.Entry(root)
        self.username_label.place(x=0, y=10, width=100, height=30)
        self.username_entry.place(x=120, y=10, width=150, height=30)

        # Create the nickname label and entry
        self.nickname_label = tk.Label(root, text="Nickname:", font=('ariel', 11, 'bold'), bg="#0e21f1")
        self.nickname_entry = tk.Entry(root, show="*")
        self.nickname_label.place(x=0, y=50, width=100, height=30)
        self.nickname_entry.place(x=120, y=50, width=150, height=30)

        # Create the reset password button
        self.reset_password_button = tk.Button(root, text="Reset Password", font=('ariel', 11, 'bold'),
                                               bg="#14b3eb", command=lambda: self.Reset())

        self.reset_password_button.place(x=120, y=100, width=150, height=30)

    def Reset(self):
        username = self.username_entry.get()
        if self.username_entry.get() == "" or self.nickname_entry.get() == "":
            messagebox.showinfo("Info", "All fields are required")
            return
        # Connect to the MySQL database
        conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                       database='employee_mng_system')
        cursor = conn.cursor()

        # Retrieve the hashed password from the database
        cursor.execute("SELECT nickname FROM user WHERE username=%s", (username,))
        result = cursor.fetchone()
        if result:
            nickname = result[0]

            # Check if the password matches the hashed password
            if nickname == self.nickname_entry.get():
                # Login succeeded
                self.username_entry.delete(0, END)
                self.nickname_entry.delete(0, END)
                call_CreateAccount()

            else:
                # Login failed
                messagebox.showerror('Invalid', "Invalid username or nickname")
                return
        else:
            # Login failed
            messagebox.showerror('Error', "Login failed!")
            return

        # Close the database connection
        cursor.close()
        conn.close()

    # Create the GUI window
    # the first gui owns the root window


class HrCreateAccount:
    def __init__(self, root):
        self.root = root
        self.root.title = "Create Account"
        root.geometry("400x400+250+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)
        # Create the username label and entry
        self.username_label = tk.Label(root, text="Username:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.username_entry = tk.Entry(root)
        self.username_label.place(x=0, y=10, width=120, height=30)
        self.username_entry.place(x=140, y=10, width=150, height=30)

        # Create the password label and entry
        self.password_label = tk.Label(root, text="New Password:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.password_entry = tk.Entry(root, show="*")
        self.password_label.place(x=0, y=50, width=120, height=30)
        self.password_entry.place(x=140, y=50, width=150, height=30)

        # Create the password label and entry
        self.new_password_label = tk.Label(root, text="New Password:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.new_password_entry = tk.Entry(root, show="*")
        self.new_password_label.place(x=0, y=90, width=120, height=30)
        self.new_password_entry.place(x=140, y=90, width=150, height=30)

        # Create the nickname label and entry
        self.nickname_label = tk.Label(root, text="Nickname:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.nickname_entry = tk.Entry(root)
        self.nickname_label.place(x=0, y=130, width=120, height=30)
        self.nickname_entry.place(x=140, y=130, width=150, height=30)

        # Create the reset password button
        self.create_account_button = tk.Button(root, text="Create Account", font=('ariel', 11, 'bold'),
                                               bg="#14b3eb", command=lambda: self.store_credentials(
                username=self.username_entry.get(),
                password=self.password_entry.get(), nickname=self.nickname_entry.get()))
        self.create_account_button.place(x=140, y=170, width=150, height=30)

    def hash_password(self, password):
        # Hash the password using bcrypt
        password = self.password_entry.get()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def check_password(self, password, hashed_password):
        # Check if the password matches the hashed password
        password = self.password_entry.get()
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    def store_credentials(self, username, password, nickname):
        if self.username_entry.get() == "" or self.password_entry.get() == "" or self.new_password_entry.get() == "":
            tk.messagebox.showerror("Error", "All field are required")
            return
        if self.password_entry.get() == self.new_password_entry.get():
            # Connect to the MySQL database
            conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                           database='employee_mng_system')
            cursor = conn.cursor(buffered=True)

            # Hash the password
            hashed_password = self.hash_password(password)

            # Insert the username and hashed password into the database
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS hr (username VARCHAR(255),password VARCHAR(255),nickname VARCHAR(255),timestamp DATETIME)")
            cursor.execute("INSERT INTO hr (username, password,nickname,timestamp) VALUES (%s, %s,%s,NOW())",
                           (username, hashed_password, nickname))
            conn.commit()
            messagebox.showinfo('Success', "Account Successfully Created")

            # Close the database connection
            cursor.close()
            conn.close()
        else:
            tk.messagebox.showerror("Error", "Entered password and the new password dont match")


class CreateAccount:
    def __init__(self, root):
        self.root = root
        self.root.title = "Create Account"
        root.geometry("400x400+250+250")
        image = Image.open('company_images/logo.jpeg')
        image = image.resize((400, 400), Image.LANCZOS)
        root.photo_logo = ImageTk.PhotoImage(image)

        root.print = Label(root, image=root.photo_logo)
        root.print.place(x=0, y=0, width=400, height=400)
        # Create the username label and entry
        self.username_label = tk.Label(root, text="Username:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.username_entry = tk.Entry(root)
        self.username_label.place(x=0, y=10, width=120, height=30)
        self.username_entry.place(x=140, y=10, width=150, height=30)

        # Create the password label and entry
        self.password_label = tk.Label(root, text="New Password:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.password_entry = tk.Entry(root, show="*")
        self.password_label.place(x=0, y=50, width=120, height=30)
        self.password_entry.place(x=140, y=50, width=150, height=30)

        # Create the password label and entry
        self.new_password_label = tk.Label(root, text="New Password:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.new_password_entry = tk.Entry(root, show="*")
        self.new_password_label.place(x=0, y=90, width=120, height=30)
        self.new_password_entry.place(x=140, y=90, width=150, height=30)

        # Create the nickname label and entry
        self.nickname_label = tk.Label(root, text="Nickname:", font=('ariel', 9, 'bold'), bg="#0e21f1")
        self.nickname_entry = tk.Entry(root)
        self.nickname_label.place(x=0, y=130, width=120, height=30)
        self.nickname_entry.place(x=140, y=130, width=150, height=30)

        # Create the reset password button
        self.create_account_button = tk.Button(root, text="Create Account", font=('ariel', 11, 'bold'),
                                               bg="#14b3eb", command=lambda: self.store_credentials(
                username=self.username_entry.get(),
                password=self.password_entry.get(), nickname=self.nickname_entry.get()))
        self.create_account_button.place(x=140, y=170, width=150, height=30)

    def hash_password(self, password):
        # Hash the password using bcrypt
        password = self.password_entry.get()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def check_password(self, password, hashed_password):
        # Check if the password matches the hashed password
        password = self.password_entry.get()
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    def store_credentials(self, username, password, nickname):
        if self.username_entry.get() == "" or self.password_entry.get() == "" or self.new_password_entry.get() == "":
            tk.messagebox.showerror("Error", "All field are required")
            return
        if self.password_entry.get() == self.new_password_entry.get():
            # Connect to the MySQL database
            conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                           database='employee_mng_system')
            cursor = conn.cursor(buffered=True)

            # Hash the password
            hashed_password = self.hash_password(password)

            # Insert the username and hashed password into the database
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS user (username VARCHAR(255),password VARCHAR(255),nickname VARCHAR(255),timestamp DATETIME)")
            cursor.execute("INSERT INTO user (username, password,nickname,timestamp) VALUES (%s, %s,%s,NOW())",
                           (username, hashed_password, nickname))
            conn.commit()
            messagebox.showinfo('Success', "Account Successfully Created")

            # Close the database connection
            cursor.close()
            conn.close()
        else:
            tk.messagebox.showerror("Error", "Entered password and the new password dont match")


class ClassAdmin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        # Variables
        self.var_department = StringVar()
        self.var_designation = StringVar()
        self.var_address = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_marital_status = StringVar()
        self.var_date_of_joining = StringVar()
        self.var_gender = StringVar()
        self.var_phone_number = StringVar()
        self.var_id_number = StringVar()
        self.var_salary = StringVar()

        label_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'),
                            fg='darkblue', bg='white')
        label_title.place(x=0, y=0, width=1530, height=50)
        # logo
        image_logo = Image.open('company_images/logo.jpeg')
        image_logo = image_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(image_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)
        # Image frame
        image_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        image_frame.place(x=0, y=50, width=1340, height=150)
        # 1st
        image = Image.open('company_images/employee_rep.jpeg')
        image = image.resize((1490, 150), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.image = Label(self.root, image=self.photo)
        self.image.place(x=0, y=50, width=1510, height=160)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=8, y=220, width=1340, height=500)

        # Upper Frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                                 font=('times new roman', 12, 'bold'), fg='red')
        upper_frame.place(x=8, y=8, width=1320, height=210)

        # Labels and Entry Fields
        label_department = Label(upper_frame, text='Department:', font=('ariel', 11, 'bold'),
                                 bg='white')
        label_department.grid(row=0, column=0, padx=2, sticky=W)

        combo_department = ttk.Combobox(upper_frame, textvariable=self.var_department,
                                        font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_department['value'] = ('Select Department', 'HR', 'Software Engineer', 'Manager')
        combo_department.current(0)
        combo_department.grid(row=0, column=1, padx=25, pady=7, sticky=W)

        # Label Designation
        label_designation = Label(upper_frame, text='Designation:', font=('ariel', 11, 'bold'),
                                  bg='white')
        label_designation.grid(row=1, column=0, padx=2, pady=7, sticky=W)
        text_designation = ttk.Entry(upper_frame, textvariable=self.var_designation, width=25,
                                     font=("arial", 11, 'bold'))
        text_designation.grid(row=1, column=1, pady=7, padx=25, sticky=W)

        # Address
        label_address = Label(upper_frame, text='Address:', font=('ariel', 11, 'bold'),
                              bg='white')
        label_address.grid(row=2, column=0, padx=2, pady=7, sticky=W)
        text_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=25,
                                 font=("arial", 11, 'bold'))
        text_address.grid(row=2, column=1, pady=7, padx=25, sticky=W)

        # Date of birth
        label_date_of_birth = Label(upper_frame, text='DateOfBirth:', font=('ariel', 11, 'bold'),
                                    bg='white')
        label_date_of_birth.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        text_date_of_birth = ttk.Entry(upper_frame, textvariable=self.var_date_of_birth, width=25,
                                       font=("arial", 11, 'bold'))
        text_date_of_birth.grid(row=3, column=1, pady=7, padx=25, sticky=W)

        # Name
        label_name = Label(upper_frame, text='Name:', font=('ariel', 11, 'bold'),
                           bg='white')
        label_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        text_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=30, font=("arial", 11, 'bold'))
        text_name.grid(row=0, column=3, pady=7, padx=25)

        # Email
        label_email = Label(upper_frame, text='Email:', font=('ariel', 11, 'bold'),
                            bg='white')
        label_email.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        text_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=30,
                               font=("arial", 11, 'bold'))
        text_email.grid(row=1, column=3, pady=7, padx=25)
        # Marital status
        label_marital_status = Label(upper_frame, text='Marital Status:', font=('ariel', 11, 'bold'),
                                     bg='white')
        label_marital_status.grid(row=2, column=2, padx=2, sticky=W)

        combo_marital_status = ttk.Combobox(upper_frame, textvariable=self.var_marital_status,
                                            font=('arial', 12, 'bold'), width=25, state='readonly')
        combo_marital_status['value'] = ('Married', 'Unmarried')
        combo_marital_status.current(0)
        combo_marital_status.grid(row=2, column=3, padx=25, pady=7, sticky=W)

        # Date Of Joining
        label_date_of_joining = Label(upper_frame, text='DateOfJoining:', font=('ariel', 11, 'bold'),
                                      bg='white')
        label_date_of_joining.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        text_date_of_joining = ttk.Entry(upper_frame, textvariable=self.var_date_of_joining, width=30,
                                         font=("arial", 11, 'bold'))
        text_date_of_joining.grid(row=3, column=3, pady=7, padx=25)

        # Gender
        label_gender = Label(upper_frame, text='Gender:', font=('ariel', 11, 'bold'),
                             bg='white')
        label_gender.grid(row=0, column=4, padx=2, sticky=W)

        combo_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 12, 'bold'),
                                    width=20,
                                    state='readonly')
        combo_gender['value'] = ('Male', 'Female')
        combo_gender.current(0)
        combo_gender.grid(row=0, column=5, padx=25, pady=7, sticky=W)

        # phone number
        label_phone_number = Label(upper_frame, text='Phone No:', font=('ariel', 11, 'bold'),
                                   bg='white')
        label_phone_number.grid(row=1, column=4, padx=2, pady=7, sticky=W)
        text_phone_number = ttk.Entry(upper_frame, textvariable=self.var_phone_number, width=25,
                                      font=("arial", 11, 'bold'))
        text_phone_number.grid(row=1, column=5, pady=7, padx=25)

        # Identification Number
        label_id_number = Label(upper_frame, text='Id No:', font=('ariel', 11, 'bold'),
                                bg='white')
        label_id_number.grid(row=2, column=4, padx=2, pady=7, sticky=W)
        text_id_number = ttk.Entry(upper_frame, textvariable=self.var_id_number, width=25,
                                   font=("arial", 11, 'bold'))
        text_id_number.grid(row=2, column=5, pady=7, padx=25)

        # Salary
        label_salary = Label(upper_frame, text='Salary:', font=('ariel', 11, 'bold'),
                             bg='white')
        label_salary.grid(row=3, column=4, padx=2, pady=7, sticky=W)
        text_salary = ttk.Entry(upper_frame, textvariable=self.var_salary, width=25,
                                font=("arial", 11, 'bold'))
        text_salary.grid(row=3, column=5, pady=7, padx=25)

        # Add Human resource Button

        button_add_human_resource = Button(upper_frame, text='AddHumanResource', command=call_HrCreateAccount,
                                           font=('arial', 11, 'bold'), width=18, bg='blue')
        button_add_human_resource.grid(row=4, column=3, padx=2)

        # Add user Button

        button_add_user = Button(upper_frame, text='Add User', command=call_CreateAccount,
                                 font=('arial', 11, 'bold'), width=18, bg='blue')
        button_add_user.grid(row=4, column=5, padx=2)

        # Button Frames
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1180, y=1, width=120, height=180)
        # Save Button
        button_save = Button(button_frame, text='Save', command=self.add_data, font=('arial', 15, 'bold'),
                             width=9,
                             bg='blue', fg='white')
        button_save.grid(row=0, column=0, padx=2, pady=1)
        # Update Button
        button_update = Button(button_frame, text='Update', command=self.update_data,
                               font=('arial', 15, 'bold'),
                               width=9, bg='blue', fg='white')
        button_update.grid(row=1, column=0, padx=2, pady=1)
        # Delete Button
        button_delete = Button(button_frame, text='Delete', command=self.delete_data,
                               font=('arial', 15, 'bold'),
                               width=9, bg='blue', fg='white')
        button_delete.grid(row=2, column=0, padx=2, pady=1)
        # Clear Button
        button_clear = Button(button_frame, text='Clear', command=self.reset_data,
                              font=('arial', 15, 'bold'), width=9,
                              bg='blue', fg='white')
        button_clear.grid(row=3, column=0, padx=2, pady=1)

        # Down Frame
        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white',
                                text='Employee Information Table',
                                font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=8, y=220, width=1320, height=270)
        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                  text='Search Employee Information',
                                  font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1317, height=60)
        # Search
        search_by = Label(search_frame, font=('arial', 11, 'bold'), text='Search By:', fg='white',
                          bg='red')
        search_by.grid(row=0, column=0, sticky=W, padx=5, pady=3)

        # Search
        self.var_combo_search = StringVar()
        combo_search_by_option = ttk.Combobox(search_frame, textvariable=self.var_combo_search,
                                              font=('arial', 12, 'bold'), width=21, state='readonly')
        combo_search_by_option['value'] = ('Select Option', 'phone_number', 'id_number')
        combo_search_by_option.current(0)
        combo_search_by_option.grid(row=0, column=1, padx=15, pady=1, sticky=W)

        self.var_search = StringVar()
        text_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22,
                                font=('arial', 11, 'bold'))
        text_search.grid(row=0, column=2, padx=20)

        button_search = Button(search_frame, text='Search', command=self.search_data,
                               font=('arial', 11, 'bold'),
                               width=14, bg='blue')
        button_search.grid(row=0, column=3, padx=2)

        button_show_all = Button(search_frame, text='Show All', command=self.fetch_data,
                                 font=('arial', 11, 'bold'),
                                 width=14, bg='blue')
        button_show_all.grid(row=0, column=4, padx=5)

        #   Employee Table
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1320, height=180)
        #  Scroll Bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(table_frame,
                                           columns=('department', 'designation', 'address', 'date_of_birth',
                                                    'name', 'email', 'marital_status', 'date_of_joining', 'gender'
                                                    , 'phone_number', 'id_number', 'salary',
                                                    )
                                           , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('department', text='Department')
        self.employee_table.heading('designation', text='Designation')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('date_of_birth', text='Date_Of_Birth')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('marital_status', text='Marital_Status')
        self.employee_table.heading('date_of_joining', text='Date_Of_Joining')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone_number', text='Phone_Number')
        self.employee_table.heading('id_number', text='Id_No')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('department', width=150)
        self.employee_table.column('designation', width=150)
        self.employee_table.column('address', width=150)
        self.employee_table.column('date_of_birth', width=150)
        self.employee_table.column('name', width=200)
        self.employee_table.column('email', width=200)
        self.employee_table.column('marital_status', width=150)
        self.employee_table.column('date_of_joining', width=150)
        self.employee_table.column('gender', width=150)
        self.employee_table.column('phone_number', width=150)
        self.employee_table.column('id_number', width=150)
        self.employee_table.column('salary', width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Declaration

    def add_data(self):
        if self.var_department.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                               database='employee_mng_system')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_department.get(),
                    self.var_designation.get(),
                    self.var_address.get(),
                    self.var_date_of_birth.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_marital_status.get(),
                    self.var_date_of_joining.get(),
                    self.var_gender.get(),
                    self.var_phone_number.get(),
                    self.var_id_number.get(),
                    self.var_salary.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added', parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror('Error'f'Due To:{str(es)}', parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                       database='employee_mng_system')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employees ')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_department.set(data[0])
        self.var_designation.set(data[1])
        self.var_address.set(data[2])
        self.var_date_of_birth.set(data[3])
        self.var_name.set(data[4])
        self.var_email.set(data[5])
        self.var_marital_status.set(data[6])
        self.var_date_of_joining.set(data[7])
        self.var_gender.set(data[8])
        self.var_phone_number.set(data[9])
        self.var_id_number.set(data[10])
        self.var_salary.set(data[11])

    def update_data(self):
        if self.var_department.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are You Sure You Want To Update This Employee Data ?')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                                   database='employee_mng_system')
                    my_cursor = conn.cursor()
                    my_cursor.execute('UPDATE employees set Department=%s,Designation=%s,Address=%s,'
                                      'Date_Of_Birth=%s,Name=%s,Email=%s,Marital_Status=%s,Date_Of_Joining=%s,'
                                      'Gender=%s,Phone_Number=%s,Salary=%s WHERE Id_Number=%s', (

                                          self.var_department.get(),
                                          self.var_designation.get(),
                                          self.var_address.get(),
                                          self.var_date_of_birth.get(),
                                          self.var_name.get(),
                                          self.var_email.get(),
                                          self.var_marital_status.get(),
                                          self.var_date_of_joining.get(),
                                          self.var_gender.get(),
                                          self.var_phone_number.get(),
                                          self.var_salary.get(),
                                          self.var_id_number.get()
                                      ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('success', 'Employee Successfully Updated', parent=self.root)

                else:
                    if not update:
                        return

            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_id_number.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                Delete = messagebox.askyesno('DELETE', 'ARE YOU SURE YOU WANT TO DELETE THIS EMPLOYEE DATA?',
                                             parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                                   database='employee_mng_system')
                    my_cursor = conn.cursor()
                    sql = 'DELETE from employees WHERE Id_Number=%s'
                    value = (self.var_id_number.get(),)
                    my_cursor.execute(sql, value)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Delete', 'Employee Successfully Deleted', parent=self.root)
                else:
                    if not Delete:
                        return
            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    # Reset
    def reset_data(self):
        self.var_department.set('Select Department')
        self.var_designation.set('')
        self.var_address.set('')
        self.var_date_of_birth.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_marital_status.set('Marital_status')
        self.var_date_of_joining.set('')
        self.var_gender.set('Gender')
        self.var_phone_number.set('')
        self.var_id_number.set('')
        self.var_salary.set('')

    # Search
    def search_data(self):
        if self.var_combo_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                               database='employee_mng_system')
                my_cursor = conn.cursor()
                # The LIKE operator is used with the WHERE statement to search for a specific pattern in the table.
                # Suppose you want to search for values which start with “a” in the table, the LIKE statement is used
                # in such scenarios.
                my_cursor.execute(
                    'select * from employees where ' + str(self.var_combo_search.get()) + " LIKE'%" + str(
                        self.var_search.get() + "%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Error", "There Is No Such Employee")

                conn.commit()
                conn.close()

            except EXCEPTION as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)


def call_Employee():
    win11 = Toplevel(root)
    c_employee = Employee
    c_employee(win11)
    return


def call_User():
    win12 = Toplevel(root)
    c_user = User
    c_user(win12)
    return


def call_ResetPassword():
    win13 = Toplevel(root)
    c_ResetPassword = ResetPassword
    c_ResetPassword(win13)


def call_ClassAdmin():
    win14 = Toplevel(root)
    c_ClassAdmin = ClassAdmin
    c_ClassAdmin(win14)


def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def check_password(password, hashed_password):
    # Check if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username_entry.get() == "" or password_entry.get() == "":
        return
    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                   database='employee_mng_system')
    cursor = conn.cursor(buffered=True)

    # Retrieve the hashed password from the database
    cursor.execute("SELECT password FROM user WHERE username=%s", (username,))
    result = cursor.fetchone()
    if result:
        hashed_password = result[0]
        # Check if the password matches the hashed password
        if check_password(password, hashed_password):
            # Login succeeded
            call_User()
            username_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            # Login failed
            messagebox.showerror('Invalid', "Invalid Username Or Password")
    else:
        # Login failed
        messagebox.showerror('Error', "Login failed!")
    # Close the database connection
    cursor.close()
    conn.close()


def Hr_login():
    username = username_entry.get()
    password = password_entry.get()
    if username_entry.get() == "" or password_entry.get() == "":
        return
    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                   database='employee_mng_system')
    cursor = conn.cursor(buffered=True)

    # Retrieve the hashed password from the database
    cursor.execute("SELECT password FROM hr WHERE username=%s", (username,))
    result = cursor.fetchone()
    if result:
        hashed_password = result[0]
        # Check if the password matches the hashed password
        if check_password(password, hashed_password):
            # Login succeeded
            call_Employee()
            username_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            # Login failed
            messagebox.showerror('Invalid', "Invalid Username Or Password")
    else:
        # Login failed
        messagebox.showerror('Error', "Login failed!")
    # Close the database connection
    cursor.close()
    conn.close()


def Admin_login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                   database='employee_mng_system')
    cursor = conn.cursor(buffered=True)

    # Retrieve the hashed password from the database
    cursor.execute("SELECT password FROM admin WHERE username=%s", (username,))
    result = cursor.fetchone()
    if result:
        hashed_password = result[0]

        # Check if the password matches the hashed password
        if check_password(password, hashed_password):
            call_ClassAdmin()
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            # Login succeeded

        else:
            # Login failed
            messagebox.showerror('Invalid', "Invalid Username Or Password")
    else:
        # Login failed
        messagebox.showerror('Error', "Login failed!")

    # Close the database connection
    cursor.close()
    conn.close()


def Admin_store_credentials(username, password):
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo("Info", "Kindly enter all field")
        return
    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost', username='root', password='locoz0227',
                                   database='employee_mng_system')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255),password VARCHAR(255))")
    cursor.execute("SELECT * from admin")
    data = cursor.fetchall()
    if len(data) < 1:
        # Hash the password
        hashed_password = hash_password(password)
        # Insert the username and hashed password into the database
        cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo('Success', "Account Successfully Created")

        # Close the database connection
        cursor.close()
        conn.close()

    else:
        messagebox.showerror('Error', "Admin account already exists")


# Create the GUI window
# the first gui owns the root window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400+500+250")
    root.title("Login")
    image_print = Image.open('company_images/logo.jpeg')
    image_print = image_print.resize((400, 400), Image.LANCZOS)
    root.photo_logo = ImageTk.PhotoImage(image_print)

    root.print = Label(root, image=root.photo_logo)
    root.print.place(x=0, y=0, width=400, height=400)

# Create the username label and entry
username_label = tk.Label(root, text="Username:", font=('ariel', 11, 'bold'), bg='darkblue', fg='white')
username_entry = tk.Entry(root)
username_label.place(x=0, y=10, width=100, height=30)
username_entry.place(x=120, y=10, width=160, height=30)

# Create the password label and entry
password_label = tk.Label(root, text="Password:", font=('ariel', 11, 'bold'), bg='darkblue', fg='white')
password_entry = tk.Entry(root, show="*")
password_label.place(x=0, y=50, width=100, height=30)
password_entry.place(x=120, y=50, width=160, height=30)

# Create the login button
login_button = tk.Button(root, text="Employee Login", font=('ariel', 11, 'bold'), bg='blue',
                         command=lambda: login())
login_button.place(x=120, y=110, width=160, height=30)

# Creating the human_resource_button
human_resource_button = tk.Button(root, text="Human Resource", font=('ariel', 11, 'bold'), bg='blue',
                                  command=lambda: Hr_login())
human_resource_button.place(x=120, y=160, width=160, height=30)

# Creating the admin login  button
admin_button = tk.Button(root, text="Admin Login", font=('ariel', 11, 'bold'), bg='blue',
                         command=lambda: Admin_login())
admin_button.place(x=120, y=210, width=160, height=30)

# Creating the admin create account  button
admin_create_account_button = tk.Button(root, text="AdminCreateAccount", font=('ariel', 11, 'bold'),
                                        bg='blue',
                                        command=lambda: Admin_store_credentials(username_entry.get(),
                                                                                password_entry.get()))
admin_create_account_button.place(x=120, y=260, width=160, height=30)

# Creating the Forgot_password_button
Forgot_password_button = tk.Button(root, text="ForgotPassword", font=('ariel', 11, 'bold'), bg='blue',
                                   command=call_ResetPassword)
Forgot_password_button.place(x=120, y=310, width=160, height=30)

root.mainloop()
