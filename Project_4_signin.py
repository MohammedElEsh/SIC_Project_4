import tkinter as tk
import json
from tkinter import messagebox
import Project_4_signup
from Project_4_home import TwitterLikeApp


name = ''

def signin():
    signin = tk.Tk()
    signin.title("signin")
    signin.geometry('925x500+300+200')
    signin.configure(bg="#fff")
    signin.resizable(False, False)
    
    def moveTO_signup_pg():
        destroy_pg(signin)
        Project_4_signup.signup()
    
    
    def signin_action():
        global name
        
        email = emailfield.get()
        password = passwordfield.get()
        users = load_json_file('Project_4_users.json')
        # print(users)
        
        for user in users:
            if user["Email"] == email: 
                name = user['Name']
                break

        for user in users:
            if user['Email'] == email and user['Password'] == password:
                
                # messagebox.showinfo("signin Successful", "You have successfully logged in!")  
            
                destroy_pg(signin)
                
                root = tk.Tk()
                app = TwitterLikeApp(root)
                app.start()
                
                break
        else:
            messagebox.showerror("signin Error", "Invalid email or password")
                
            emailfield.delete(0, 'end')
            passwordfield.delete(0, 'end')
            
        return(name)
                
                


    # Create a Frame
    frame = tk.Frame(signin, bg="#0066ff")
    frame.place(relwidth=1, relheight=1)

    # Labels
    label2 = tk.Label(frame, text="Sign in to your existing Account", font=("MS Shell Dlg 2", 23),
                            fg="white", bg="#0066ff")
    label2.place(x=250, y=30)

    # Email Field
    emailfield = tk.Entry(frame, font=("MS Shell Dlg 2", 14))
    emailfield.place(x=250, y=180, width=471, height=51)

    # Password Field
    passwordfield = tk.Entry(frame, font=("MS Shell Dlg 2", 14), show="*")
    passwordfield.place(x=250, y=270, width=471, height=51)

    # Labels for Email and Password Fields
    label_3 = tk.Label(frame, text="Email", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    label_3.place(x=250, y=150)

    label_4 = tk.Label(frame, text="Password", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    label_4.place(x=250, y=240)


    # signin Button
    signin_btn = tk.Button(frame, text="Sign in", font=("MS Shell Dlg 2", 18), bg="#002966", fg="white", command=signin_action)
    signin_btn.place(x=250, y=350, width=471, height=61)


    # signup Button
    moveTO_signup = tk.Button(frame, text="Don't have an account!", font=("MS Shell Dlg 2", 10), bg="#002966", fg="white", command= moveTO_signup_pg)
    moveTO_signup.place(x=570, y=420, width=150, height=40)
    
    




    signin.mainloop()










    
def destroy_pg(pg_name):
    pg_name.destroy()  

def write_json_file(data, filename):
    file = open (filename,'w')
    json.dump(data , file , indent=2)
    # file.close()


def load_json_file(filename):
    file = open (filename,"r") 
    data = json.load(file)
    return data



# signin()