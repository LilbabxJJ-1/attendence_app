import datetime
from pytz import timezone
import customtkinter
from dbfuncs import DBFuncs as DB


class App(customtkinter.CTk):
    def __init__(self):
        super(App, self).__init__()
        self.title("JD Attendance")
        self.minsize(300, 200)
        self.current = 1
        self.dbnew = DB()
        self.textbox = customtkinter.CTkTextbox(master=self, width=570, height=380, fg_color="black", text_color="white")
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        self.textbox.insert("insert", "1st Period Class\n\n")
        self.textbox.configure(state="disabled", text_font=("Serif", 10))
        self.test = customtkinter.CTkProgressBar(master=self)
        self.firstpButton = customtkinter.CTkButton(master=self, text="1st Period", command=self.period1, fg_color="blue", state="disabled")
        self.secondpButton = customtkinter.CTkButton(master=self, text="2nd Period", command=self.period2, fg_color="blue", state="disabled")
        self.thirdpButton = customtkinter.CTkButton(master=self, text="3rd Period", command=self.period3, fg_color="blue", state="disabled")
        self.fourthpButton = customtkinter.CTkButton(master=self, text="4th Period", command=self.period4, fg_color="blue", state="disabled")
        self.fifthpButton = customtkinter.CTkButton(master=self, text="5th Period", command=self.period5, fg_color="purple", state="disabled")
        self.sixthpButton = customtkinter.CTkButton(master=self, text="6th Period", command=self.period6, fg_color="purple", state="disabled")
        self.seventhpButton = customtkinter.CTkButton(master=self, text="7th Period", command=self.period7, fg_color="purple", state="disabled")
        self.eigthpButton = customtkinter.CTkButton(master=self, text="8th Period", command=self.period8, fg_color="purple", state="disabled")
        self.addstudentButton = customtkinter.CTkButton(master=self, text="Add Student", command=self.add_student, fg_color="green", state="disabled")
        self.removestudentButton = customtkinter.CTkButton(master=self, text="Remove Student", command=self.remove_student, fg_color='red',
                                                           state="disabled")
        self.settingsButton = customtkinter.CTkButton(master=self, text="Settings", command=self.settings, fg_color="white", text_color="black",
                                                      state="disabled")
        self.loginButton = customtkinter.CTkButton(master=self, text="Login", command=self.login, fg_color="Blue", text_color="Black")
        self.loggeduser = customtkinter.CTkLabel(master=self, text='Welcome, User', text_color="White", fg_color=None)
        self.loggeduser.place(relx=0.01, rely=.0005)
        self.firstpButton.place(relx=0.03, rely=0.8)
        self.secondpButton.place(relx=0.27, rely=0.8)
        self.thirdpButton.place(relx=0.51, rely=0.8)
        self.fourthpButton.place(relx=0.75, rely=0.8)
        self.fifthpButton.place(relx=0.03, rely=.87)
        self.sixthpButton.place(relx=0.27, rely=.87)
        self.seventhpButton.place(relx=0.51, rely=.87)
        self.eigthpButton.place(relx=0.75, rely=.87)
        self.addstudentButton.place(relx=.75, rely=.033)
        self.removestudentButton.place(relx=.75, rely=.1)
        self.settingsButton.place(relx=.75, rely=.17)
        self.loginButton.place(relx=.75, rely=.24)
        self.resizable(0, 0)
        self.nostudents = None
        self.rewrite = None
        self.user = ""
        self.showing = ""
        self.update()
        self.label = None

    def login(self):
        def remove():
            teacher = self.dbnew.select("Teacher")
            tu = teacher_user.get()
            tp = teacher_pass.get()
            if self.label is not None:
                self.label.destroy()
            if tp == "" or tu == " ":
                label = customtkinter.CTkLabel(master=window, text="Please fill ALL the fields", text_color="red")
                label.place(relx=0.3, rely=.67)
            num = 0
            for i in teacher:
                if str(tu.title()) == str(i[1].title()):
                    num += 1
                    if i[2] == tp:
                        print("Logged in")
                        self.user = tu.title().split(" ")[1]
                        print(self.user)
                        self.loggeduser.configure(text=f"Welcome {tu.title()}")
                        self.firstpButton.configure(state="enabled")
                        self.secondpButton.configure(state="enabled")
                        self.thirdpButton.configure(state="enabled")
                        self.fourthpButton.configure(state="enabled")
                        self.fifthpButton.configure(state="enabled")
                        self.sixthpButton.configure(state="enabled")
                        self.seventhpButton.configure(state="enabled")
                        self.eigthpButton.configure(state="enabled")
                        self.settingsButton.configure(state="enabled")
                        self.addstudentButton.configure(state="enabled")
                        self.removestudentButton.configure(state="enabled")
                        self.loginButton.configure(state="disabled")
                        window.destroy()
                        break

                    else:
                        self.label = customtkinter.CTkLabel(master=window, text="Password is incorrect", text_color="red")
                        self.label.place(relx=0.3, rely=.67)
                        return

            else:
                if num == 0:
                    self.label = customtkinter.CTkLabel(master=window, text="User doesn't exist, please signup on the scanner app", text_color="red")
                    self.label.place(relx=0.1, rely=.67)
                    return

            # self.user =

        window = customtkinter.CTkToplevel(self)
        window.title('Login')
        window.geometry("400x200")
        teacher_user = customtkinter.CTkEntry(master=window, placeholder_text="Username...")
        teacher_pass = customtkinter.CTkEntry(master=window, placeholder_text="Password...")
        submit = customtkinter.CTkButton(master=window, text="Confirm Login", command=remove, fg_color="green")
        teacher_user.place(relx=0.3, rely=0.3)
        teacher_pass.place(relx=0.3, rely=0.5)
        submit.place(relx=0.3, rely=0.8)
        window.transient(master=self)

    def textboxcolor(self, choice):
        if choice == "White":
            self.textbox.configure(fg_color="White")
        elif choice == "Black":
            self.textbox.configure(fg_color="Black")
        elif choice == "Red":
            self.textbox.configure(fg_color="Red")
        elif choice == "Blue":
            self.textbox.configure(fg_color="Blue")
        elif choice == "Grey":
            self.textbox.configure(fg_color="Grey")
        elif choice == "Green":
            self.textbox.configure(fg_color="Green")
        else:
            self.textbox.configure(fg_color="Pink")

    def textcolor(self, choice):
        if choice == "White":
            self.textbox.configure(text_color="White")
        elif choice == "Black":
            self.textbox.configure(text_color="Black")
        elif choice == "Red":
            self.textbox.configure(text_color="Red")
        elif choice == "Blue":
            self.textbox.configure(text_color="Blue")
        elif choice == "Grey":
            self.textbox.configure(text_color="Grey")
        elif choice == "Green":
            self.textbox.configure(text_color="Green")
        else:
            self.textbox.configure(text_color="Pink")

    def row1colors(self, choice):
        if choice == "White":
            self.firstpButton.configure(fg_color="White")
            self.secondpButton.configure(fg_color="White")
            self.thirdpButton.configure(fg_color="White")
            self.fourthpButton.configure(fg_color="White")
        elif choice == "Black":
            self.firstpButton.configure(fg_color="Black")
            self.secondpButton.configure(fg_color="Black")
            self.thirdpButton.configure(fg_color="Black")
            self.fourthpButton.configure(fg_color="Black")
        elif choice == "Red":
            self.firstpButton.configure(fg_color="Red")
            self.thirdpButton.configure(fg_color="Red")
            self.secondpButton.configure(fg_color="Red")
            self.fourthpButton.configure(fg_color="Red")
        elif choice == "Blue":
            self.firstpButton.configure(fg_color="Blue")
            self.secondpButton.configure(fg_color="Blue")
            self.thirdpButton.configure(fg_color="Blue")
            self.fourthpButton.configure(fg_color="Blue")
        elif choice == "Grey":
            self.firstpButton.configure(fg_color="Grey")
            self.secondpButton.configure(fg_color="Grey")
            self.thirdpButton.configure(fg_color="Grey")
            self.fourthpButton.configure(fg_color="Grey")
        elif choice == "Green":
            self.firstpButton.configure(fg_color="Green")
            self.secondpButton.configure(fg_color="Green")
            self.thirdpButton.configure(fg_color="Green")
            self.fourthpButton.configure(fg_color="Green")
        else:
            self.firstpButton.configure(fg_color="Pink")
            self.secondpButton.configure(fg_color="Pink")
            self.thirdpButton.configure(fg_color="Pink")
            self.fourthpButton.configure(fg_color="Pink")

    def row2color(self, choice):
        if choice == "White":
            self.fifthpButton.configure(fg_color="White")
            self.sixthpButton.configure(fg_color="White")
            self.seventhpButton.configure(fg_color="White")
            self.eigthpButton.configure(fg_color="White")
        elif choice == "Black":
            self.fifthpButton.configure(fg_color="Black")
            self.sixthpButton.configure(fg_color="Black")
            self.seventhpButton.configure(fg_color="Black")
            self.eigthpButton.configure(fg_color="Black")
        elif choice == "Red":
            self.fifthpButton.configure(fg_color="Red")
            self.sixthpButton.configure(fg_color="Red")
            self.seventhpButton.configure(fg_color="Red")
            self.eigthpButton.configure(fg_color="Red")
        elif choice == "Blue":
            self.fifthpButton.configure(fg_color="Blue")
            self.sixthpButton.configure(fg_color="Blue")
            self.seventhpButton.configure(fg_color="Blue")
            self.eigthpButton.configure(fg_color="Blue")
        elif choice == "Grey":
            self.fifthpButton.configure(fg_color="Grey")
            self.sixthpButton.configure(fg_color="Grey")
            self.seventhpButton.configure(fg_color="Grey")
            self.eigthpButton.configure(fg_color="Grey")
        elif choice == "Green":
            self.fifthpButton.configure(fg_color="Green")
            self.sixthpButton.configure(fg_color="Green")
            self.seventhpButton.configure(fg_color="Green")
            self.eigthpButton.configure(fg_color="Green")
        else:
            self.fifthpButton.configure(fg_color="Pink")
            self.sixthpButton.configure(fg_color="Pink")
            self.seventhpButton.configure(fg_color="Pink")
            self.eigthpButton.configure(fg_color="Pink")

    def show(self, choice):
        if choice == "IDs":
            self.showing = "IDs"
        else:
            self.showing = "Names"

    def settings(self):
        window = customtkinter.CTkToplevel(self)
        window.title('Settings Student')
        window.geometry("400x400")
        window.transient(master=self)
        label = customtkinter.CTkLabel(master=window, text="BG-Color")
        label2 = customtkinter.CTkLabel(master=window, text="Text-Color")
        label3 = customtkinter.CTkLabel(master=window, text="Row1-Color")
        label4 = customtkinter.CTkLabel(master=window, text="Row2-Color")
        label5 = customtkinter.CTkLabel(master=window, text="Sort By")
        label.place(relx=0.1, rely=0.06)
        label2.place(relx=.1, rely=0.2)
        label3.place(relx=0.1, rely=0.34)
        label4.place(relx=0.1, rely=0.48)
        label5.place(relx=0.1, rely=0.62)
        combobox = customtkinter.CTkOptionMenu(master=window, values=["Black", "White", "Red", "Blue", "Grey", "Green", "Pink"],
                                               command=self.textboxcolor)
        combobox2 = customtkinter.CTkOptionMenu(master=window, values=["Black", "White", "Red", "Blue", "Grey", "Green", "Pink"],
                                                command=self.textcolor)
        combobox3 = customtkinter.CTkOptionMenu(master=window, values=["Black", "White", "Red", "Blue", "Grey", "Green", "Pink"],
                                                command=self.row1colors)
        combobox4 = customtkinter.CTkOptionMenu(master=window, values=["Black", "White", "Red", "Blue", "Grey", "Green", "Pink"],
                                                command=self.row2color)
        combobox5 = customtkinter.CTkOptionMenu(master=window, values=["IDs", "Names"],
                                                command=self.show)
        combobox.place(relx=0.38, rely=0.06)
        combobox2.place(relx=0.38, rely=0.2)
        combobox3.place(relx=0.38, rely=0.34)
        combobox4.place(relx=0.38, rely=0.48)
        combobox5.place(relx=0.38, rely=0.62)

    def remove_student(self):
        def remove():
            ids = student_id.get()
            pd = period.get()
            students = self.dbnew.select("Student")
            for student in students:
                if student[10] == int(ids):
                    try:
                        if student[int(pd) + 1].split(", ")[0] == self.user:
                            self.dbnew.overwrite("Student", f"Period{pd}", "Student Name", student[1], "")
                        else:
                            print(f"that student isn't in your {pd} period")
                    except AttributeError:
                        print(f"that student isn't in your {pd} period")
            window.destroy()

        window = customtkinter.CTkToplevel(self)
        window.title('Remove Student')
        window.geometry("400x200")
        period = customtkinter.CTkEntry(master=window, placeholder_text="Class period...")
        student_id = customtkinter.CTkEntry(master=window, placeholder_text="Student ID...")
        submit = customtkinter.CTkButton(master=window, text="Confirm Information", command=remove, fg_color="green")
        student_id.place(relx=0.3, rely=0.3)
        period.place(relx=0.3, rely=0.5)
        submit.place(relx=0.3, rely=0.8)
        window.transient(master=self)

    def add_student(self):
        def save():
            def confirm():
                window.destroy()
                self.dbnew.overwrite("Student", f"Period{period}", "Student Name", str(i[1]), str(f"{self.user}, No"))
                print("Switched student to class")

            ids = student_id.get()
            period = classes.get()
            if period == '' or ids == "":
                label = customtkinter.CTkLabel(master=window, text="Please fill ALL the fields", text_color="red")
                label.place(relx=0.3, rely=.67)
            else:
                if period.isdigit() and ids.isdigit() and 8 >= int(period) >= 1:
                    students = self.dbnew.select("Student")
                    for i in students:
                        if int(ids) in i:
                            try:
                                if i[int(period) + 1].split(", ")[0] == self.user:
                                    label = customtkinter.CTkLabel(master=window, text="Student already registered in your class", text_color="red")
                                    label.place(relx=0.1, rely=.67)
                                    break
                                elif i[int(period) + 1] is not None:
                                    label = customtkinter.CTkLabel(master=window,
                                                                   text=f"Already registered in a {period} period. To confirm press the button again",
                                                                   text_color="red")
                                    label.place(relx=0.01, rely=.67)
                                    submit.destroy()
                                    confirms = customtkinter.CTkButton(master=window, text="Confirm Information", command=confirm, fg_color="green")
                                    confirms.place(relx=0.3, rely=0.8)
                                    break
                            except AttributeError:
                                self.dbnew.overwrite("Student", f"Period{period}", "Student Name", str(i[1]), str(f"{self.user}, No"))
                                print("Added student to class")
                                window.destroy()

                else:
                    label = customtkinter.CTkLabel(master=window, text="Period = Digit 1-8, ID = 7-Digits", text_color="red")
                    label.place(relx=0.3, rely=.67)

        window = customtkinter.CTkToplevel(self)
        window.title('Add Student')
        window.geometry("400x200")
        window.transient(master=self)
        student_name = customtkinter.CTkEntry(master=window, placeholder_text="Student Name...")
        student_id = customtkinter.CTkEntry(master=window, placeholder_text="Student ID...")
        classes = customtkinter.CTkEntry(master=window, placeholder_text="Class Period-Ex( 3, 8,..)")
        submit = customtkinter.CTkButton(master=window, text="Confirm Information", command=save, fg_color="green")
        student_id.place(relx=0.3, rely=0.1)
        classes.place(relx=0.3, rely=0.3)
        submit.place(relx=0.3, rely=0.5)

    def period1(self):
        """Period1-8 all show the list of the students in the class and weather they're attending class or not"""
        self.current = 1
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "1st Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[2] is None:
                continue
            i = student[2].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period2(self):
        self.current = 2
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "2nd Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[3] is None:
                continue
            i = student[3].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period3(self):
        self.current = 3
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "3rd Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[4] is None:
                continue

            i = student[4].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period4(self):
        self.current = 4
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "4th Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[5] is None:
                continue
            i = student[5].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period5(self):
        self.current = 5
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "5th Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[6] is None:
                continue
            num += 1
            i = student[6].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period6(self):
        self.current = 6
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "6th Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[7] is None:
                continue
            i = student[7].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period7(self):
        self.current = 7
        if self.user == "":
            print("ehy")
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "7th Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[8] is None:
                continue
            i = student[8].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def period8(self):
        self.current = 8
        if self.user == "":
            return
        if self.nostudents is not None:
            self.nostudents.destroy()
        self.textbox.configure(state='normal', text_font=("Serif", 10))
        self.textbox.textbox.delete("1.0", "end")
        self.textbox.insert("insert", "8th Period Class\n\n")
        classes = self.dbnew.select("Student")
        num = 0
        for student in classes:
            if student[9] is None:
                continue
            i = student[9].split(", ")
            if self.showing == "IDs":
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert", f"|SID#: {student[10]}     | Attended: ❌\n_______________________________________\n")
            else:
                if i[0].title() == self.user:
                    num += 1
                    if i[1] == "Yes":
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ✔\n_______________________________________\n")
                    else:
                        self.textbox.insert("insert",
                                            f"|Student: {student[1]}\t| Attended: ❌\n_______________________________________\n")
        else:
            if num == 0:
                if self.nostudents is not None:
                    self.nostudents.destroy()
                self.nostudents = customtkinter.CTkLabel(master=self, text=f"You don't have anyone in your period {self.current}")
                self.nostudents.place(relx=.35, rely=.3)
            self.textbox.configure(state="disabled", text_font=("Serif", 10))
            self.update()

    def help(self):
        """Makes sure that the classrooms are getting updated every so often (every 30s specifically)"""
        if self.current == 1:
            self.period1()
        elif self.current == 2:
            self.period2()
        elif self.current == 3:
            self.period3()
        elif self.current == 4:
            self.period4()
        elif self.current == 5:
            self.period5()
        elif self.current == 6:
            self.period6()
        elif self.current == 7:
            self.period7()
        else:
            self.period8()

    def update(self):
        hour = datetime.datetime.now(timezone('America/Chicago')).hour
        min = datetime.datetime.now(timezone('America/Chicago')).minute
        if hour > 16 or hour == 16 and min >= 30 or hour < 8 or hour == 8 and min < 23:
            pass
        customtkinter.CTk.after(self, ms=30000, func=self.help)


if __name__ == '__main__':
    app = App()
    app.mainloop()
