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
        """User authentication. True if authenticated, False if not."""
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
        login_button.grid(row=2, column = 0, sticky="swen", pady=(20, 30))


    def create_main_window(self):
        # create local window
        main_window = Tk()
        self.set_display_scale(main_window)
        main_window.title("Safe Word")
        main_window.geometry(self.dpi_settings["main_window_geometry"])

        
        
        
        
        
        
        
        
        main_window.after(1, self.show_login_window)


        self.main_window = main_window
            


    def todofunc(self):
        """place-holder to-do function"""
        print("to-do function")



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
            self.dpi_settings["main_window_geometry"] = "1000x670"
            self.dpi_settings["log_in_window_geometry"] = "500x200"
            self.dpi_settings["dpi_scrollbar_width"] = 16
            self.dpi_settings["dpi_option_menu_width"] = 10
            self.dpi_settings["dpi_language_dropdown_width"] = 18
            self.dpi_settings["dpi_process_window_geometry"] = "200x100"
            self.dpi_settings["dpi_progress_bar_length"] = 200
            self.dpi_settings["dpi_about_page_geometry"] = "600x300"
            self.dpi_settings["dpi_author_window_geometry"] = "550x340"
            self.dpi_settings["dpi_treeview_entry_height"] = 1
            self.dpi_settings["dpi_process_window_geometry_finished"] = "700x900"
            self.dpi_settings["dpi_description_box_border"] = 3

            ttk_style = ttk.Style()
            ttk_style.configure('Treeview', rowheight = 20)

        elif self.dpi_setting == 2:
            # double scaling
            self.dpi_settings["main_window_geometry"] = "2000x1150"
            self.dpi_settings["log_in_window_geometry"] = "1000x400"
            self.dpi_settings["dpi_scrollbar_width"] = 28
            self.dpi_settings["dpi_option_menu_width"] = 10
            self.dpi_settings["dpi_language_dropdown_width"] =18
            self.dpi_settings["dpi_process_window_geometry"] = "500x200"
            self.dpi_settings["dpi_progress_bar_length"] = 400
            self.dpi_settings["dpi_about_page_geometry"] = "1200x600"
            self.dpi_settings["dpi_author_window_geometry"] = "1170x590"
            self.dpi_settings["dpi_treeview_entry_height"] = 2
            self.dpi_settings["dpi_process_window_geometry_finished"] = "1400x1100"
            self.dpi_settings["dpi_description_box_border"] = 5

            ttk_style = ttk.Style()
            ttk_style.configure('Treeview', rowheight = 35)
    
    def start(self):
        self.main_window.mainloop()




if __name__ == "__main__":
    Safe_Word_App = Safe_Word()
    Safe_Word_App.start()
