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
    

    GUI_debug = 0
    def __init__(self):
        self.backend = Backend()
        self.GUI_debug = 0
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
        if not login[0]:
            error = Label(window, text="Wrong username or password")
            error.grid(row=3, column=1)
        else:
            window.destroy()
            self.user_key = login[1]
            
        return None

    def log_out(self, item):
        item.delete(*item.get_children())
        return None

    def retrieve_passwords(self, user_key, listbox: ttk.Treeview):
        ...

    def add_password(self, user_key, listbox: ttk.Treeview):
        ...

    def delete_password(self, listbox: ttk.Treeview):
        del_pw_confirm = Toplevel()
        confirm_text = Label(self.main_window, text="Confirm delete password?")
        
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


        menubar = Menu(main_window)
        
        menu_file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="Options", menu=menu_file)

        menu_file.add_command(label="Log in", command=self.show_login_window)
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
            "New\npassword": {"fun": todo, "item": None}, "Edit\npassword": {"fun": todo, "item": None},
            "Delete\npassword": {"fun": todo, "item": None}, "View\npassword": {"fun": todo, "item": None},
        }

        col_count = 0
        for b in top_frame_buttons:
            top_frame_buttons[b]["item"] = Button(top_frame, text=b, height=3, width=top_frame_buttons_width, command=top_frame_buttons[b]["fun"])
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

        menu_file.add_command(label="Log out", command=lambda:self.log_out(password_list))
        menu_file.add_command(label="Exit", command=main_window.destroy)

        pwlist_scrollbar = Scrollbar(
            password_list_frame,
            width = self.dpi_settings["dpi_scrollbar_width"],
            command = password_list.yview)
        pwlist_scrollbar.pack(side=RIGHT, fill=BOTH)
        password_list.config(yscrollcommand = pwlist_scrollbar.set)

        for j in range(100):
            password_list.insert(parent="", index=END, text=str(j), value=[str(j), "something"+str(j+10), "something"+str(j*2-5)])


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
