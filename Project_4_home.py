import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import json
from tkinter import messagebox
from Stack import Stack
import Project_4_signin


class TwitterLikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medium-like Home Page")
        self.root.geometry("800x600")

        # self.home_page_posts = []
        self.profile_posts = []

        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_search_box()
        self.create_tweet_box()
        self.create_buttons()
        self.create_tweet_feed()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#1DA1F2", height=50)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(header_frame, text="Medium", font=(
            "Helvetica", 18), fg="white", bg="#1DA1F2")
        header_label.pack()

    def create_search_box(self):
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill=tk.BOTH, padx=20, pady=(10, 5))
        self.search_entry = tk.Entry(
            search_frame, font=("Helvetica", 14), fg='gray')
        self.search_entry.insert(0, "Search for users")
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_users_by_name,
                                  bg="#1DA1F2", fg="white", font=("Helvetica", 14))
        search_button.pack(side=tk.LEFT)
        
        
        
        

    def on_entry_click(self, event):
        if self.search_entry.get() == "Search for users":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='black')

    def on_focus_out(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, "Search for users")
            self.search_entry.config(fg='gray')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    def search_users_by_name(self):
        name = self.search_entry.get()
        users = load_json_file('Project_4_users.json')
        results = []
        for user in users:
            if name.lower() in user["Name"].lower():
                results.append(user)

        if results:
            search_pg = tk.Tk()
            search_pg.configure(bg="black")
            search_pg.geometry("700x400")
            search_pg.title("Search results")





            # Create a canvas to hold the scrollable frame
            canvas = tk.Canvas(search_pg, bg="black")
            canvas.pack(side="left", fill="both", expand=True)

            # Create a scrollbar and associate it with the canvas
            scrollbar = tk.Scrollbar(
                search_pg, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")

            # Configure the canvas to use the scrollbar
            canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame inside the canvas to hold the search results
            results_frame = tk.Frame(canvas, bg="black")
            results_frame.pack(fill="both", expand=True)

            # Add the frame to the canvas
            canvas.create_window((0, 0), window=results_frame, anchor="nw")

            def on_configure(event):
                # Update the scrollable region when the size of the frame changes
                canvas.configure(scrollregion=canvas.bbox("all"))

            # Call the on_configure function when the frame size changes
            results_frame.bind("<Configure>", on_configure)
            
            
            

            def follow_click(userName):
                users = load_json_file('Project_4_users.json')
                name = Project_4_signin.name

                for user in users:
                    if user["Name"] == name:
                        user["Following"] += 1
                    if user["Name"] == userName:
                        user["Followers"] += 1

                    write_json_file(users, 'Project_4_users.json')

            def unfollow_click(userName):
                users = load_json_file('Project_4_users.json')
                name = Project_4_signin.name

                for user in users:
                    if user["Name"] == name:
                        if user["Following"] > 0:
                            user["Following"] -= 1
                    if user["Name"] == userName:
                        if user["Followers"] > 0:
                            user["Followers"] -= 1

                write_json_file(users, 'Project_4_users.json')

            for user in results:
                frame = tk.LabelFrame(
                    results_frame, text="User Details", fg="white", bg="#1162FF")
                frame.pack(pady=5)

                name_label = tk.Label(frame, text=f"Name: {user['Name']}")
                name_label.pack(pady=5)

                bio_label = tk.Label(frame, text=f"Bio: {user['Bio']}")
                bio_label.pack(pady=5)

                following_label = tk.Label(
                    frame, text=f"Following: {user['Following']}")
                following_label.pack(pady=5)

                followers_label = tk.Label(
                    frame, text=f"Followers: {user['Followers']}")
                followers_label.pack(pady=5)

                # Create a "Follow" button
                follow_button = tk.Button(
                    frame, text="Follow", fg="white", bg="green", command=lambda u=user: follow_click(u['Name']))
                follow_button.pack(side="left", padx=5)

                # Create an "Unfollow" button
                unfollow_button = tk.Button(
                    frame, text="Unfollow", fg="white", bg="red", command=lambda u=user: unfollow_click(u['Name']))
                unfollow_button.pack(side="left", padx=5)

            search_pg.mainloop()

        else:
            messagebox.showerror("Error", "User not found!")
            self.search_entry.delete(0, tk.END)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    def create_tweet_box(self):
        posts = load_json_file('Project_4_posts.json')

        def on_selection_change(event):
            topic = topics.get()
            print(f"You selected: {topic}")

        topics_frame = tk.Frame(self.root)
        topics_frame.pack(fill=tk.BOTH, padx=20, pady=5)

        userTopics_label = tk.Label(topics_frame, text="Choose a topic to post in !", font=("MS Shell Dlg 2", 12), fg="white", bg="black")
        userTopics_label.pack(side=tk.LEFT, padx=5)

        topics = tk.StringVar(topics_frame)
        topics.set("Topics")

        for topic in posts:
            options = list(posts.keys())

        topics_menu = ttk.Combobox(topics_frame, textvariable=topics, values=options)
        topics_menu.bind("<<ComboboxSelected>>", on_selection_change)
        topics_menu.pack(side=tk.LEFT, padx=5)

        tweet_box_frame = tk.Frame(self.root)
        tweet_box_frame.pack(fill=tk.BOTH, padx=20, pady=5)

        tweet_button = tk.Button(tweet_box_frame, text="Post", command=lambda: self.post_tweet(topics.get()), bg="#1DA1F2", fg="white", font=("Helvetica", 14))
        tweet_button.pack(side=tk.LEFT, padx=5)

        self.tweet_text = scrolledtext.ScrolledText(tweet_box_frame,width=30,height=5,font=("Helvetica", 14))
        self.tweet_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def create_buttons(self):
        posts = load_json_file('Project_4_posts.json')

        def on_selection_change(event):
            topic = topics.get()
            print(f"You selected: {topic}")

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, padx=20, pady=5)

        profile_button = tk.Button(button_frame, text="Profile", command=lambda: self.open_profile(Project_4_signin.name), bg="#1DA1F2", fg="white", font=("Helvetica", 14))
        profile_button.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(button_frame, text="Search", command=lambda: self.search_tweets(topics.get()), bg="#1DA1F2", fg="white", font=("Helvetica", 14))
        search_button.pack(side=tk.LEFT, padx=5)

        topics_frame = tk.Frame(self.root)
        topics_frame.pack(fill=tk.BOTH, padx=20, pady=5)

        userTopics_label = tk.Label(topics_frame, text="Choose a topic to search for !", font=("MS Shell Dlg 2", 12), fg="white", bg="black")
        userTopics_label.pack(side=tk.LEFT, padx=5)

        topics = tk.StringVar(topics_frame)
        topics.set("Topics")

        for topic in posts:
            options = list(posts.keys())
        # print(options)

        topics_menu = ttk.Combobox(topics_frame, textvariable=topics, values=options)
        topics_menu.bind("<<ComboboxSelected>>", on_selection_change)
        topics_menu.pack(side=tk.LEFT, padx=5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def search_tweets(self, topic):
        posts = load_json_file('Project_4_posts.json')

        results_window = tk.Tk()
        results_window.configure(bg="#4d4d4d")
        results_window.title("Search Results")
        results_window.geometry("400x600")

        for post in posts[topic]:
            print(post)

            frame = tk.LabelFrame(results_window, text="post", fg="white", bg="#1162FF")
            frame.pack(pady=5)

            post_label = tk.Label(results_window, text=post)
            post_label.pack(pady=5)

        results_window.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def post_tweet(self, topic):
        def append_to_list(new_post):
            posts = load_json_file('Project_4_posts.json')

            posts[topic].append(new_post)
            print(posts[topic])

            write_json_file(posts, 'Project_4_posts.json')
            print(new_post, "appended to the", topic, "list.")

        append_to_list(self.tweet_text.get("1.0", tk.END).rstrip())

        tweet = self.tweet_text.get(1.0, tk.END)
        if tweet.strip():
            self.profile_posts.insert(0, tweet)
            self.clear_profile_listbox()
            for post in self.profile_posts:
                self.profile_posts_listbox.insert(tk.END, post)
            self.save_tweets_to_file()
            self.tweet_text.delete(1.0, tk.END)
            self.update_character_count()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def create_tweet_feed(self):
        self.tweet_listbox = tk.Listbox(self.root, font=("Helvetica", 12), selectbackground="#1DA1F2", selectforeground="white")
        self.tweet_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)



    def clear_profile_listbox(self):
        self.profile_posts_listbox.delete(0, tk.END)
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def open_profile(self, name):
        users = load_json_file('Project_4_users.json')

        def edit_name(userName):
            for user in users:
                if user["Name"] == name:
                    user["Name"] = edit_name_entry.get().capitalize()
                    messagebox.showinfo("Update", "Your new name is " + user["Name"])
                    write_json_file(users, 'Project_4_users.json')
                    break

        def edit_bio(userName):
            for user in users:
                if user["Name"] == name:
                    user["Bio"] = edit_bio_entry.get()
                    messagebox.showinfo("Update", "Your new bio is " + user["Bio"])
                    write_json_file(users, 'Project_4_users.json')
                    break

        for user in users:
            if user["Name"] == name:
                bio = user["Bio"]
                following = str(user["Following"])
                followers = str(user["Followers"])
                

        profile_frame = tk.LabelFrame(self.root, text="User Profile", font=("Helvetica", 14))
        profile_frame.place(relx=0.7, rely=0.1, relwidth=0.28, relheight=0.8)

        username_label = tk.Label(profile_frame, text="User Name: " + name, font=("Helvetica", 12))
        username_label.pack(pady=10)

        bio_label = tk.Label(profile_frame, text="Bio: " + bio, font=("Helvetica", 8))
        bio_label.pack()

        following_label = tk.Label(profile_frame, text="Following: " + following, font=("Helvetica", 10))
        following_label.pack()

        followers_label = tk.Label(profile_frame, text="Followers: " + followers, font=("Helvetica", 10))
        followers_label.pack()

        edit_name_entry = tk.Entry(profile_frame, font=("Helvetica", 10))
        edit_name_entry.pack()
        
        

        edit_name_button = tk.Button(profile_frame, text="Edit Your Name", font=("Helvetica", 10), bg="blue", fg="white", command=lambda: edit_name(name))
        edit_name_button.pack()

        edit_bio_entry = tk.Entry(profile_frame, font=("Helvetica", 10))
        edit_bio_entry.pack()

        edit_bio_button = tk.Button(profile_frame, text="Edit Your Bio", font=("Helvetica", 10), bg="blue", fg="white", command=lambda: edit_bio(name))
        edit_bio_button.pack()

        profile_posts_label = tk.Label(profile_frame, text="My Posts", font=("Helvetica", 14))
        profile_posts_label.pack(pady=10)
        
        
        

        

        self.profile_posts_listbox = tk.Listbox(profile_frame, font=("Helvetica", 12), selectbackground="#1DA1F2", selectforeground="white")
        self.profile_posts_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        for post in self.profile_posts:
            self.profile_posts_listbox.insert(tk.END, post)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    def clear_tweet_listbox(self):
        self.tweet_listbox.delete(0, tk.END)

    def save_tweets_to_file(self):
        with open("user.txt", "w") as file:
            for tweet in self.profile_posts:
                file.write(tweet + "\n")

    def start(self):
        home_page_posts = Stack()

        try:
            with open("user.txt", "r") as file:
                for line in file:

                    # self.home_page_posts.append(line.strip())
                    home_page_posts.push(line.strip())

        except FileNotFoundError:
            pass

        self.root.mainloop()


def destroy_pg(pg_name):
    pg_name.destroy()


def write_json_file(data, filename):
    file = open(filename, 'w')
    json.dump(data, file, indent=2)
    # file.close()


def load_json_file(filename):
    file = open(filename, "r")
    data = json.load(file)
    return data



# root = tk.Tk()
# app = TwitterLikeApp(root)
# app.start()