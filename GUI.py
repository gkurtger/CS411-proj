from tkinter import *
from tkinter import ttk
from time import sleep


from sys import platform



class Backend():
    """place-holder backend"""
    def __init__(self):
        pass

    def check_password(self, username, password):
        if password == "0":
            return (False, "")
        else:
            return (True, "userkey")


def todo():
    """place-holder to-do function"""
    print("to-do function")


class Safe_Word():

    main_window = None
    login_window = None

    dpi_setting: str = None
    dpi_settings = dict()

    user_key = None # This is used to check if application is logged in. Ideally it's a key to decrypt stuff.
    

    def __init__(self):
        self.backend = Backend()
        self.GUI_debug = 2
        # create main window
        self.create_main_window()


    def user_authentication(self, username, password, window):
        """User authentication. Calls backend to verify user."""
        # TODO user auth.
        
        if username == "" or password == "":
            error = Label(window, text="Enter user name or password")
            error.grid(row=3, column=1)
            return None
            
        login = self.backend.check_password(username, password)
        # login = (True/False, user_key)
        if not login[0]:
            error = Label(window, text="Wrong username or password")
            error.grid(row=3, column=1)
        else:
            self.pw_listbox[0].delete(*self.pw_listbox[0].get_children())
            self.retrieve_passwords(login[1])
            window.destroy()
            self.user_key = login[1]
            
        return None

    def log_out(self, item):
        item.delete(*item.get_children())
        return None

    def retrieve_passwords(self, user_key):
        if self.GUI_debug > 1: print("retrieve password")
        list_of_passwords = None
        # TODO get user's passwords from backend:
        # return a list containing: website, username, encryption. No actual passwords.


        for j in range(100):
            self.pw_listbox[0].insert(parent="", index=END, text=str(j), value=[str(j), "something"+str(j+10), "something"+str(j*2-5)])

    def add_password(self, user_key, listbox: list):

        if self.GUI_debug > 1: print("add_password")
        # TODO call backend to add the new password
        ...

    def view_password(self, something1, something):
        if self.GUI_debug > 1: print("view_password_window")
        ...


    def delete_password_from_database(self, password_id):
        # TODO call backend to delete password
        print(password_id)
        ...

    def delete_password_window(self, listbox: list):
        if self.GUI_debug > 1: print("delete_password_window")
        del_pw_confirm = Toplevel()
        del_pw_confirm.geometry(self.dpi_settings["small_window_geometry"])
        del_pw_confirm.grab_set()

        delete_item = listbox[0].get(listbox[0].selection())
        print(delete_item)

        confirm_text = Label(del_pw_confirm, text="Confirm delete password?")
        confirm_text.pack(side=TOP, pady=10)
        
        yes_button = Button(del_pw_confirm, text="Delete", background="#ee9999", highlightbackground="#ffcccc", activebackground="#ffcccc",
            command=lambda b=listbox[0]: self.delete_password_from_database(b))
        yes_button.pack()
        no_button = Button(del_pw_confirm, text="No", command=del_pw_confirm.destroy)
        no_button.pack()

        # TODO call backend to delete the password
        ...

    def show_login_window(self):
        """Log in window."""
        login_window = Toplevel()
        login_window.title("Log in")
        login_window.geometry(self.dpi_settings["log_in_window_geometry"])
        login_window.lift()
        login_window.grab_set()

        login_window.columnconfigure(0, weight=0)
        login_window.columnconfigure(1, weight=1)
        login_window.rowconfigure(0, weight=0)
        login_window.rowconfigure(1, weight=0)
        login_window.rowconfigure(2, weight=0)


        username_text = Label(login_window, text="User name")
        username_text.grid(row=0, column=0, sticky="swen", pady=(30, 0), padx=(30, 10))
        username_entry = Entry(login_window)
        username_entry.grid(row=0, column=1, sticky="swen", pady=(30, 0), padx=(10, 30))

        password_text = Label(login_window, text="Password")
        password_text.grid(row=1, column=0, sticky="swen", pady=(30, 0), padx=(30, 10))
        password_entry = Entry(login_window, show="●")
        password_entry.grid(row=1, column=1, sticky="swen", pady=(30, 0), padx=(10, 30))

        login_button = Button(login_window, text="login", command=lambda: self.user_authentication(username_entry.get(), password_entry.get(), login_window))
        login_button.grid(row=2, column = 0, sticky="swen", pady=(20, 30), padx=10)


    def create_main_window(self):
        # create local window
        main_window = Tk()
        self.set_display_scale(main_window)
        main_window.title("Safe Word")
        main_window.geometry(self.dpi_settings["main_window_geometry"])

        # This is such that the object is passed by reference.
        self.pw_listbox = [None]

        menubar = Menu(main_window)
        
        menu_file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="Options", menu=menu_file)

        menu_file.add_command(label="Log in", command=self.show_login_window)
        menu_file.add_command(label="Log out", command=lambda a=self.pw_listbox: self.log_out(a[0]))
        menu_file.add_command(label="Exit", command=main_window.destroy)
        main_window.config(menu = menubar)

        top_frame_height = self.dpi_settings["top_frame_height"]

        top_frame_buttons_width = 10

        main_window.rowconfigure(0, weight=0)
        main_window.rowconfigure(1, weight=1)
        main_window.rowconfigure(2, weight=0)
        main_window.columnconfigure(0, weight=1)
        top_frame = Frame(main_window, height=top_frame_height, relief=SUNKEN, borderwidth=1)
        top_frame.grid(row=0, sticky="we", padx=10, pady=10)

        top_frame_buttons = {
            "New\npassword": {"fun": self.add_password, "args": ["sfs", self.pw_listbox], "item": None},
            "Edit\npassword": {"fun": self.add_password, "args": ["sfs", self.pw_listbox], "item": None},
            "Delete\npassword": {"fun": self.delete_password_window, "args": [self.pw_listbox], "item": None},
            "View\npassword": {"fun": self.view_password, "args": ["sfs", self.pw_listbox], "item": None},
        }

        col_count = 0
        for b in top_frame_buttons:
            fun = top_frame_buttons[b]["fun"]
            print(fun)
            top_frame_buttons[b]["item"] = Button(top_frame, text=b, height=3, width=top_frame_buttons_width, command=lambda fun=fun, b=b: fun(*top_frame_buttons[b]["args"]))
            top_frame_buttons[b]["item"].grid(row=0, column=col_count, sticky="swen")
            col_count += 1

        middle_frame = Frame(main_window, relief=SUNKEN, borderwidth=1)
        middle_frame.grid(row=1, sticky="swen", padx=10, pady=0)

        password_list_frame = Frame(middle_frame)
        password_list_frame.pack(fill=BOTH, expand=True)

        password_list = ttk.Treeview(password_list_frame, columns=("Website", "User name", "Encryption"))
        password_list.pack(side=LEFT, expand=True, fill=BOTH)
        password_list.column("#0", width = 0, stretch = NO)
        password_list.heading("Website", text = "Website", anchor = W)
        password_list.heading("User name", text = "User name", anchor = W)
        password_list.heading("Encryption", text = "Encryption", anchor = W)
        self.pw_listbox[0] = password_list


        pwlist_scrollbar = Scrollbar(
            password_list_frame,
            width = self.dpi_settings["dpi_scrollbar_width"],
            command = password_list.yview)
        pwlist_scrollbar.pack(side=RIGHT, fill=BOTH)
        password_list.config(yscrollcommand = pwlist_scrollbar.set)



        bottom_frame = Frame(main_window, height=self.dpi_settings["bottom_frame_height"], relief=SUNKEN, borderwidth=1)
        bottom_frame.grid(row=2, sticky="swen", padx=10, pady=10)

        main_window.after(2, self.show_login_window)
        self.main_window = main_window




    def set_display_scale(self, window):
        """Set display scale using DPI. Copied from existing project."""

        dpi = window.winfo_fpixels('1i')


        if platform == "win32" or platform == "darwin":
            self.dpi_setting = 1
        else:
            if dpi > 72:
                if self.GUI_debug >= 2: print("1x UI scale")
                self.dpi_setting = 1
            else:
                if self.GUI_debug >= 2: print("2x UI scale")
                self.dpi_setting = 2

        if self.dpi_setting == None:
            raise ValueError("Unknown DPI setting %s."% (str(self.dpi_setting)))

        print(self.dpi_setting)

        if self.dpi_setting == 1:
            # standard scaling
            self.dpi_settings["main_window_geometry"] = "700x400"
            self.dpi_settings["bottom_frame_height"] = 20
            self.dpi_settings["log_in_window_geometry"] = "500x150"
            self.dpi_settings["small_window_geometry"] = "300x150"
            self.dpi_settings["dpi_scrollbar_width"] = 16
            self.dpi_settings["dpi_process_window_geometry"] = "200x100"
            self.dpi_settings["dpi_about_page_geometry"] = "300x150"
            self.dpi_settings["dpi_author_window_geometry"] = "550x340"
            self.dpi_settings["dpi_treeview_entry_height"] = 1
            self.dpi_settings["dpi_description_box_border"] = 3
            self.dpi_settings["top_frame_height"] = 70

            ttk_style = ttk.Style()
            ttk_style.configure('Treeview', rowheight = 20)

        elif self.dpi_setting == 2:
            # double scaling
            self.dpi_settings["main_window_geometry"] = "1400x800"
            self.dpi_settings["bottom_frame_height"] = 40
            self.dpi_settings["log_in_window_geometry"] = "1000x300"
            self.dpi_settings["small_window_geometry"] = "600x300"
            self.dpi_settings["dpi_scrollbar_width"] = 28
            self.dpi_settings["dpi_process_window_geometry"] = "500x200"
            self.dpi_settings["dpi_about_page_geometry"] = "600x300"
            self.dpi_settings["dpi_author_window_geometry"] = "1170x590"
            self.dpi_settings["dpi_treeview_entry_height"] = 2
            self.dpi_settings["dpi_description_box_border"] = 5
            self.dpi_settings["top_frame_height"] = 140

            ttk_style = ttk.Style()
            ttk_style.configure('Treeview', rowheight = 35)
    
    def start(self):
        self.main_window.mainloop()




if __name__ == "__main__":
    Safe_Word_App = Safe_Word()
    Safe_Word_App.start()
