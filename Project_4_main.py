import tkinter as tk
import json
import Project_4_signin as signin
import Project_4_signup as signup




def pg1():
    pg1 = tk.Tk()
    pg1.title("Welcome Page")
    pg1.geometry('925x500+300+200')
    pg1.configure(bg="#fff")
    pg1.resizable(False, False)
    
    
    
    def signin_action():
        destroy_pg(pg1)
        signin.signin()

    def create_account_action():
        destroy_pg(pg1)
        signup.signup()
    
    
    

    

    
    
    

    # Create a Frame
    frame = tk.Frame(pg1, bg="#0066ff")  
    frame.pack(fill=tk.BOTH, expand=True)

    # Labels
    label = tk.Label(frame, text="Welcome", font=("MS Shell Dlg 2", 33), fg="white", bg="#0066ff")
    label.place(x=400, y=100)

    label2 = tk.Label(frame, text="Sign in or Create a New Account", font=("MS Shell Dlg 2", 23), fg="white", bg="#0066ff")
    label2.place(x=270, y=180)

    # Sign-in Button
    signin_button = tk.Button(frame, text="Sign in", font=("MS Shell Dlg 2", 18), bg="white", command=signin_action)
    signin_button.place(x=230, y=280, width=520, height=61)

    # Create Account Button
    create_button = tk.Button(frame, text="Create New Account For Free", font=("MS Shell Dlg 2", 18), bg="white",command=create_account_action)
    create_button.place(x=230, y=380, width=520, height=61)
    

    pg1.mainloop()


    


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
    
pg1()