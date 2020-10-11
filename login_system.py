#Created by Ayotomiwa Adekunle

import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Login System")
        tk.Tk.geometry(self, "300x150")
        tk.Tk.maxsize(self, 300, 150)


        container = tk.Frame(self)
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
    
    #Register function
    def register(self, cont, username, password):
        self.username = user_str.get()
        self.password = passw_str.get()

        with open("Account_info.txt", "a") as file:
            if len(self.username) or len(self.password) != 0:
                file.write(self.username + "," + self.password + "\n")
                username1.delete(0, "end")
                password1.delete(0, "end")
                self.show_frame(SucReg)
            else:
                invalid = tk.Tk()
                invalid.title("Error")

                error_label = tk.Label(invalid, text="Invalid username/password", font=("Arial", "10", "bold"))
                error_label.grid(row=0, column=0, padx=10, pady=10)

                button_close = tk.Button(invalid, text="OK", command= lambda: invalid.destroy())
                button_close.grid(row=1, column=0, padx=10, pady=10)

                invalid.mainloop()   
            
                
    #Login functionn
    def login(self, cont, username1, password1):
        self.username1 = user_str1.get()
        self.password1 = passw_str1.get()
        success = 0
        
        #File is read and each line is made into a list which is looped through
        with open("Account_info.txt", "r") as file:
            for line in file:
                split = line.strip().split(",")
                if self.username1 == split[0] and self.password1 == split[1]:
                    success += 1
            

        if success == 1:
            username.delete(0, "end")
            password.delete(0, "end")
            self.show_frame(SucLog)
        else:
            error1 = tk.Tk()
            error1.title("Error")

            text = tk.Label(error1, text="Wrong username/password", font=("Arial", "10", "bold"))
            text.grid(row=0, column=0, padx=10, pady=10)

            button_error = tk.Button(error1, text="OK", command=lambda: error1.destroy())
            button_error.grid(row=1, column=0, padx=10, pady=10)


            error1.mainloop()
        

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Created by Ayotomiwa Adekunle", font=('Arial', '10', 'bold'))
        label.pack()

        button1 = tk.Button(self, text="Login", width=20, height=1, command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10, pady=20)


        button2 = tk.Button(self, text="Register", width=20, height=1, command=lambda: controller.show_frame(PageTwo))
        button2.pack(padx=10, pady=10)

#Login Page
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global username
        global password
        global user_str1
        global passw_str1

        log = tk.Label(self, text="Login", font=('Arial', '10', 'bold')) 
        log.grid(column=1, row=0)

        user = tk.Label(self, text="Username")
        user.grid(column=0, row=1, padx=10, pady=10)

        passw = tk.Label(self, text="Password")
        passw.grid(column=0, row=2, padx=10, pady=10)

        user_str1 = tk.StringVar()
        username = tk.Entry(self, textvariable = user_str1)
        username.grid(column=1, row=1)

        passw_str1 = tk.StringVar()
        password = tk.Entry(self, show="*", textvariable = passw_str1)
        password.grid(column=1, row=2)


        button3 = tk.Button(self, text="Login", command=lambda: controller.login(SucLog, user_str1, passw_str1))
        button3.grid(column=1, row=3)
        
#Register Page
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global user_str
        global passw_str
        global username1
        global password1

        create = tk.Label(self, text="Create an Account", font=('Arial', '10', 'bold')) 
        create.grid(column=1, row=0)
  
        user1 = tk.Label(self, text="Username")
        user1.grid(column=0, row=1, padx=10, pady=10)

        passw1 = tk.Label(self, text="Password")
        passw1.grid(column=0, row=2, padx=10, pady=10)

        user_str = tk.StringVar()
        username1 = tk.Entry(self, textvariable = user_str)
        username1.grid(column=1, row=1)

        passw_str = tk.StringVar()
        password1 = tk.Entry(self, show="*", textvariable = passw_str)
        password1.grid(column=1, row=2)

        button4 = tk.Button(self, text="Register", command=lambda: controller.register(SucReg, user_str, passw_str))
        button4.grid(column=1, row=3)
        
#Succesful Register frame
class SucReg(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        reg_success = tk.Label(self, text="Succesful Registration", font=('Arial', '10', 'bold'))
        reg_success.pack()

        button1 = tk.Button(self, text="Login", width=20, height=1,  command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10, pady=20)

        button2 = tk.Button(self, text="Register", width=20, height=1,  command=lambda: controller.show_frame(PageTwo))
        button2.pack(padx=10, pady=10)

#Succesful Login frame
class SucLog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        reg_success = tk.Label(self, text="Succesful Login", font=('Arial', '10', 'bold'))
        reg_success.pack()

        button1 = tk.Button(self, text="Login", width=20, height=1,  command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10, pady=20)

        button2 = tk.Button(self, text="Register", width=20, height=1,  command=lambda: controller.show_frame(PageTwo))
        button2.pack(padx=10, pady=10)

app = App()
app.mainloop()
