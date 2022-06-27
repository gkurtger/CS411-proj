from tkinter import *
from tkinter import ttk
from time import sleep
from backend import Backend

from sys import platform
from os import listdir as ls

# from py4j.java_gateway import JavaGateway


def todo():
    """place-holder to-do function"""
    print("to-do function")


class Safe_Word():

    main_window = None
    login_window = None

    main_window_title = "Safe Word"

    dpi_setting: str = None
    dpi_settings = dict()

    user_key = None # This is used to check if application is logged in. Ideally it's a key to decrypt stuff.
    user_data_path = None

    pw_listbox = []

    def __init__(self):
        self.GUI_debug = 0
        # create main window
        self.create_main_window()


    def status_update(self, displayed_text="", ifsame=None):
        """
        updates the text in the status bar.
        """
        # ifsame: only update the text
        # if the currently displayed text is the same as this string.
        
        if self.GUI_debug > 1:
            print("status_update('%s', condition = %s)"
                    %(displayed_text, ifsame))
        self.statusbar_label
        if ifsame == None:
            # do not check if the status text is the same as "ifsame"
            if self.statusbar_label['text'] == displayed_text:
                self.statusbar_label.config(text = " ")
                self.statusbar_label.after(20,
                                    lambda t = displayed_text:self.status_update(t))
            else: self.statusbar_label.config(text = displayed_text)
        else: # only change label if the text is the same as "ifsame"
            if self.statusbar_label['text'] == ifsame:
                self.statusbar_label.config(text = displayed_text)
        return None


    def user_authentication(self, username, password, window):
        """User authentication. Calls backend to verify user."""        
        if username == "" or password == "":
            error = Label(window, text="Enter user name or password")
            error.grid(row=3, column=1)
            return None

        login = Backend.check_password(username, password)
        # login = (True/False, user_key)
        if not login[0]:
            error = Label(window, text="Wrong username or password")
            error.grid(row=3, column=1)
        else:
            self.pw_listbox[0].delete(*self.pw_listbox[0].get_children())
            
            self.user_key = login[2]
            self.user_data_path = login[1]
            self.retrieve_passwords(login[2])

            self.main_window.title(self.main_window_title + " - " + '"%s"'%(username))
            
            window.destroy()
        return None

    def log_out(self, item):
        item.delete(*item.get_children())
        self.user_key = None
        self.user_data_path = None
        self.main_window.title(self.main_window_title)
        return None

    def retrieve_passwords(self, user_key):
        """Retrieve the user's passwords from backend."""
        if self.GUI_debug > 1: print("retrieve password")
        
        list_of_passwords = Backend.read_database(self.user_data_path)

        if len(list_of_passwords) == 0:
            self.status_update("No saved password. Press \"New Password\" to add one.")
            self.main_window.after(3000, lambda: self.status_update("", "No saved password. Press \"Add Password\" to add one."))
        for i in range(len(list_of_passwords)):
            self.pw_listbox[0].insert(parent="", index=END, text=str(i), value=list_of_passwords[i][:3])
        return

    def edit_password(self, old_pw: str, website, username, new_pw: str, encryption_choice, window_to_destroy: Toplevel):
        if website.strip() == "" or username.strip == "" or new_pw == "":
            self.status_update("Field missing")
            self.main_window.after(4000, lambda: self.status_update("", "Field missing"))
            return
        # old_pw is look up key for the ttk.Treeview
        old_pw_item = self.pw_listbox[0].item(old_pw)["values"]
        new_pw_item = (website, username, new_pw, encryption_choice)
        Backend.edit_password(self.user_data_path, old_pw_item, new_pw_item)
        self.pw_listbox[0].delete(*self.pw_listbox[0].get_children())
        self.retrieve_passwords(self.user_key)
        window_to_destroy.destroy()

    def add_password(self, website, username, password, encryption, listbox: list, window_to_destroy: Toplevel):
        if website.strip() == "" or username.strip == "" or password == "":
            self.status_update("Field missing")
            self.main_window.after(4000, lambda: self.status_update("", "Field missing"))
            return None

        # l = list(listbox[0].get_children())
        # l = [listbox[0].item(x)['values'] for x in l]
        # l.append([website, username, encryption])
        # l.sort()
        new_pw_item = (website, username, password, encryption)
        Backend.edit_password(self.user_data_path, None, new_pw_item)
        listbox[0].delete(*listbox[0].get_children())
        self.retrieve_passwords(self.user_key)

        window_to_destroy.destroy()
        self.status_update("Password saved")
        self.main_window.after(6000, lambda: self.status_update("", "Password saved"))
        return

    def add_password_window(self, user_key, listbox: list, title_text):
        if self.GUI_debug > 1: print("add_password")

        if self.user_key == None or self.user_key == "":
            self.status_update("Not logged in")
            self.main_window.after(4000, lambda: self.status_update("", "Not logged in"))
            return None

        if title_text == "Edit Password" and (len(listbox[0].selection()) == 0 or len(listbox[0].selection()) > 1):
            sleep(0.02)
            self.status_update("Select one entry to edit")
            self.main_window.after(6000, lambda m="Select one entry to edit": self.status_update("", m))
            return

        new_pw = Toplevel()
        new_pw.title(title_text)
        new_pw.lift()
        
        new_pw.columnconfigure(0, weight=0)
        new_pw.columnconfigure(1, weight=1)
        new_pw.rowconfigure(0, weight=0)
        new_pw.rowconfigure(1, weight=0)
        new_pw.rowconfigure(2, weight=0)
        new_pw.rowconfigure(3, weight=0)
        new_pw.rowconfigure(4, weight=1)

        website_l = Label(new_pw, text="Website")
        username_l = Label(new_pw, text="User name")
        newpw_l = Label(new_pw, text="Password")
        enc_l = Label(new_pw, text="Encryption")
        website_e = Entry(new_pw)
        username_e = Entry(new_pw)
        newpw_e = Entry(new_pw)

        padding = 10

        website_l.grid(row=0, column = 0, sticky="ns", pady=padding, padx=padding)
        username_l.grid(row=1, column = 0, sticky="ns", pady=padding, padx=padding)
        newpw_l.grid(row=2, column = 0, sticky="ns", pady=padding, padx=padding)
        enc_l.grid(row=3, column = 0, sticky="ns", pady=padding, padx=padding)
        website_e.grid(row=0, column = 1, sticky="swen", pady=padding, padx=padding)
        username_e.grid(row=1, column = 1, sticky="swen", pady=padding, padx=padding)
        newpw_e.grid(row=2, column = 1, sticky="swen", pady=padding, padx=padding)


        encryption_choice = StringVar()
        #may need a lookup function for the options below
        encryption_algorithms = list(Backend.list_of_encryptions.keys())
        encryption_choice.set(encryption_algorithms[0])
        encryption_option_menu = OptionMenu(
            new_pw, encryption_choice, *encryption_algorithms
        )
        encryption_option_menu.config(width=20)
        encryption_option_menu['anchor']='nw'
        encryption_option_menu.grid(row=3, column=1, sticky='nw', pady=padding)

        if title_text == "Add New Password":
            ok_button = Button(new_pw, text="Save",
                command=lambda this_window=new_pw: self.add_password(website_e.get(), username_e.get(), newpw_e.get(), encryption_choice.get(), listbox, this_window))
        if title_text == "Edit Password":
            website_e.insert(0, listbox[0].item(listbox[0].selection())["values"][0])
            username_e.insert(0, listbox[0].item(listbox[0].selection())["values"][1])
            encryption_choice.set(listbox[0].item(listbox[0].selection())["values"][2])
            ok_button = Button(new_pw, text="Save",
                command=lambda this_window=new_pw: self.edit_password(listbox[0].selection(), website_e.get(), username_e.get(), newpw_e.get(), encryption_choice.get(), this_window))

        cancel_button = Button(new_pw, text="Cancel", command=new_pw.destroy)
        ok_button.grid(row=4, column=0, sticky="nw", padx=padding, pady=padding)
        cancel_button.grid(row=4, column=1, sticky="nw", padx=padding, pady=padding)
        return
        

    def download_password(self, something1, something):
        if self.GUI_debug > 1: print("download_password_window")
        with open("export.txt", "w+") as write_to:
            with open(self.user_data_path, "r") as read_from:
                write_to.write(read_from.read())


    def delete_password_from_database(self, password_id, window_to_destroy: Toplevel==None):
        print(password_id)
        for item in password_id:
            old_pw_item = self.pw_listbox[0].item(item)["values"]
            Backend.edit_password(self.user_data_path, old_pw_item, None)
        self.pw_listbox[0].delete(*self.pw_listbox[0].get_children())
        self.retrieve_passwords(self.user_key)
        if window_to_destroy != None:
            window_to_destroy.destroy()
        return

    def delete_password_window(self, listbox: list):
        if self.GUI_debug > 1: print("delete_password_window")

        to_delete = listbox[0].selection()
        if len(to_delete) == 0:
            sleep(0.02)
            self.status_update("Nothing to delete")
            self.main_window.after(6000, lambda m="Nothing to delete": self.status_update("", m))
            return


        del_pw_confirm = Toplevel()
        del_pw_confirm.geometry(self.dpi_settings["small_window_geometry"])
        del_pw_confirm.title("Delete password")
        del_pw_confirm.lift()


        
        if len(to_delete) == 1:
            confirm_text = Label(del_pw_confirm, text="Confirm delete password?")
            delete_item_label = Label(del_pw_confirm, text=" ".join([str(x) for x in listbox[0].item(to_delete)["values"]]))
        else:
            confirm_text = Label(del_pw_confirm, text="Confirm delete")
            delete_item_label = Label(del_pw_confirm, text="%s items?" % (str(len(to_delete))))

        confirm_text.pack(side=TOP, pady=10)
        delete_item_label.pack()
        
        yes_button = Button(del_pw_confirm, text="Delete", background="#ee9999", highlightbackground="#ffcccc", activebackground="#ffcccc",
            command=lambda di=to_delete, this_window=del_pw_confirm: self.delete_password_from_database(di, this_window), width=15)
        yes_button.pack(pady=(50, 20))
        no_button = Button(del_pw_confirm, text="No", command=del_pw_confirm.destroy, width=15)
        no_button.pack()

        # TODO call backend to delete the password

        return

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
        main_window.title(self.main_window_title)
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
            "New\npassword": {"fun": self.add_password_window, "args": ["sfs", self.pw_listbox, "Add New Password"], "item": None},
            "Edit\npassword": {"fun": self.add_password_window, "args": ["sfs", self.pw_listbox, "Edit Password"], "item": None},
            "Delete\npassword": {"fun": self.delete_password_window, "args": [self.pw_listbox], "item": None},
            "Download\npasswords": {"fun": self.download_password, "args": ["sfs", self.pw_listbox], "item": None},
        }

        col_count = 0
        for b in top_frame_buttons:
            fun = top_frame_buttons[b]["fun"]
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

        status_label = Label(bottom_frame, text="")
        status_label.pack(side=RIGHT)
        self.statusbar_label = status_label

        main_window.after(100, self.show_login_window)
        self.main_window = main_window

        self.status_update("CS 411 group 4, summer 2022.")
        self.main_window.after(3000, lambda:self.status_update("", "CS 411 group 4, summer 2022."))



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


        if self.dpi_setting == 1:
            # standard scaling
            self.dpi_settings["main_window_geometry"] = "700x400"
            self.dpi_settings["bottom_frame_height"] = 20
            self.dpi_settings["log_in_window_geometry"] = "500x150"
            self.dpi_settings["small_window_geometry"] = "300x200"
            self.dpi_settings["dpi_scrollbar_width"] = 16
            self.dpi_settings["dpi_process_window_geometry"] = "200x100"
            self.dpi_settings["dpi_treeview_entry_height"] = 1
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
            self.dpi_settings["dpi_treeview_entry_height"] = 2
            self.dpi_settings["top_frame_height"] = 140

            ttk_style = ttk.Style()
            ttk_style.configure('Treeview', rowheight = 35)
    
    def start(self):
        self.main_window.mainloop()

        




if __name__ == "__main__":
    Safe_Word_App = Safe_Word()
    Safe_Word_App.start()
