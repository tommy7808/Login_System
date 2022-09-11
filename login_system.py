# Created by Ayotomiwa Adekunle

from tkinter import Frame, Tk, Label, Button, StringVar, Entry

import utils


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.title(self, "Login System")
        Tk.geometry(self, "300x150")
        Tk.maxsize(self, 300, 150)

        # Main frame for app
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, SucReg, SucLog):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # Register function
    def register(self, username, password, uname_field, passw_field):
        # Get username and password from fields
        self.username = username.get()
        self.password = password.get()

        with open("Account_info.txt", "a") as file:
            if utils.validate_register(self.username, self.password):
                file.write(f'{self.username},{self.password}\n')

                # Clear fields
                uname_field.delete(0, "end")
                passw_field.delete(0, "end")

                # Show Successful Registration Frame
                self.show_frame(SucReg)
            else:
                # Create error window
                invalid = Tk()
                invalid.title("Error")

                error_label = Label(
                    invalid, text="Invalid username/password", font=("Arial", "10", "bold"))
                error_label.grid(row=0, column=0, padx=10, pady=10)

                info_label = Label(invalid, text="A valid username is at least 5 characters long\n\nA valid password is at least 8 characters long,\nhas at least one uppercase and lower case letter,\nhas at least one number and special character", font=(
                    "Arial", "10"))
                info_label.grid(row=1, column=0, padx=10, pady=10)

                button_close = Button(invalid, text="OK",
                                      command=lambda: invalid.destroy())
                button_close.grid(row=2, column=0, padx=10, pady=10)

                invalid.mainloop()

    # Login function
    def login(self, username, password, uname_field, passw_field):
        self.username = username.get()
        self.password = password.get()
        success = 0

        # File is read and each line is made into a list which is looped through
        with open("Account_info.txt", "r") as file:
            for line in file:
                split = line.strip().split(",")
                if self.username == split[0] and self.password == split[1]:
                    success += 1

        if success == 1:
            uname_field.delete(0, "end")
            passw_field.delete(0, "end")
            self.show_frame(SucLog)
        else:
            error1 = Tk()
            error1.title("Error")

            text = Label(error1, text="Wrong username/password",
                         font=("Arial", "10", "bold"))
            text.grid(row=0, column=0, padx=10, pady=10)

            button_error = Button(
                error1, text="OK", command=lambda: error1.destroy())
            button_error.grid(row=1, column=0, padx=10, pady=10)

            error1.mainloop()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        author_label = Label(self, text="Created by Ayotomiwa Adekunle",
                             font=('Arial', '10', 'bold'))
        author_label.pack()

        login_button = Button(self, text="Login", width=20, height=1,
                              command=lambda: controller.show_frame(PageOne))
        login_button.pack(padx=10, pady=20)

        register_button = Button(self, text="Register", width=20, height=1,
                                 command=lambda: controller.show_frame(PageTwo))
        register_button.pack(padx=10, pady=10)

# Login Page


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        login_label = Label(self, text="Login", font=('Arial', '10', 'bold'))
        login_label.grid(column=1, row=0)

        username_label = Label(self, text="Username")
        username_label.grid(column=0, row=1, padx=10, pady=10)

        password_label = Label(self, text="Password")
        password_label.grid(column=0, row=2, padx=10, pady=10)

        user_str = StringVar()
        username_field = Entry(self, textvariable=user_str)
        username_field.grid(column=1, row=1)

        passw_str = StringVar()
        password_field = Entry(self, show="*", textvariable=passw_str)
        password_field.grid(column=1, row=2)

        login_button = Button(
            self, text="Login", command=lambda: controller.login(user_str, passw_str, username_field, password_field))
        login_button.grid(column=1, row=3)

# Register Page


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        create_label = Label(self, text="Create an Account",
                             font=('Arial', '10', 'bold'))
        create_label.grid(column=1, row=0)

        username_label = Label(self, text="Username")
        username_label.grid(column=0, row=1, padx=10, pady=10)

        password_label = Label(self, text="Password")
        password_label.grid(column=0, row=2, padx=10, pady=10)

        user_str = StringVar()
        username_field = Entry(self, textvariable=user_str)
        username_field.grid(column=1, row=1)

        passw_str = StringVar()
        password_field = Entry(self, show="*", textvariable=passw_str)
        password_field.grid(column=1, row=2)

        register_button = Button(self, text="Register",
                                 command=lambda: controller.register(user_str, passw_str, username_field, password_field))
        register_button.grid(column=1, row=3)

# Succesful Register frame


class SucReg(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        success_label = Label(self, text="Succesful Registration",
                              font=('Arial', '10', 'bold'))
        success_label.pack()

        login_button = Button(self, text="Login", width=20, height=1,
                              command=lambda: controller.show_frame(PageOne))
        login_button.pack(padx=10, pady=20)

        register_button = Button(self, text="Register", width=20, height=1,
                                 command=lambda: controller.show_frame(PageTwo))
        register_button.pack(padx=10, pady=10)

# Succesful Login frame


class SucLog(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        success_label = Label(self, text="Succesful Login",
                              font=('Arial', '10', 'bold'))
        success_label.pack()

        login_button = Button(self, text="Login", width=20, height=1,
                              command=lambda: controller.show_frame(PageOne))
        login_button.pack(padx=10, pady=20)

        register_button = Button(self, text="Register", width=20, height=1,
                                 command=lambda: controller.show_frame(PageTwo))
        register_button.pack(padx=10, pady=10)


app = App()
app.mainloop()
