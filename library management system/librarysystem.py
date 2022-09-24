from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

mycursor = conn.cursor(dictionary=True)

newWindows=[]


def closewindows():

    for i in newWindows:
        i.destroy()


def login():



    if username.get()=="" or password.get()=="":
        messagebox.showinfo("Invalid", "Please enter valid Username or Password")
        return
    else:

        mycursor.execute(f"select * from student where userid='{username.get()}' and password='{password.get()}'")
        result = mycursor.fetchall()

        if len(result) > 0:
            messagebox.showinfo("Congrats!", "Login succesfully")
            screen.destroy()
            newscreen = Tk()
            newscreen.title("Library")
            newscreen.geometry("1280x720+150+30")

            photo = PhotoImage(file="library2.png")
            label1 = Label(newscreen, image=photo, height=800, width=1400)
            label1.place(y=50)



            def AddBook():


                def getinfo():
                    query=f"insert into books(BookTitle, ISBN, AuthorName, PublisherName) values('{nameentry.get()}', {int(Numberentry.get())}, '{AuNameentry.get()}', '{Publisherentry.get()}')"
                    mycursor.execute(query)
                    conn.commit()

                    messagebox.showinfo("Congrats!", "Book added successfully")



                frame6 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame6.pack(side=TOP, fill="y")
                name = Label(frame6, text="Book Title",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                Number = Label(frame6, text="ISBN Number",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=1)
                AuName = Label(frame6, text="Author Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=2)
                PubName = Label(frame6, text="Publisher Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=3)



                nameentry = Entry(frame6, font=10)

                Numberentry = Entry(frame6, font=10)
                AuNameentry = Entry(frame6, font=10)
                Publisherentry = Entry(frame6, font=10)
                nameentry.grid(row=0, column=1)

                Numberentry.grid(row=1, column=1)
                AuNameentry.grid(row=2, column=1)
                Publisherentry.grid(row=3, column=1)

                b5 = Button(frame6, text="Submit",bg="#00bd56", fg='white', command=getinfo, font=10)
                b5.grid()


                closewindows()
                newWindows.append(frame6)

            def AddUser():

                def userinfo():
                    query = f"insert into students(SID, Name, Age, Mobile) values({int(sidentry.get())}, '{nameentry.get()}', '{ageentry.get()}', '{mobileentry.get()}')"
                    mycursor.execute(query)
                    conn.commit()

                    messagebox.showinfo("Congrats!", "User added successfully")

                frame8 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame8.pack(side=TOP, fill="y")
                name = Label(frame8, text="Student ID",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                Number = Label(frame8, text="Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=1)
                AuName = Label(frame8, text="Age",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=2)
                PubName = Label(frame8, text="Mobile",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=3)

                sidentry = Entry(frame8, font=10)

                nameentry = Entry(frame8, font=10)
                ageentry = Entry(frame8, font=10)
                mobileentry = Entry(frame8, font=10)
                sidentry.grid(row=0, column=1)

                nameentry.grid(row=1, column=1)
                ageentry.grid(row=2, column=1)
                mobileentry.grid(row=3, column=1)

                b7 = Button(frame8, text="Submit",bg="#00bd56", fg='white', command=userinfo, font=10)
                b7.grid()

                closewindows()
                newWindows.append(frame8)

            def displayuser():

                def query_data():
                    # Create a database or connect to one that exists

                    # Create a cursor instance

                    mycursor.execute("SELECT * FROM students")
                    records = mycursor.fetchall()

                    # Add our data to the screen
                    global count
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            user_tree.insert(parent='', index='end', iid=count, text='',
                                           values=(
                                               record["SID"], record["Name"], record["Age"], record["Mobile"]),
                                           tags=('evenrow',))
                        else:
                            user_tree.insert(parent='', index='end', iid=count, text='',
                                           values=(
                                               record["SID"], record["Name"], record["Age"], record["Mobile"]),
                                           tags=('oddrow',))
                        # increment counter
                        count += 1

                style = ttk.Style()

                # Pick A Theme
                style.theme_use('default')

                # Configure the Treeview Colors
                style.configure("Treeview",
                                background="#D3D3D3",
                                foreground="black",
                                rowheight=25,
                                fieldbackground="#D3D3D3")

                # Change Selected Color
                style.map('Treeview',
                          background=[('selected', "#347083")])

                # Create a Treeview Frame
                tree_frame1 = Frame(newscreen, bg='#d7dae2',borderwidth=6, relief=SUNKEN, padx=80, pady=40, width=1080)
                tree_frame1.pack(side=TOP, fill="y")

                # Create a Treeview Scrollbar
                tree_scroll1 = Scrollbar(tree_frame1)
                tree_scroll1.pack(side=RIGHT, fill=Y)

                # Create The Treeview
                user_tree = ttk.Treeview(tree_frame1, yscrollcommand=tree_scroll1.set, selectmode="extended", height=33)
                user_tree.pack()

                # Configure the Scrollbar
                tree_scroll1.config(command=user_tree.yview)

                # Define Our Columns
                user_tree['columns'] = ("SID", "Name", "Age", "Mobile")

                # Format Our Columns
                user_tree.column("#0", width=0, stretch=NO)
                user_tree.column("SID", anchor=W, width=200)
                user_tree.column("Name", anchor=W, width=100)
                user_tree.column("Age", anchor=CENTER, width=180)
                user_tree.column("Mobile", anchor=CENTER, width=180)

                # Create Headings
                user_tree.heading("#0", text="", anchor=W)
                user_tree.heading("SID", text="SID", anchor=W)
                user_tree.heading("Name", text="Name", anchor=W)
                user_tree.heading("Age", text="Age", anchor=CENTER)
                user_tree.heading("Mobile", text="Mobile", anchor=CENTER)

                # Create Striped Row Tags
                user_tree.tag_configure('oddrow', background="white")
                user_tree.tag_configure('evenrow', background="lightblue")
                query_data()

                closewindows()
                newWindows.append(tree_frame1)
            def updtuser():

                query = f"update students set Name='{nameentry.get()}', Age='{ageentry.get()}', Mobile='{mobileentry.get()}' where SID={int(sidentry.get())}"
                mycursor.execute(query)
                conn.commit()

                messagebox.showinfo("Congrats!", "User update successfully")




            def userupdate():

                global nameentry
                global ageentry
                global mobileentry

                frame10 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame10.pack(side=TOP, fill="y")
                Number = Label(frame10, text="Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=1)
                AuName = Label(frame10, text="Age",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=2)
                PubName = Label(frame10, text="Mobile",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=3)


                nameentry = Entry(frame10, font=10)
                ageentry = Entry(frame10, font=10)
                mobileentry = Entry(frame10, font=10)


                nameentry.grid(row=1, column=1)
                ageentry.grid(row=2, column=1)
                mobileentry.grid(row=3, column=1)

                b10 = Button(frame10, text="Submit",bg="#00bd56", fg='white', command=updtuser, font=10)
                b10.grid()

                newWindows.append(frame10)

            def update():
                global sidentry

                frame9 = Frame(newscreen, bg='#d7dae2',borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame9.pack(side=LEFT, fill="y")
                name = Label(frame9, text="Enter Student ID",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                sidentry = Entry(frame9, font=10)
                sidentry.grid(row=0, column=1)
                b9 = Button(frame9, text="Submit",bg="#00bd56", fg='white', command=userupdate, font=10)
                b9.grid()

                closewindows()
                newWindows.append(frame9)

            def result():
                query = f"SELECT * FROM books where ISBN = {Numberentry.get()}"
                mycursor.execute(query)
                res = mycursor.fetchone()

                frame12 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame12.pack(side=TOP, fill="y")

                name = Label(frame12, text="Book Title",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                AuName = Label(frame12, text="Author Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=2)
                PubName = Label(frame12, text="Publisher Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=3)

                nameentry = Entry(frame12, font=10)
                AuNameentry = Entry(frame12, font=10)
                Publisherentry = Entry(frame12, font=10)
                nameentry.grid(row=0, column=1)

                AuNameentry.grid(row=2, column=1)
                Publisherentry.grid(row=3, column=1)

                nameentry.insert(0, res["BookTitle"])
                AuNameentry.insert(0, res["AuthorName"])
                Publisherentry.insert(0, res["PublisherName"])

                closewindows()
                newWindows.append(frame12)


            def FindBook():

                global Numberentry

                frame11 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame11.pack(side=LEFT, fill="y")
                Number = Label(frame11, text="Enter ISBN Number",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                Numberentry = Entry(frame11, font=10)
                Numberentry.grid(row=0, column=1)

                b11 = Button(frame11, text="Submit",bg="#00bd56", fg='white', command=result, font=10)
                b11.grid()

                closewindows()
                newWindows.append(frame11)

            def deletee():
                query = f"Delete from books where ISBN= {Numberentry.get()}"
                mycursor.execute(query)
                conn.commit()
                messagebox.showwarning("Warning", "Deleted")




            def delete():
                query = f"SELECT * FROM books where ISBN = {Numberentry.get()}"
                mycursor.execute(query)
                res = mycursor.fetchone()

                frame14 = Frame(newscreen, bg='#d7dae2', borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame14.pack(side=LEFT, fill="y")

                name = Label(frame14, text="Book Title",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                AuName = Label(frame14, text="Author Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=2)
                PubName = Label(frame14, text="Publisher Name",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=3)

                nameentry = Entry(frame14, font=10)
                AuNameentry = Entry(frame14, font=10)
                Publisherentry = Entry(frame14, font=10)
                nameentry.grid(row=0, column=1)

                AuNameentry.grid(row=2, column=1)
                Publisherentry.grid(row=3, column=1)

                nameentry.insert(0, res["BookTitle"])
                AuNameentry.insert(0, res["AuthorName"])
                Publisherentry.insert(0, res["PublisherName"])


                btn14 = Button(frame14, text='Delete', command=deletee, width=10, bg="#ed3833", fg='white', font=("arial", 15), bd=0)
                btn14.grid(row=6, column=0, pady=30)
                btn15 = Button(frame14, text='Cancel', width=10, bg="#00bd56", fg='white', font=("arial", 15), bd=0)
                btn15.grid(row=6, column=1, pady=30)

                newWindows.append(frame14)

            def deletebook():

                global Numberentry

                frame13 = Frame(newscreen, bg='#d7dae2',borderwidth=6, relief=SUNKEN, padx=80, pady=40)
                frame13.pack(side=LEFT, fill="y")
                Number = Label(frame13, text="Enter ISBN Number",bg='#d7dae2', font=10, padx=10, pady=15).grid(row=0)
                Numberentry = Entry(frame13, font=10)
                Numberentry.grid(row=0, column=1)

                b13 = Button(frame13, text="Submit",bg="#00bd56", fg='white', command=delete, font=10)
                b13.grid()


                newWindows.append(frame13)
            def displaybook():
            #    mycursor.execute("select * from books")
            #    display = mycursor.fetchall()
            #    for i in display:
            #        print(i)

                    #######################....type this code......############################
                def query_database():
                    # Create a database or connect to one that exists

                    # Create a cursor instance

                    mycursor.execute("SELECT * FROM books")
                    records = mycursor.fetchall()

                    # Add our data to the screen
                    global count
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            my_tree.insert(parent='', index='end', iid=count, text='',
                                           values=(
                                               record["BookTitle"], record["ISBN"], record["AuthorName"],
                                               record["PublisherName"]),
                                           tags=('evenrow',))
                        else:
                            my_tree.insert(parent='', index='end', iid=count, text='',
                                           values=(
                                               record["BookTitle"], record["ISBN"], record["AuthorName"],
                                               record["PublisherName"]),
                                           tags=('oddrow',))
                        # increment counter
                        count += 1

                style = ttk.Style()

                # Pick A Theme
                style.theme_use('default')

                # Configure the Treeview Colors
                style.configure("Treeview",
                                background="#D3D3D3",
                                foreground="black",
                                rowheight=25,
                                fieldbackground="#D3D3D3")

                # Change Selected Color
                style.map('Treeview',
                          background=[('selected', "#347083")])

                # Create a Treeview Frame
                tree_frame = Frame(newscreen, bg='#d7dae2',borderwidth=6, relief=SUNKEN, padx=40, pady=40, width=1080)
                tree_frame.pack(side=TOP, fill="y")

                # Create a Treeview Scrollbar
                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)

                # Create The Treeview
                my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=33)
                my_tree.pack()

                # Configure the Scrollbar
                tree_scroll.config(command=my_tree.yview)

                # Define Our Columns
                my_tree['columns'] = ("BookTitle", "ISBN", "AuthorName", "PublisherName")

                # Format Our Columns
                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("BookTitle", anchor=W, width=200)
                my_tree.column("ISBN", anchor=W, width=100)
                my_tree.column("AuthorName", anchor=CENTER, width=180)
                my_tree.column("PublisherName", anchor=CENTER, width=180)

                # Create Headings
                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("BookTitle", text="BookTitle", anchor=W)
                my_tree.heading("ISBN", text="ISBN", anchor=W)
                my_tree.heading("AuthorName", text="AuthorName", anchor=CENTER)
                my_tree.heading("PublisherName", text="PublisherName", anchor=CENTER)

                # Create Striped Row Tags
                my_tree.tag_configure('oddrow', background="white")
                my_tree.tag_configure('evenrow', background="lightblue")
                query_database()



                closewindows()
                newWindows.append(tree_frame)

                #   root = Toplevel(screen)
                #   root.title("project")
                #   root.geometry("1280x720+150+80")
                #   screen.configure(bg='#d7dae2')
                #   root.resizable(False, False)
                #   return

                #    mycursor.execute("insert into student values('"+ username.get() +"', '"+ password.get() +"')")
                #    mycursor.execute("commit")

                # username.delete(0, 'end')
                # password.delete(0, 'end')

                    #########.....END....#########################




            # frame2 = Frame(borderwidth=6, relief=SUNKEN)
            # frame2.pack(side=TOP, fill="x")

            frame2 = Frame(newscreen, borderwidth=2, bg='#d7dae2', relief=SUNKEN, bd=1)
            frame2.pack(fill="x")

            heading = Label(frame2, text="Welcome to Library System", bg='#d7dae2', fg="black",
                            font=("comicsansms", 25, "bold"), padx=15, pady=15)
            heading.pack(fill="x")

            frame3 = Frame(newscreen, borderwidth=2, bg='#d7dae2', relief=SUNKEN, bd=1)
            frame3.pack(fill="x")

            b1 = Button(frame3, bg="orange", fg='black', text="Add Book", font=("arial", 15), bd=1, relief=SUNKEN, command=AddBook).grid(column=0, row=0, padx=70, pady=20)
            b2 = Button(frame3, bg="#f44336", fg='white', text="Add User", font=("arial", 15), bd=1, relief=SUNKEN, command=AddUser).grid(column=0, padx=70, row=1, pady=20)
            b3 = Button(frame3, bg="orange", fg='black', text="Find Book", font=("arial", 15), bd=1, relief=SUNKEN, command=FindBook).grid(column=2, row=0, padx=50, pady=20)
            b4 = Button(frame3, bg="#f44336", fg='white', text="Clear Window", font=("arial", 15), bd=1, relief=SUNKEN,command=closewindows).grid(column=3, row=1, padx=150, pady=20)
            b5 = Button(frame3, bg="#f44336", fg='white', text="Delete Book", font=("arial", 15), bd=1, relief=SUNKEN, command=deletebook).grid(column=1, row=1, padx=150, pady=20)
            b6 = Button(frame3, bg="#f44336", fg='white', text="Update User", font=("arial", 15), bd=1, relief=SUNKEN, command=update).grid(column=2, row=1, padx=50, pady=20)
            b7 = Button(frame3, bg="orange", fg='black', text="Display User", font=("arial", 15), bd=1, relief=SUNKEN, command=displayuser).grid(column=1, row=0, padx=150, pady=20)
            b8 = Button(frame3, bg="orange", fg='black', text="Display Book", font=("arial", 15), bd=1, relief=SUNKEN, command=displaybook).grid(column=3, row=0, padx=150, pady=20)

            newscreen.mainloop()


def main_screen():
    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x720+150+30")
    screen.configure(bg='#d7dae2')
    screen.title('Library Management System')

    login1 = Label(text='Welcome to Library Centre', font=('arial', 30, 'bold'), fg='black', bg='#d7dae2').pack(side=TOP, pady=50)

    bordercolor = Frame(screen, bg='black', width=800, height=450, relief=SUNKEN)
    bordercolor.pack()

    frame1 = Frame(bordercolor, bg='#d7dae2', width=780, height=450, relief=SUNKEN)
    frame1.pack(padx=15, pady=15)

    txt1 = Label(frame1, text='Username', font=('arial', 15, 'bold'), bg='#d7dae2', fg='black').place(x=120, y=100)
    txt2 = Label(frame1, text='Password', font=('arial', 15, 'bold'), bg='#d7dae2', fg='black').place(x=120, y=160)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(frame1, textvariable=username, width=12, bd=2, font=("arial", 15))
    entry_username.place(x=250, y=100)

    entry_password = Entry(frame1, textvariable=password, width=12, bd=2, font=("arial", 15), show="*")
    entry_password.place(x=250, y=160)

    btn1 = Button(frame1, text='Login', command=login, width=10, bg="#ed3833", fg='white', font=("arial", 15), bd=0).place(x=250, y=220)

    txt3 = Label(frame1, text='Not registered yet? please register', font=('arial', 12), bg='#d7dae2', fg='black').place(x=170, y=300)

    btn2 = Button(frame1, text='Register', width=10, bg="#00bd56", fg='white', font=("arial", 15), bd=0).place(x=250, y=340)



    screen.mainloop()


main_screen()

