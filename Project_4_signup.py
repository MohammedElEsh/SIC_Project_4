import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
import Project_4_signin
from PIL import Image, ImageTk






def signup():

    def on_selection_change(event):
        city = cities.get()
        print(f"You selected: {city}")
        
    def moveTO_signin_pg():
        destroy_pg(signup)
        Project_4_signin.signin() 
    
        



    def store_in_db():
        userData = {
            "Name": userName.get().capitalize(),
            "phone": userPhone.get(),
            "Email": userMail.get(),
            "Password": userPass.get(),
            "Governorate": cities.get().capitalize(),
            "Age": userAge.get(),
            "Gender": userGender.get().capitalize(),
            "Bio": " ",
            "Following": 0,
            "Followers": 0
        }

        users = load_json_file('Project_4_users.json')

        email = userMail.get()
        password = userPass.get()

        for user in users:
            if user["Email"] == email or user["Password"] == password:
                messagebox.showerror("Signup Error", "Your Email or password is already used.")
                break
        else:
            users.append(userData)
            print("Done!")
            write_json_file(users, 'Project_4_users.json')
            messagebox.showinfo("Signup Successful", "You have successfully signed up!")

    
    
        destroy_pg(signup)
        Project_4_signin.signin() 
    
    
    signup = tk.Tk()
    signup.title("Create Account")
    signup.geometry("925x500+300+200")
    signup.configure(bg="#fff")
    signup.resizable(False, False)
    
    
    
    
    frame = tk.Frame(signup, bg="#0066ff")
    frame.pack(fill=tk.BOTH, expand=True)
    
    
    
    
    
    label = tk.Label(frame, text="Welcome", font=("MS Shell Dlg 2", 23), fg="white", bg="#0066ff")
    label.grid(row=0, column=1, pady=10)
    label2 = tk.Label(frame, text="Create Account For Free", font=("MS Shell Dlg 2", 20), fg="white", bg="#0066ff")
    label2.grid(row=1, column=1, pady=10)
    
    
    

    userName_lable = tk.Label(frame, text="name", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userName_lable.grid(row=2, column=0, pady=10)
    userName = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userName.grid(row=2, column=1, pady=10)
    
    
    
    
    

    userPhone_lable = tk.Label(frame, text="phone", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userPhone_lable.grid(row=3, column=0, pady=10)
    userPhone = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userPhone.grid(row=3, column=1, pady=10)
    
    
    
    
    
    
    
    userMail_lable = tk.Label(frame, text="Email", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userMail_lable.grid(row=4, column=0, pady=10)
    userMail = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userMail.grid(row=4, column=1, pady=10)
    
    
    
    
    userPass_lable = tk.Label(frame, text="Password", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userPass_lable.grid(row=5, column=0, pady=10)
    userPass = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userPass.grid(row=5, column=1, pady=10)
    
    
    
    
    
    
    userGovernnorate_lable = tk.Label(frame, text="Governorate", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userGovernnorate_lable.grid(row=6, column=0, pady=10)

    cities = tk.StringVar(frame)
    cities.set("cities")

    options = [
        "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum",
        "Gharbia", "Giza", "Ismailia", "Kafr El Sheikh", "Luxor", "Matrouh", "Minya", "Monufia", "New Valley",
        "North Sinai", "Port Said", "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"]

    cities_menu = ttk.Combobox(frame, textvariable=cities, values=options)
    cities_menu.bind("<<ComboboxSelected>>", on_selection_change)
    cities_menu.grid(row=6, column=1, pady=10)
    
    
    
    
    
    
    
    userAge_lable = tk.Label(frame, text="Age", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userAge_lable.grid(row=7, column=0, pady=10)
    userAge = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userAge.grid(row=7, column=1, pady=10)
    
    


    
    userGender_lable = tk.Label(frame, text="Gender", font=("MS Shell Dlg 2", 12), fg="white", bg="#0066ff")
    userGender_lable.grid(row=8, column=0, pady=10)
    userGender = tk.Entry(frame, font=("MS Shell Dlg 2", 13))
    userGender.grid(row=8, column=1, pady=10)
    
    
    

    register_button = tk.Button(frame, text="Register", font=("MS Shell Dlg 2", 15), bg="#002966", fg="white", command=store_in_db)
    register_button.grid(row=9, column=1, pady=3)
    
    # Load the image
    image_path = r"D:\SIC\SIC_Project_4\home.png"
    image = Image.open(image_path)
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image) 
    
        
    moveTo_signin = tk.Button(frame, text="  Already have an account!", font=("MS Shell Dlg 2", 10), bg="#002966", fg="white", command=moveTO_signin_pg, image=photo, compound=tk.LEFT)
    moveTo_signin.grid(row=9, column=2, pady=3)
    moveTo_signin.image = photo



    
    
    
    
    
    signup.mainloop()
        


  
def write_json_file(data, filename):
    file = open (filename,'w')
    json.dump(data , file , indent=2)
    # file.close()


def load_json_file(filename):
    file = open (filename,"r") 
    data = json.load(file)
    return data
    
def destroy_pg(pg_name):
    pg_name.destroy()    
    
    
     
# signup()